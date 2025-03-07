# -*- coding: utf-8 -*-
import streamlit as st
import noisereduce as nr
import librosa
import soundfile as sf
import numpy as np
import io
import matplotlib.pyplot as plt
from scipy.signal import wiener
from librosa.effects import time_stretch, pitch_shift
import os
import tempfile
import subprocess
import logging
import whisper
from typing import Union

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)

# --- Funktionsdefinitionen (Audiobearbeitung) ---
RAUSCHTYPEN_TRADITIONELL = ['stationär', 'nicht_stationär']
ALGORITHMUS_OPTIONEN = ['noisereduce_basic', 'noisereduce_adaptive', 'wiener_filter']
DEFAULT_ALGORITHMUS = 'noisereduce_basic'


def rauschreduktion_audio_datei_streamlit(y, sr, algorithmus=DEFAULT_ALGORITHMUS, rauschtyp='stationär', **kwargs):
    if algorithmus == 'noisereduce_basic':
        if rauschtyp == 'stationär':
            reduced_noise = nr.reduce_noise(y=y, sr=sr, stationary=True, **kwargs)
        else:
            reduced_noise = nr.reduce_noise(y=y, sr=sr, stationary=False, **kwargs)
    elif algorithmus == 'noisereduce_adaptive':
        if rauschtyp == 'stationär':
            adaptive_parameter_stationaer = {'prop_decrease': 0.9, 'time_constant_s': 2.0, **kwargs}
            reduced_noise = nr.reduce_noise(y=y, sr=sr, stationary=True, **adaptive_parameter_stationaer)
        else:
            adaptive_parameter_nicht_stationaer = {'prop_decrease': 0.7, 'time_constant_s': 0.8, **kwargs}
            reduced_noise = nr.reduce_noise(y=y, sr=sr, stationary=False, **adaptive_parameter_nicht_stationaer)
    elif algorithmus == 'wiener_filter':
        reduced_noise = wiener(y, **kwargs)
        reduced_noise = np.clip(reduced_noise, -1, 1)
    else:
        raise ValueError(f"Ungültiger Algorithmus: {algorithmus}")
    return reduced_noise


def trim_audio(y, sr, start_time, end_time):
    start_sample = int(start_time * sr)
    end_sample = int(end_time * sr)
    return y[start_sample:end_sample]


def adjust_volume(y, volume_factor):
    return y * volume_factor


def adjust_speed(y, speed_factor):
    return time_stretch(y, rate=speed_factor)


def adjust_pitch(y, sr, pitch_factor):
    return pitch_shift(y, sr=sr, n_steps=pitch_factor)


def reverse_audio(y):
    return np.flip(y)


def fade_in_audio(y, sr, fade_duration=0.05):
    fade_samples = int(fade_duration * sr)
    fade_in_curve = np.linspace(0, 1, fade_samples)
    y[:fade_samples] *= fade_in_curve
    return y


def fade_out_audio(y, sr, fade_duration=0.05):
    fade_samples = int(fade_duration * sr)
    fade_out_curve = np.linspace(1, 0, fade_samples)
    y[-fade_samples:] *= fade_out_curve
    return y


def normalize_audio(y):
    max_amplitude = np.max(np.abs(y))
    if max_amplitude > 0:
        return y / max_amplitude
    return y


def display_waveform(y, sr, start_time=None, end_time=None):
    fig, ax = plt.subplots(figsize=(10, 2))
    librosa.display.waveshow(y, sr=sr, ax=ax)
    if start_time is not None and end_time is not None:
        ax.axvspan(start_time, end_time, color='red', alpha=0.3, label='Auswahl')
        ax.legend()
    ax.set_title("Audio-Wellenform")
    ax.set_xlabel("Zeit (Sekunden)")
    ax.set_ylabel("Amplitude")
    st.pyplot(fig)


# --- Funktionsdefinitionen (Video-Untertitelung) ---
def erstelle_srt(segmente: list[dict]) -> str:
    srt_inhalt = ""
    for index, segment in enumerate(segmente, start=1):
        start = segment['start']
        ende = segment['end']
        text = segment['text'].strip()

        start_zeit = sekunden_zu_srt_zeit(start)
        end_zeit = sekunden_zu_srt_zeit(ende)

        srt_inhalt += f"{index}\n{start_zeit} --> {end_zeit}\n{text}\n\n"

    return srt_inhalt


def sekunden_zu_srt_zeit(sekunden: float) -> str:
    millis = int((sekunden - int(sekunden)) * 1000)
    h = int(sekunden // 3600)
    m = int((sekunden % 3600) // 60)
    s = int(sekunden % 60)
    return f"{h:02}:{m:02}:{s:02},{millis:03}"


def transkribiere_audio_zu_srt(dateipfad: str, model, sprache: Union[str, None]) -> str:
    ergebnis = model.transcribe(dateipfad, fp16=False, language=sprache)
    segmente = ergebnis['segments']
    return erstelle_srt(segmente)


def merge_video_mit_srt(video_path: str, srt_path: str, output_path: str) -> tuple[bool, str]:
    srt_path_safe = srt_path.replace('\\', '/').replace(':', '\\:')

    command = [
        "ffmpeg",
        "-i", video_path,
        "-vf", f"subtitles='{srt_path_safe}'",
        "-c:v", "libx264",
        "-c:a", "copy",
        "-y",
        output_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        logging.error(f"FFmpeg Fehler: {result.stderr}")

    return result.returncode == 0, result.stderr


def validate_srt(content: str) -> bool:
    try:
        entries = content.strip().split("\n\n")
        for entry in entries:
            lines = entry.split("\n")
            if len(lines) < 3:
                return False
            if "-->" not in lines[1]:
                return False
        return True
    except:
        return False


# --- Streamlit App ---
def main():
    st.title("🎧🎬 Audio & Video Editor")

    # Tabs für Audiobearbeitung und Videountertitelung
    app_mode = st.sidebar.selectbox("Wähle den Modus:", ["Audio Editor", "Video Untertitelung"])

    if app_mode == "Audio Editor":
        audio_editor()
    elif app_mode == "Video Untertitelung":
        video_untertitelung()


def audio_editor():
    st.header("Audio Editor")
    uploaded_file = st.file_uploader("Audio-Datei hochladen (WAV, MP3, FLAC)", type=["wav", "mp3", "flac"])

    if uploaded_file is not None:
        try:
            y, sr = librosa.load(uploaded_file)
            y = np.asarray(y)
            duration = librosa.get_duration(y=y, sr=sr)
            st.session_state['original_duration'] = duration

            st.audio(y, format='audio/wav', sample_rate=sr)
            display_waveform(y, sr)

            st.sidebar.header("Audiofunktionen")

            # --- Rauschunterdrückung ---
            with st.sidebar.expander("Rauschunterdrückung", expanded=False):
                st.subheader("Rauschunterdrückung")
                rauschtyp_wahl = st.selectbox("Rauschtyp", RAUSCHTYPEN_TRADITIONELL, index=0)
                algorithmus_wahl = st.selectbox("Algorithmus", ALGORITHMUS_OPTIONEN, index=0)
                reduce_noise_button = st.button("Rauschen reduzieren")

            # --- Zuschneiden ---
            with st.sidebar.expander("Zuschneiden", expanded=False):
                st.subheader("Zuschneiden")
                start_time_rel = st.slider("Startzeit (relativ)", min_value=0.0, max_value=1.0, value=0.0, step=0.01,
                                             format="%.2f")
                end_time_rel = st.slider("Endzeit (relativ)", min_value=0.0, max_value=1.0, value=1.0, step=0.01,
                                           format="%.2f")
                trim_button = st.button("Zuschneiden")
                start_time = duration * start_time_rel
                end_time = duration * end_time_rel

            # --- Lautstärke ---
            with st.sidebar.expander("Lautstärke", expanded=False):
                st.subheader("Lautstärke anpassen")
                volume_factor = st.slider("Lautstärke Faktor", min_value=0.0, max_value=2.0, value=1.0, step=0.1)
                adjust_volume_button = st.button("Lautstärke anwenden")

            # --- Geschwindigkeit ---
            with st.sidebar.expander("Geschwindigkeit", expanded=False):
                st.subheader("Geschwindigkeit anpassen")
                speed_factor = st.slider("Geschwindigkeitsfaktor", min_value=0.5, max_value=2.0, value=1.0, step=0.1)
                adjust_speed_button = st.button("Geschwindigkeit anwenden")

            # --- Tonhöhe ---
            with st.sidebar.expander("Tonhöhe", expanded=False):
                st.subheader("Tonhöhe anpassen")
                pitch_factor = st.slider("Tonhöhenschritte (Halbtöne)", min_value=-12, max_value=12, value=0, step=1)
                adjust_pitch_button = st.button("Tonhöhe anwenden")

            # --- Umkehren ---
            with st.sidebar.expander("Umkehren", expanded=False):
                st.subheader("Audio umkehren")
                reverse_button = st.button("Audio umkehren")

            # --- Fade In/Out ---
            with st.sidebar.expander("Fade In/Out", expanded=False):
                st.subheader("Fade In/Out Effekte")
                fade_in_duration = st.slider("Fade-In Dauer (Sekunden)", min_value=0.0, max_value=1.0, value=0.05,
                                              step=0.01)
                fade_out_duration = st.slider("Fade-Out Dauer (Sekunden)", min_value=0.0, max_value=1.0, value=0.05,
                                               step=0.01)
                fade_in_out_button = st.button("Fade In/Out anwenden")

            # --- Normalisieren ---
            with st.sidebar.expander("Normalisieren", expanded=False):
                st.subheader("Audio normalisieren")
                normalize_button = st.button("Normalisieren")

            # --- Verarbeitungslogik (Buttons) ---
            if reduce_noise_button:
                with st.spinner("Rauschreduktion wird angewendet..."):
                    y_reduced = rauschreduktion_audio_datei_streamlit(y, sr, algorithmus=algorithmus_wahl,
                                                                     rauschtyp=rauschtyp_wahl)
                    st.session_state['processed_audio'] = y_reduced
                    st.session_state['processed_sr'] = sr
                    st.success("Rauschreduktion abgeschlossen!")

            if trim_button:
                with st.spinner("Audio wird zugeschnitten..."):
                    if 'processed_audio' in st.session_state:
                        y_to_trim = st.session_state['processed_audio']
                    else:
                        y_to_trim = y
                    y_trimmed = trim_audio(y_to_trim, sr, start_time, end_time)
                    st.session_state['processed_audio'] = y_trimmed
                    st.session_state['processed_sr'] = sr
                    st.success("Audio zugeschnitten!")

            if adjust_volume_button:
                with st.spinner("Lautstärke wird angepasst..."):
                    if 'processed_audio' in st.session_state:
                        y_to_adjust = st.session_state['processed_audio']
                    else:
                        y_to_adjust = y
                    y_adjusted = adjust_volume(y_to_adjust, volume_factor)
                    st.session_state['processed_audio'] = y_adjusted
                    st.session_state['processed_sr'] = sr
                    st.success("Lautstärke angepasst!")

            if adjust_speed_button:
                with st.spinner("Geschwindigkeit wird angepasst..."):
                    if 'processed_audio' in st.session_state:
                        y_to_adjust = st.session_state['processed_audio']
                    else:
                        y_to_adjust = y
                    y_speed_adjusted = adjust_speed(y_to_adjust, speed_factor)
                    st.session_state['processed_audio'] = y_speed_adjusted
                    st.session_state['processed_sr'] = sr
                    st.success("Geschwindigkeit angepasst!")

            if adjust_pitch_button:
                with st.spinner("Tonhöhe wird angepasst..."):
                    if 'processed_audio' in st.session_state:
                        y_to_adjust = st.session_state['processed_audio']
                    else:
                        y_to_adjust = y
                    y_pitch_adjusted = adjust_pitch(y_to_adjust, sr, pitch_factor)
                    st.session_state['processed_audio'] = y_pitch_adjusted
                    st.session_state['processed_sr'] = sr
                    st.success("Tonhöhe angepasst!")

            if reverse_button:
                with st.spinner("Audio wird umgekehrt..."):
                    if 'processed_audio' in st.session_state:
                        y_to_reverse = st.session_state['processed_audio']
                    else:
                        y_to_reverse = y
                    y_reversed = reverse_audio(y_to_reverse)
                    st.session_state['processed_audio'] = y_reversed
                    st.session_state['processed_sr'] = sr
                    st.success("Audio umgekehrt!")

            if fade_in_out_button:
                with st.spinner("Fade In/Out wird angewendet..."):
                    if 'processed_audio' in st.session_state:
                        y_to_fade = st.session_state['processed_audio']
                    else:
                        y_to_fade = y
                    y_faded_in = fade_in_audio(y_to_fade, sr, fade_in_duration)
                    y_faded_in_out = fade_out_audio(y_faded_in, sr, fade_out_duration)
                    st.session_state['processed_audio'] = y_faded_in_out
                    st.session_state['processed_sr'] = sr
                    st.success("Fade In/Out angewendet!")

            if normalize_button:
                with st.spinner("Audio wird normalisiert..."):
                    if 'processed_audio' in st.session_state:
                        y_to_normalize = st.session_state['processed_audio']
                    else:
                        y_to_normalize = y
                    y_normalized = normalize_audio(y_to_normalize)
                    st.session_state['processed_audio'] = y_normalized
                    st.session_state['processed_sr'] = sr
                    st.success("Audio normalisiert!")

            if 'processed_audio' in st.session_state:
                st.subheader("Verarbeitetes Audio")
                processed_audio = np.asarray(st.session_state['processed_audio'])
                st.audio(processed_audio, format='audio/wav', sample_rate=st.session_state['processed_sr'])
                display_waveform(processed_audio, st.session_state['processed_sr'], start_time, end_time)

                st.sidebar.header("Download")
                with st.sidebar:
                    output_format_download = st.selectbox("Download Format", ["WAV"], index=0)

                    buffer = io.BytesIO()
                    sf.write(buffer, processed_audio, st.session_state['processed_sr'], format='WAV')
                    wav_data = buffer.getvalue()

                    st.download_button(
                        label="Verarbeitetes Audio herunterladen",
                        data=wav_data,
                        file_name="bearbeitetes_audio.wav",
                        mime="audio/wav"
                    )

            else:
                display_waveform(y, sr, start_time, end_time)


        except Exception as e:
            st.error(f"Fehler beim Laden oder Verarbeiten der Audio-Datei: {e}")


def video_untertitelung():
    st.header("Video mit automatischen Untertiteln")
    st.write("Erstelle Untertitel aus einer Audiodatei oder verwende eine SRT-Datei, um sie in dein Video einzubetten.")

    model_option = st.selectbox(
        "Whisper-Modell wählen:",
        ["tiny", "base", "small", "medium", "large"],
        index=3
    )
    model = whisper.load_model(model_option)

    sprache = st.selectbox(
        "Sprache des Videos wählen:",
        ["auto", "de", "en", "fr", "es", "it", "ru"],
        index=0
    )

    audio_datei = st.file_uploader("Audio-Datei hochladen (optional)", type=["mp3", "wav", "flac"], key="audio")
    srt_datei = st.file_uploader("SRT-Datei hochladen (optional)", type=["srt"], key="srt")
    video_datei = st.file_uploader("Video hochladen", type=["mp4", "mov", "avi", "mkv"], key="video")

    srt_inhalt = ""

    with tempfile.TemporaryDirectory() as tmpdir:
        if audio_datei:
            audio_path = os.path.join(tmpdir, audio_datei.name)
            with open(audio_path, "wb") as f:
                f.write(audio_datei.read())
            srt_inhalt = transkribiere_audio_zu_srt(audio_path, model, sprache if sprache != "auto" else None)

        if srt_datei:
            srt_inhalt = srt_datei.read().decode('utf-8')
            if not validate_srt(srt_inhalt):
                st.error("Fehler: Die hochgeladene SRT-Datei ist ungültig!")
                return

        if srt_inhalt:
            srt_bearbeitet = st.text_area("SRT-Inhalt bearbeiten:", srt_inhalt, height=300)

            if video_datei and st.button("Video mit Untertiteln zusammenführen"):
                video_path = os.path.join(tmpdir, video_datei.name)
                srt_path = os.path.join(tmpdir, "untertitel.srt")
                output_video_path = os.path.join(tmpdir, "video_mit_untertitel.mp4")

                with open(video_path, "wb") as f:
                    f.write(video_datei.read())

                with open(srt_path, "w", encoding="utf-8") as f:
                    f.write(srt_bearbeitet)

                with st.spinner("Video und Untertitel werden zusammengeführt..."):
                    success, error_message = merge_video_mit_srt(video_path, srt_path, output_video_path)
                    if success:
                        st.success("Video mit Untertiteln erstellt!")
                        with open(output_video_path, "rb") as final_video:
                            st.download_button(
                                label="Video mit Untertiteln herunterladen",
                                data=final_video,
                                file_name="video_mit_untertiteln.mp4",
                                mime="video/mp4"
                            )
                    else:
                        st.error(f"Fehler beim Zusammenführen:\n{error_message}")


if __name__ == '__main__':
    main()
