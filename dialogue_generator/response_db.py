# response_db.py

fallback_responses = {
    ("sad", "negative"): "I'm really sorry you're feeling this way. You’re not alone. Would you like to talk about it or do something comforting together?",
    ("sad", "neutral"): "If you're feeling a little down, that's okay. Take your time—I'm here for you.",
    ("sad", "positive"): "Even when you’re feeling okay, a hint of sadness can linger. Want to explore what’s behind that feeling?",

    ("angry", "negative"): "It’s completely valid to feel angry. Would it help to vent or maybe pause and breathe together?",
    ("angry", "neutral"): "I see you're feeling some tension. I'm here if you want to talk it out or shift your focus.",
    ("angry", "positive"): "You're holding a lot in but still seeing the positive — that’s strength. What would help most right now?",

    ("happy", "positive"): "That's fantastic to hear! Want to share what made your day better?",
    ("happy", "neutral"): "It's nice to feel content. Let’s hold onto that peace together.",
    ("happy", "negative"): "Even when things feel happy, mixed feelings can show up. Want to talk through it?",

    ("neutral", "positive"): "You seem calm and balanced — that's a good place to be.",
    ("neutral", "neutral"): "I'm here with you. Let me know how you're feeling or what’s on your mind.",
    ("neutral", "negative"): "Even a neutral tone can carry quiet heaviness. Want to check in with yourself a little deeper?",
}
