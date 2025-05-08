import sys
import os

# Ensure parent directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from speech_processor.wav2vec_emotion import Wav2VecEmotionRecognizer
from speech_processor.wav2vec_transcription import Wav2VecTranscriber
from speech_processor.wav2vec_sentiment import Wav2VecSentimentAnalyzer

def main():
    # Choose the file to test
    test_file = "data/audio_samples/Speech Testing (a).wav"
    print(f"🎧 Processing file: {test_file}")

    # Initialize modules
    recognizer = Wav2VecEmotionRecognizer()
    transcriber = Wav2VecTranscriber()
    sentiment_analyzer = Wav2VecSentimentAnalyzer()

    # Run transcription
    transcription_result = transcriber.transcribe(test_file)
    transcript = transcription_result["transcript"]

    # Run emotion recognition
    emotion_result = recognizer.predict_emotion(test_file)

    # Run sentiment analysis on the transcript
    sentiment_result = sentiment_analyzer.analyze(transcript)

    # Print all results
    print("\n=== Speech Analysis ===")
    print("Transcript       :", transcript)
    print("Emotion          :", emotion_result["predicted_label"])
    print("Emotion Confidence:", emotion_result["confidence"])
    print("Emotion Scores   :", emotion_result["probabilities"])
    print("Sentiment        :", sentiment_result["sentiment"])
    print("Sentiment Score  :", sentiment_result["score"])

if __name__ == "__main__":
    main()
