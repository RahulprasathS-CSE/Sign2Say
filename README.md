# Sign2Say
A Python project using OpenCV, MediaPipe and pyttsx3 to convert hand gestures into speech

# 🖐️ Hand Gesture to Speech Converter 🔊

This project uses **OpenCV**, **MediaPipe**, and **pyttsx3** to detect hand gestures from a webcam and convert them into **spoken audio responses** using text-to-speech.

It supports **both single-hand and two-hand gestures**, making it a cool and accessible way to interpret body language into sound!

---

## 📹 Features

- ✅ Real-time hand tracking using MediaPipe
- ✋ Detects multiple gestures like:
  - Open Palm
  - Peace ✌️
  - Thumbs Up/Down
  - Call Me 🤙
  - Rock 🤘
  - Pointing 👉
  - Fist 👊
  - Two-hand gestures (e.g., both hands open)
- 🔊 Converts recognized gestures into speech using `pyttsx3`
- 🧠 Custom gesture dictionary for easy updates
- 🪄 Clean, flip-mirrored camera display

---

## 🛠️ Tech Stack

| Tool      | Usage                        |
|-----------|------------------------------|
| Python    | Programming Language         |
| OpenCV    | Real-time video processing   |
| MediaPipe | Hand tracking & landmarks    |
| pyttsx3   | Text-to-speech conversion    |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/RahulprasathS-CSE/Sign2Say.git
cd Sign2Say

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
