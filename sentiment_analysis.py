import runpod
from transformers import pipeline

# Function to load the sentiment analysis model
def load_model():
    return pipeline("sentiment-analysis", model="black-forest-labs/FLUX.1-dev")

# Main handler for sentiment analysis requests
def sentiment_analysis_handler(event):
    global model  # global is used here to retain model instance across invocations

    # Ensure the model is loaded only once
    if 'model' not in globals():
        model = load_model()

    # Extract input text from the event
    text = event.get("input", {}).get("text")

    # Validate input
    if not text or not isinstance(text, str):
        return {"error": "Invalid input: Text must be a non-empty string."}

    # Perform sentiment analysis
    try:
        result = model(text)[0]
        return {"sentiment": result["label"], "score": float(result["score"])}
    except Exception as e:
        return {"error": f"Error during sentiment analysis: {str(e)}"}

# Start the serverless function with the handler
runpod.serverless.start({"handler": sentiment_analysis_handler})
