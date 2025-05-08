import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from speech_processing.wav2vec_emotion import Wav2VecEmotionRecognizer

if __name__ == "__main__":
    recognizer = Wav2VecEmotionRecognizer()
    test_file = "data/audio_samples/speech_tester3.wav" 
    emotion = recognizer.predict_emotion(test_file)
    print("Predicted Emotion:", emotion)
