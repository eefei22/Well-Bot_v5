# Well-Bot_v5 - Multimodal AI Assistant

## Project Overview
A comprehensive AI assistant combining:
- Speech processing (emotion, sentiment, transcription)
- Dialogue generation with WizardLM2
- Text-to-speech capabilities
- Audio sample analysis

## Directory Structure

```
.
├── README.md
├── requirements.txt
├── data/
│   └── audio_samples/
│       ├── speech_tester.wav
│       ├── speech_tester2.wav
│       ├── speech_tester3.wav
│       └── speech_tester4.wav
├── dialogue_generator/
│   ├── response_db.py
│   └── wizardllm_handler.py
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
    └── text_to_speech.py
```

## Key Components
- **Speech Processing**: Emotion detection, sentiment analysis, and transcription
- **Dialogue System**: WizardLM2 integration with response database
- **Audio Pipeline**: End-to-end processing from speech input to generated response

---

## Setup Instructions

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

## Ollama & WizardLM2 Setup
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

## GitHub Best Practice
Do **not** upload the contents of `models/ser/` to GitHub. These files are large and should remain local. They are already ignored via `.gitignore`.

---
## Running the Speech Analysis Test
You can test speech processing using:
```
python tests/test_speech_analysis.py
```
Make sure your .wav files are in data/audio_samples/.
