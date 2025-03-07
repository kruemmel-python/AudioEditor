# 📖 Audio & Video Editor – Benutzerhandbuch

Dieses Handbuch beschreibt detailliert die Funktionen und Verwendungsmöglichkeiten der Anwendung zur Audiobearbeitung und Video-Untertitelung.

## 🎵 1. Audio Editor

Der Audio Editor ermöglicht die Bearbeitung von Audiodateien im **WAV-, MP3- und FLAC-Format**.

### 1.1. Hochladen

1. Klicken Sie auf **"Datei hochladen"** und wählen Sie eine Audiodatei von Ihrem Computer aus.
2. Nach dem Hochladen wird die **Wellenform** des Audiosignals visuell dargestellt.

### 1.2. Bearbeitungsmöglichkeiten

Die Bearbeitungsfunktionen befinden sich im **linken Seitenmenü**.

#### 🔇 Rauschunterdrückung
- **Rauschtyp**: 
  - *stationär*: Gleichmäßiges Hintergrundrauschen (z. B. Brummen).
  - *nicht stationär*: Variierendes Rauschen (z. B. Windgeräusche).
- **Algorithmus**: Wählen Sie einen Rauschreduktionsalgorithmus (z. B. `noisereduce_basic`).
- **Rauschen reduzieren**: Startet die Rauschreduzierung.

#### ✂️ Zuschneiden
- **Startzeit (relativ)**: Wert zwischen `0.0` (Anfang) und `1.0` (Ende), z. B. `0.25` für ein Viertel der Länge.
- **Endzeit (relativ)**: Wert zwischen `0.0` und `1.0`.
- **Zuschneiden**: Entfernt unerwünschte Bereiche.

#### 🔊 Lautstärke
- **Faktor**: 
  - `1.0` = Original
  - `< 1.0` = Leiser
  - `> 1.0` = Lauter
- **Lautstärke anwenden**: Wendet die Anpassung an.

#### ⏩ Geschwindigkeit
- **Geschwindigkeitsfaktor**: 
  - `< 1.0` = Verlangsamung
  - `> 1.0` = Beschleunigung
- **Geschwindigkeit anwenden**: Ändert die Abspielgeschwindigkeit.

#### 🎼 Tonhöhe
- **Halbtöne**: 
  - Positive Werte = Höher
  - Negative Werte = Tiefer
- **Tonhöhe anwenden**: Passt die Tonhöhe an.

#### 🔄 Umkehren
- **Audio umkehren**: Spielt das Audio rückwärts ab.

#### 🎚️ Fade In/Out
- **Fade-In Dauer (Sek.)**
- **Fade-Out Dauer (Sek.)**
- **Fade anwenden**: Fügt sanfte Übergänge hinzu.

#### 🔊 Normalisieren
- **Normalisieren**: Maximiert die Lautstärke ohne Verzerrung.

#### 🏛️ Echo
- **Verzögerung (Sek.)**: Zeit zwischen Original und Echo.
- **Abklingrate**: Wie schnell das Echo abnimmt.
- **Echo anwenden**: Wendet den Effekt an.

#### 🌫️ Hall
- **Raumgröße**: Simuliert verschiedene akustische Umgebungen.
- **Dämpfung**: Steuerung des Halls.
- **Hall-Anteil**: Mischverhältnis.
- **Hall anwenden**: Wendet den Effekt an.

#### 🎭 Stimmverzerrung
- **Tonhöhenverschiebung (stark)**: Extremer Pitch-Shift.
- **Bit Depth**: Digitaler, verzerrter Klang.
- **Stimme verzerren**: Wendet die Verzerrung an.

### 1.3. Download
- **Format**: WAV, MP3, OGG
- **Bitrate** (MP3 & OGG): Höhere Werte = bessere Qualität.
- **Download**: Speichert die bearbeitete Datei.

---

## 🎬 2. Video-Untertitelung

Dieser Modus ermöglicht das **automatische Erstellen und Einbetten von Untertiteln** in Videos mit **Whisper AI**.

### 2.1. Einstellungen

- **Whisper-Modell wählen**: Kleinere Modelle (`tiny`, `base`, `small`) sind schneller, größere (`medium`, `large`) genauer.
- **Sprache des Videos**: Automatische oder manuelle Sprachauswahl.
- **Audio-Datei hochladen (optional)**: Falls das Video keine Audiospur enthält.
- **SRT-Datei hochladen (optional)**: Bereits vorhandene Untertitel importieren.
- **Video hochladen**: Unterstützte Formate: **MP4, MOV, AVI, MKV**.
- **Video Bitrate**: Höhere Werte = bessere Qualität.
- **Video Auflösung**: Anpassbare Ausgabegröße.
- **Video Framerate**: Steuerung der Bildrate.

### 2.2. SRT-Bearbeitung

Falls eine Audiodatei hochgeladen oder eine SRT-Datei vorhanden ist, wird der **SRT-Text** angezeigt. Dieser kann direkt bearbeitet werden.

### 2.3. Zusammenführen

- **Video mit Untertiteln zusammenführen**: Verknüpft Untertitel und Video.
- **Download**: Speichert das fertige Video.

---

📌 **Hinweis**: Die Verarbeitung kann je nach **Dateigröße und Einstellungen** einige Zeit in Anspruch nehmen. 

🚀 Viel Erfolg mit dem **Audio & Video Editor**!
