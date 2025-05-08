import torch
import torchaudio
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2FeatureExtractor

MODEL_PATH = "./models/ser/" 

class Wav2VecEmotionRecognizer:
    def __init__(self, model_path=MODEL_PATH, device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_path)
        self.model = Wav2Vec2ForSequenceClassification.from_pretrained(model_path)
        self.model.to(self.device)
        self.model.eval()

        # Load label mapping from config.json (e.g. {'0': 'neu', '1': 'hap', ...})
        self.label_map = self.model.config.id2label

        # Normalize short labels to full emotion names
        self.label_normalizer = {
            "neu": "neutral",
            "hap": "happy",
            "ang": "angry",
            "sad": "sad"
        }

    def load_audio(self, file_path):
        waveform, sample_rate = torchaudio.load(file_path)
        if waveform.shape[0] > 1:
            waveform = waveform.mean(dim=0, keepdim=True)
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16000)
            waveform = resampler(waveform)
        return waveform.squeeze().numpy()

    def predict_emotion(self, file_path):
        audio = self.load_audio(file_path)
        inputs = self.feature_extractor(audio, sampling_rate=16000, return_tensors="pt", padding=True)
        inputs = {key: val.to(self.device) for key, val in inputs.items()}

        with torch.no_grad():
            logits = self.model(**inputs).logits
            probs = torch.nn.functional.softmax(logits, dim=-1).squeeze().cpu().numpy()
            assert len(probs) == len(self.label_map), "Mismatch: id2label does not match model output size."
            predicted_class_id = int(probs.argmax())

        # Build dictionary of full-label probabilities
        prob_dict = {
            self.label_normalizer[self.label_map[i]]: float(prob)
            for i, prob in enumerate(probs)
        }

        predicted_label = self.label_map[predicted_class_id]
        normalized_label = self.label_normalizer[predicted_label]

        # Optional: print
        print("🧠 Emotion Probabilities:")
        for label, score in prob_dict.items():
            print(f"  {label.capitalize():<10}: {score:.4f}")

        return {
            "predicted_label": normalized_label,
            "confidence": float(probs[predicted_class_id]),
            "probabilities": prob_dict
        }

"""
Wav2Vec2-based Speech Emotion Recognition Module

Class: Wav2VecEmotionRecognizer
- Uses Wav2Vec2 model fine-tuned for emotion classification
- Processes audio files to predict emotional state

Methods:
1. __init__(model_path=MODEL_PATH, device=None)
   - Initializes feature extractor and classification model
   - Parameters:
     - model_path: Path to pretrained model directory (default: "./models/ser/")
     - device: PyTorch device (auto-detects CUDA/CPU if None)

2. load_audio(file_path)
   - Loads and preprocesses audio file
   - Parameters:
     - file_path: Path to audio file (.wav)
   - Returns: numpy array of normalized audio samples

3. predict_emotion(file_path)
   - Main prediction method
   - Parameters:
     - file_path: Path to audio file (.wav)
   - Returns dictionary with:
     - predicted_label: String of predicted emotion
     - confidence: Prediction probability score
     - probabilities: Dict of all emotion probabilities
       (keys: "neutral", "happy", "angry", "sad")
"""
