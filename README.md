# Well-Bot_v5 Project

## Directory Structure

```
.
├── README.md
├── requirements.txt
├── data/
│   └── audio_samples/
│       ├── speech_tester.wav
│       ├── speech_tester2.wav
│       └── speech_tester3.wav
├── dialogue_generate/
├── main_controller/
├── models/
│   ├── download_models.py
│   └── ser/
│       ├── config.json
│       ├── model.safetensors
│       └── preprocessor_config.json
├── speech_processing/
│   ├── wav2vec_emotion.py
│   └── wav2vec_transcription.py
├── tests/
│   └── test_emotion.py
└── utilities_scripts/
```

Project Description
(Add detailed description here...)

---

## ⚙️ Setup Instructions

1. **Create and activate a virtual environment**
    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

2. **Install dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Download emotion classification model**
    This project uses a local Wav2Vec2 model for speech emotion recognition. Run the following to download it:
    ```
    python models/download_models.py
    ```

---

## 🚫 GitHub Best Practice
Do **not** upload the contents of `models/ser/` to GitHub. These files are large and should remain local. They are already ignored via `.gitignore`.

---
## 🧪 Running the Emotion Test Script
You can test speech emotion recognition using:
```
python tests/test_emotion.py
```
Make sure your .wav files are in data/audio_samples/.
