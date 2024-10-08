from textblob import TextBlob

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Analyze sentiment
    sentiment_polarity = blob.sentiment.polarity
    
    # Determine sentiment category based on polarity
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"


# Example text input
text = input("Enter text for sentiment analysis: ")
    
# Get sentiment
sentiment = analyze_sentiment(text)
    
# Output result
print(f"Sentiment: {sentiment}")
