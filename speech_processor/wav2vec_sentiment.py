# wav2vec_sentiment.py

from transformers import pipeline

class Wav2VecSentimentAnalyzer:
    def __init__(self, model_name="distilbert-base-uncased-finetuned-sst-2-english"):
        self.analyzer = pipeline("sentiment-analysis", model=model_name)

    def analyze(self, text):
        if not text or not text.strip():
            return {
                "sentiment": "neutral",
                "score": 0.0
            }

        result = self.analyzer(text)[0]
        return {
            "sentiment": result["label"].lower(), 
            "score": float(result["score"])
        }

"""
Wav2VecSentimentAnalyzer - A sentiment analysis class using HuggingFace's transformers.

Class Methods:
__init__(model_name="distilbert-base-uncased-finetuned-sst-2-english")
    - Initializes the sentiment analyzer with specified model.
    - Parameters:
        - model_name (str): Name of pre-trained HuggingFace model to use.
                            Defaults to distilbert-base-uncased-finetuned-sst-2-english.

analyze(text)
    Analyzes sentiment of input text.
    Parameters:
        text (str): Input text to analyze sentiment for.
    Returns:
        dict: Contains sentiment analysis results with keys:
            - sentiment (str): 'positive', 'negative', or 'neutral'
            - score (float): Confidence score between 0.0 and 1.0
Notes:
    - Returns neutral with score 0.0 for empty/whitespace-only input
    - Converts sentiment labels to lowercase
"""