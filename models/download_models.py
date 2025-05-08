#import sys
#print("Python executable:", sys.executable)

from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2FeatureExtractor

MODEL_NAME = "superb/wav2vec2-base-superb-er"
SAVE_PATH = "./models/ser/"

# Download from Hugging Face
model = Wav2Vec2ForSequenceClassification.from_pretrained(MODEL_NAME)
extractor = Wav2Vec2FeatureExtractor.from_pretrained(MODEL_NAME)

# Save to local directory
model.save_pretrained(SAVE_PATH)
extractor.save_pretrained(SAVE_PATH)

print(f"Model and feature extractor saved to {SAVE_PATH}")

# Save once from Hugging Face (optional if already done)
# model = Wav2Vec2ForSequenceClassification.from_pretrained("superb/wav2vec2-base-superb-er")
# extractor = Wav2Vec2FeatureExtractor.from_pretrained("superb/wav2vec2-base-superb-er")
# model.save_pretrained("./models/ser/")
# extractor.save_pretrained("./models/ser/")