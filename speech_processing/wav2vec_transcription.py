# wav2vec_transcription.py
import torch
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

MODEL_NAME = "facebook/wav2vec2-base-960h"

class Wav2VecTranscriber:
    def __init__(self, model_name=MODEL_NAME, device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.model.to(self.device)
        self.model.eval()

    def load_audio(self, file_path):
        waveform, sample_rate = torchaudio.load(file_path)
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)
        return waveform.squeeze().numpy()

    def transcribe(self, file_path):
        audio = self.load_audio(file_path)
        inputs = self.processor(audio, sampling_rate=16000, return_tensors="pt", padding=True)
        inputs = {key: val.to(self.device) for key, val in inputs.items()}

        with torch.no_grad():
            logits = self.model(**inputs).logits
            predicted_ids = torch.argmax(logits, dim=-1)

        transcript = self.processor.decode(predicted_ids[0])
        return {
            "transcript": transcript.lower().strip(),
            "confidence": None  # Not provided by default
        }

"""
Wav2Vec2-based Speech Transcription Module

Class: Wav2VecTranscriber
- Uses Wav2Vec2 model for automatic speech recognition (ASR)
- Converts speech audio files to text transcripts

Methods:
1. __init__(model_name=MODEL_NAME, device=None)
   - Initializes processor and CTC model
   - Parameters:
     - model_name: Pretrained model identifier (default: "facebook/wav2vec2-base-960h")
     - device: PyTorch device (auto-detects CUDA/CPU if None)

2. load_audio(file_path)
   - Loads and preprocesses audio file
   - Parameters:
     - file_path: Path to audio file (.wav)
   - Returns: numpy array of normalized audio samples

3. transcribe(file_path)
   - Main transcription method
   - Parameters:
     - file_path: Path to audio file (.wav)
   - Returns dictionary with:
     - transcript: String of recognized text (lowercase, stripped)
     - confidence: None (confidence scoring not implemented)
"""
