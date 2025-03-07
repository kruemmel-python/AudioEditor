# 🎧🎬 Audio & Video Editor

Ein vielseitiges Streamlit-basiertes Tool zur Audiobearbeitung und automatischen Video-Untertitelung.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/your-streamlit-link)  <-- *Ersetze dies durch deinen Streamlit-Link!*
[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## ✨ Funktionen

**Audio-Editor:**

* **Rauschunterdrückung:** Entferne stationäres oder nicht-stationäres Rauschen mit verschiedenen Algorithmen (noisereduce, Wiener-Filter).
* **Zuschneiden:** Schneide Audio präzise zu, indem du Start- und Endzeiten auswählst.
* **Lautstärkeanpassung:** Verändere die Lautstärke des Audios.
* **Geschwindigkeitsänderung:** Beschleunige oder verlangsame das Audio, ohne die Tonhöhe zu beeinflussen.
* **Tonhöhenänderung:** Verstelle die Tonhöhe des Audios in Halbtonschritten.
* **Umkehren:** Spiele das Audio rückwärts ab.
* **Fade In/Out:** Füge sanfte Ein- und Ausblend-Effekte hinzu.
* **Normalisieren:** Maximiere die Lautstärke, ohne Übersteuerung.
* **Wellenform-Visualisierung:** Betrachte die Wellenform des Audios.
* **Download:** Lade das bearbeitete Audio im WAV-Format herunter.

**Video-Untertitelung:**

* **Automatische Transkription:**  Generiere Untertitel aus dem Audio des Videos mithilfe von Whisper AI.
* **SRT-Unterstützung:** Lade vorhandene SRT-Dateien hoch oder bearbeite automatisch generierte Untertitel.
* **Sprache auswählen:** Wähle die Sprache des Videos für die Transkription.
* **Whisper-Modell auswählen:** Wähle zwischen verschiedenen Whisper-Modellen für die Transkription (tiny, base, small, medium, large).
* **Untertiteleinbettung:** Bette die Untertitel direkt in das Video ein.
* **Download:** Lade das Video mit eingebetteten Untertiteln im MP4-Format herunter.


## 🚀 Erste Schritte

1. **Installation:**

```bash
pip install streamlit librosa noisereduce soundfile numpy matplotlib scipy whisper ffmpeg-python
```

2. **Ausführen:**

```bash
streamlit run dein_skript.py
```

*Ersetze `dein_skript.py` durch den Namen deiner Python-Datei.*

## 🛠️ Verwendung

**Audio-Editor:**

Lade eine Audiodatei hoch und wähle die gewünschten Audiobearbeitungsfunktionen im Sidebar-Menü aus. Die Wellenform wird visualisiert und du kannst das bearbeitete Audio anhören und herunterladen.

**Video-Untertitelung:**

Lade ein Video hoch. Optional kannst du eine Audiodatei für die Transkription hochladen oder eine vorhandene SRT-Datei verwenden. Bearbeite die Untertitel nach Bedarf und binde sie in das Video ein.  Lade anschließend das Video mit den eingebetteten Untertiteln herunter.

## 💻 Technologien

* **Streamlit:** Für die interaktive Web-App.
* **Librosa:** Für Audioanalyse und -verarbeitung.
* **Noisereduce:** Für Rauschunterdrückung.
* **Soundfile:** Zum Lesen und Schreiben von Audiodateien.
* **NumPy:** Für numerische Berechnungen.
* **Matplotlib:** Für die Visualisierung der Wellenform.
* **SciPy:** Für die Signalverarbeitung (Wiener-Filter).
* **Whisper AI:** Für die automatische Spracherkennung und Transkription.
* **FFmpeg:** Zum Einbetten von Untertiteln in Videos.


## 📝 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die [LICENSE](LICENSE)-Datei für weitere Informationen.


## 🙏 Danksagung

* Den Entwicklern der verwendeten Bibliotheken.

---
