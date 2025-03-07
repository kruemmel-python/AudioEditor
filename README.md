# 🎧🎬 Audio & Video Editor

Ein vielseitiges, webbasiertes Tool zur Audiobearbeitung, automatischen Video-Untertitelung und kreativen Klanggestaltung, entwickelt mit Streamlit.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/audioeditor-d5vappwrtpddfj2imgxdgqk.streamlit.app)

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## ✨ Features

### 🎵 Audio Editor

*   **Rauschunterdrückung:** Entferne stationäres und nicht-stationäres Rauschen. (Noisereduce, Wiener-Filter)
*   **Präzises Zuschneiden:** Schneide Audiosignale zeitgenau zu.
*   **Lautstärkeanpassung:**  Ändere die Lautstärke präzise.
*   **Geschwindigkeitskontrolle:** Beschleunige oder verlangsame das Audio ohne Tonhöhenänderung.
*   **Tonhöhenänderung:** Transponiere die Tonhöhe in Halbtonschritten.
*   **Umkehren:** Spiele das Audio rückwärts ab.
*   **Fade In/Out:** Füge sanfte Übergänge hinzu.
*   **Normalisierung:** Maximiere die Lautstärke ohne Übersteuerung.
*   **Wellenformanalyse:** Visuelle Darstellung des Audiosignals.
*   **Audioeffekte:**
    *   **Echo:**  Mit einstellbarer Verzögerung und Abklingrate.
    *   **Hall (Reverb):** Simuliere verschiedene Raumakustiken.
    *   **Stimmverzerrung:**  Tonhöhenverschiebung, Bitcrushing.
*   **Download:** Exportiere bearbeitetes Audio in verschiedenen Formaten (WAV, MP3, OGG).


### 🎬 Video-Untertitelung

*   **Automatische Transkription:** Generiere Untertitel mit Whisper AI.
*   **SRT-Import/Export:**  Bearbeite und verwalte Untertitel.
*   **Mehrsprachige Unterstützung:**  Transkription in verschiedenen Sprachen.
*   **Modellauswahl:** Wähle zwischen verschiedenen Whisper AI-Modellen (Tiny, Base, Small, Medium, Large).
*   **Untertitelintegration:** Bette Untertitel direkt in das Video ein.
*   **Video-Download:**  Lade Videos mit eingebetteten Untertiteln herunter (MP4).


## 🚀 Erste Schritte

### 📦 Voraussetzungen

*   Python 3.8+
*   FFmpeg (siehe [FFmpeg Installation](#ffmpeg-installation))

### ⚙️ Installation

1.  Klone das Repository:

    ```bash
    git clone https://github.com/kruemmel-python/AudioEditor.git
    cd dein_repo
    ```

2.  Installiere die Abhängigkeiten:

    ```bash
    pip install -r requirements.txt
    ```

    **Erstelle eine `requirements.txt` Datei mit allen Abhängigkeiten:**

    ```
streamlit==1.32.2
librosa==0.10.1
soundfile==0.12.1
numpy==1.26.4
matplotlib==3.8.3
noisereduce==3.0.3
scipy==1.12.0
openai-whisper==20231117
setuptools==69.5.1
wheel==0.43.0
pedalboard
    ```


### ▶️ Ausführen

```bash
streamlit run dein_skript.py
```

Ersetze `dein_skript.py` durch den Namen deiner Python-Datei.


## 🛠️ Verwendung

Siehe die Dokumentation im Streamlit App für detaillierte Anleitungen.


## 💻 Technologien

*   [Streamlit](https://streamlit.io/)
*   [Librosa](https://librosa.org/doc/latest/index.html)
*   [Noisereduce](https://pypi.org/project/noisereduce/)
*   [Soundfile](https://pysoundfile.readthedocs.io/en/latest/)
*   [NumPy](https://numpy.org/)
*   [Matplotlib](https://matplotlib.org/)
*   [SciPy](https://scipy.org/)
*   [Whisper AI](https://openai.com/research/whisper)
*   [Pedalboard](https://github.com/spotify/pedalboard)
*   [FFmpeg](https://ffmpeg.org/)


## ⚙️ FFmpeg Installation

Anleitungen zur Installation von FFmpeg für verschiedene Betriebssysteme findest du [hier](https://ffmpeg.org/download.html).


## 📝 Lizenz

MIT License - siehe die [LICENSE](LICENSE) Datei für Details.


## 🙏 Danksagung

Ein großes Dankeschön an die Entwickler der oben genannten Bibliotheken und Tools sowie an die Open-Source-Community.
