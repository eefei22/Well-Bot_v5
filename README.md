# Well-Bot_v5 Project

## Directory Structure

```
.
├── README.md
├── requirements.txt
├── data/
│   └── audio_samples/
│       ├── speech_tester4.wav
│       ├── speech_tester.wav
│       ├── speech_tester2.wav
│       └── speech_tester3.wav
├── dialogue_generator/
├── main_controller/
├── models/
│   ├── download_models.py
│   └── ser/
│       ├── config.json
│       ├── model.safetensors
│       └── preprocessor_config.json
├── speech_processor/
│   ├── wav2vec_emotion.py
│   ├── wav2vec_sentiment.py
│   └── wav2vec_transcription.py
├── tests/
│   └── test_speech_analysis.py
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

## 🤖 Ollama & WizardLM2 Setup
This project requires Ollama for running the WizardLM2 language model locally.

### Installing Ollama (Windows)
1. Download the installer from [ollama.ai](https://ollama.ai)
2. Run the downloaded .exe file
3. Open a new terminal/PowerShell window after installation

### Pulling the WizardLM2 Model
Run this command to download the model:
```
ollama pull wizardlm2
```

Verify it works by running:
```
ollama run wizardlm2 "Hello"
```

---

## 🚫 GitHub Best Practice
Do **not** upload the contents of `models/ser/` to GitHub. These files are large and should remain local. They are already ignored via `.gitignore`.

---
## 🧪 Running the Speech Analysis Test
You can test speech processing using:
```
python tests/test_speech_analysis.py
```
Make sure your .wav files are in data/audio_samples/.
