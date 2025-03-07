# 📖 Audio & Video Editor – Benutzerhandbuch

Dieses Handbuch beschreibt detailliert die Funktionen und Verwendungsmöglichkeiten der Anwendung zur Audiobearbeitung und Video-Untertitelung.

## 🎵 1. Audio Editor

![image](https://github.com/user-attachments/assets/68ebb482-fe75-46e8-b28e-4b0c3f443347)


Der Audio Editor ermöglicht die Bearbeitung von Audiodateien im **WAV-, MP3- und FLAC-Format**.

### 1.1. Hochladen

1. Klicken Sie auf **"Datei hochladen"** und wählen Sie eine Audiodatei von Ihrem Computer aus.
2. Nach dem Hochladen wird die **Wellenform** des Audiosignals visuell dargestellt, wodurch Sie die Struktur des Audiosignals über die Zeit hinweg analysieren können.

### 1.2. Bearbeitungsmöglichkeiten

Die Bearbeitungsfunktionen befinden sich im **linken Seitenmenü**.

#### 🔇 Rauschunterdrückung
- **Rauschtyp**: 
  - *stationär*: Gleichmäßiges Hintergrundrauschen, das sich über die gesamte Datei erstreckt (z. B. Brummen, konstantes Rauschen von Lüftern oder Stromleitungen).
  - *nicht stationär*: Variierendes Rauschen, das sich im Verlauf der Aufnahme verändert (z. B. Straßenlärm, Windgeräusche, Gespräche im Hintergrund).
- **Algorithmus**: Es stehen verschiedene Algorithmen zur Rauschreduzierung zur Verfügung. 
  - `noisereduce_basic`: Eine einfache und schnelle Methode zur Entfernung von Rauschen basierend auf spektraler Rauschmodellierung.
  - `wiener_filter`: Ein adaptiver Algorithmus, der das Signal-Rausch-Verhältnis verbessert, indem er das Spektrum gezielt filtert.
- **Rauschen reduzieren**: Wendet die gewählte Rauschreduzierungsmethode auf die Audiodatei an. Experimentieren Sie mit den Algorithmen, um das beste Ergebnis zu erzielen.

#### ✂️ Zuschneiden
- **Startzeit (relativ)**: Gibt an, ab welchem Punkt das Audio abgespielt werden soll, Werte zwischen `0.0` (Anfang) und `1.0` (Ende). Beispiel: `0.25` startet das Audio nach einem Viertel der Gesamtdauer.
- **Endzeit (relativ)**: Gibt an, wo das Audio enden soll.
- **Zuschneiden**: Entfernt die nicht gewünschten Abschnitte und schneidet das Audio auf den gewählten Bereich zu.

#### 🔊 Lautstärke
- **Faktor**: 
  - `1.0` = Original-Lautstärke
  - `< 1.0` = Lautstärke wird reduziert (z. B. `0.5` halbiert die Lautstärke)
  - `> 1.0` = Lautstärke wird erhöht (z. B. `2.0` verdoppelt die Lautstärke)
- **Lautstärke anwenden**: Wendet die Lautstärkeänderung an.

#### ⏩ Geschwindigkeit
- **Geschwindigkeitsfaktor**: 
  - `< 1.0` = Audio wird langsamer abgespielt
  - `> 1.0` = Audio wird schneller abgespielt
- **Geschwindigkeit anwenden**: Passt die Geschwindigkeit des Audiosignals an, ohne die Tonhöhe zu verändern.

#### 🎼 Tonhöhe
- **Halbtöne**: 
  - Positive Werte = Tonhöhe wird erhöht
  - Negative Werte = Tonhöhe wird gesenkt
- **Tonhöhe anwenden**: Ändert die Tonhöhe des Audios, ohne die Geschwindigkeit zu beeinflussen.

#### 🔄 Umkehren
- **Audio umkehren**: Spielt das Audiosignal rückwärts ab, um spezielle Effekte zu erzeugen.

#### 🎚️ Fade In/Out
- **Fade-In Dauer (Sek.)**: Bestimmt, wie lange das Audio beim Start langsam eingeblendet wird.
- **Fade-Out Dauer (Sek.)**: Bestimmt, wie lange das Audio zum Ende hin langsam ausgeblendet wird.
- **Fade anwenden**: Fügt die gewählten Ein- und Ausblendeffekte hinzu.

#### 🔊 Normalisieren
- **Normalisieren**: Hebt die Lautstärke auf ein einheitliches Niveau an, ohne das Signal zu verzerren oder zu übersteuern.

#### 🏛️ Echo
- **Verzögerung (Sek.)**: Die Zeitverzögerung zwischen dem Originalsignal und dem wiederholten Echo.
- **Abklingrate**: Gibt an, wie schnell das Echo im Klangraum ausklingt.
- **Echo anwenden**: Fügt den Echo-Effekt mit den gewählten Parametern hinzu.

#### 🌫️ Hall
- **Raumgröße**: Simuliert die Größe des Raums, in dem sich der Klang befindet (kleine Räume vs. große Hallen).
- **Dämpfung**: Kontrolliert, wie stark der Hall über die Zeit abnimmt.
- **Hall-Anteil**: Legt fest, wie stark der Hall dem Originalsignal beigemischt wird.
- **Hall anwenden**: Wendet den Hall-Effekt an.

#### 🎭 Stimmverzerrung
- **Tonhöhenverschiebung (stark)**: Starke Veränderung der Tonhöhe für robotische oder verfremdete Effekte.
- **Bit Depth**: Reduziert die Bit-Tiefe des Audios, um einen verzerrten digitalen Klang zu erzeugen.
- **Stimme verzerren**: Wendet die Stimmverzerrungseffekte an.

### 1.3. Download
- **Format**: Wählen Sie zwischen **WAV, MP3 oder OGG**.
- **Bitrate (MP3 & OGG)**: Bestimmen Sie die gewünschte Audioqualität (höhere Werte bieten bessere Qualität, erzeugen aber größere Dateien).
- **Download**: Speichert die bearbeitete Datei.

---

## 🎬 2. Video-Untertitelung
![image](https://github.com/user-attachments/assets/1bf8e676-7f52-4d31-84be-97eb7a53eb2f)

Dieser Modus ermöglicht das **automatische Erstellen und Einbetten von Untertiteln** in Videos mit **Whisper AI**.

### 2.1. Einstellungen

- **Whisper-Modell wählen**: 
  - `tiny`, `base`, `small`: Schnellere Verarbeitung, aber geringere Genauigkeit.
  - `medium`, `large`: Höhere Genauigkeit, aber langsamer.
- **Sprache des Videos**: Wählen Sie die Sprache des Videos oder lassen Sie die Sprache automatisch erkennen.
- **Audio-Datei hochladen (optional)**: Falls das Video keine Audiospur enthält oder eine separate Transkription gewünscht ist.
- **SRT-Datei hochladen (optional)**: Falls bereits Untertitel vorliegen, können diese importiert und bearbeitet werden.
- **Video hochladen**: Unterstützte Formate: **MP4, MOV, AVI, MKV**.
- **Video Bitrate**: Steuerung der Ausgabequalität des Videos.
- **Video Auflösung**: Wählen Sie die gewünschte Ausgabegröße.
- **Video Framerate**: Legen Sie die Anzahl der Bilder pro Sekunde fest.

### 2.2. SRT-Bearbeitung

Falls eine Audiodatei hochgeladen oder eine SRT-Datei vorhanden ist, wird der **SRT-Text** angezeigt. Dieser kann bearbeitet werden, um Fehler zu korrigieren oder den Inhalt anzupassen.

### 2.3. Zusammenführen

- **Video mit Untertiteln zusammenführen**: Fügt die Untertitel dauerhaft ins Video ein.
- **Download**: Speichert das fertige Video mit eingebetteten Untertiteln.

---

📌 **Hinweis**: Die Verarbeitung kann je nach **Dateigröße und Einstellungen** einige Zeit in Anspruch nehmen. 

🚀 Viel Erfolg mit dem **Audio & Video Editor**!
