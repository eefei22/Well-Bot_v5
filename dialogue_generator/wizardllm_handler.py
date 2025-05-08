# wizardllm_handler.py

import requests
from dialogue_generator.response_db import fallback_responses

class WizardDialogueEngine:
    def __init__(self, model="wizardlm", endpoint="http://localhost:11434/api/generate"):
        self.model = model
        self.endpoint = endpoint
        self.available = self.check_ollama()

    def check_ollama(self):
        try:
            res = requests.get("http://localhost:11434/api/tags", timeout=2)
            return res.status_code == 200
        except requests.RequestException:
            return False

    def build_prompt(self, transcript, emotion, sentiment):
        return f"""You are a friendly and supportive AI that helps users with their emotional well-being.

Context:
- Transcript: "{transcript}"
- Detected Emotion: {emotion}
- Sentiment Tone: {sentiment}

Based on this, provide an empathetic and thoughtful response to support the user. Response should not exceed 200 words.
Make sure to acknowledge the user's feelings and the situation.
"""

    def fallback_response(self, emotion, sentiment):
        key = (emotion.lower(), sentiment.lower())
        return fallback_responses.get(
            key,
            "I'm here for you. You can talk to me about anything or we can just take a moment together in silence."
        )

    def generate_response(self, transcript, emotion, sentiment):
        if not self.available:
            return self.fallback_response(emotion, sentiment)

        prompt = self.build_prompt(transcript, emotion, sentiment)
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(self.endpoint, json=payload, timeout=10)
            response.raise_for_status()
            result = response.json()
            return result.get("response", "").strip()

        except (requests.RequestException, ValueError) as e:
            # Fallback if POST fails or response is invalid
            return self.fallback_response(emotion, sentiment)

