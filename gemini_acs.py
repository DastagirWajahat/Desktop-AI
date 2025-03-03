from google.cloud import language_v1

# Replace with your project ID and location
project_id = "gen-lang-client-0278147956"
location = "us-central1"

# Create a client object
client = language_v1.LanguageServiceClient()

# Define your text input
text = "Write a poem about the ocean."

# Specify the desired analysis type (e.g., sentiment analysis, text classification)
document = language_v1.Document(
    content=text,
    type_=language_v1.Document.Type.PLAIN_TEXT,
)

# Choose the specific analysis you want (sentiment analysis in this example)
analyze_sentiment_response = client.analyze_sentiment(document=document)

# Access the results based on the chosen analysis
sentiment = analyze_sentiment_response.document_sentiment.score
magnitude = analyze_sentiment_response.document_sentiment.magnitude

print(f"Sentiment score: {sentiment}, Magnitude: {magnitude}")
