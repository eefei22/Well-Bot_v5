import sys
import os

# Ensure parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from speech_processing.wav2vec_emotion import Wav2VecEmotionRecognizer
from speech_processing.wav2vec_transcription import Wav2VecTranscriber

def main():
    # Choose the file to test
    test_file = "data/audio_samples/speech_tester3.wav"
    print(f"Processing file: {test_file}")

    # Initialize modules
    recognizer = Wav2VecEmotionRecognizer()
    transcriber = Wav2VecTranscriber()

    # Emotion analysis
    emotion_result = recognizer.predict_emotion(test_file)

    # Transcription
    transcription_result = transcriber.transcribe(test_file)

    # Print results
    print("\n=== Speech Analysis ===")
    print("Transcript       :", transcription_result["transcript"])
    print("Predicted Emotion:", emotion_result["predicted_label"])
    print("Confidence       :", emotion_result["confidence"])
    print("Emotion Scores   :", emotion_result["probabilities"])

if __name__ == "__main__":
    main()
