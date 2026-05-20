from textblob import TextBlob
def analyze_sentiment(text):
    """
    Analyze the sentiment of given text using TextBlob.
    Returns: Positive, Negative, or Neutral
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    print(f"Text: {text}")
    print(f"Polarity Score: {polarity}")
    
    if polarity > 0:
        return "Sentiment: Positive 😊"
    elif polarity < 0:
        return "Sentiment: Negative 😞"
    else:
        return "Sentiment: Neutral 😐"

Test the analyzer
if __name__ == "__main__":
    print("=== AI Sentiment Analyzer - CodTech Internship ===")
    print("Intern: Ramya Sri Pamidi | ID: CITS1340\n")
    
    # Test cases
    test1 = "I love this internship! Learning so much."
    test2 = "This project is very difficult and frustrating."
    test3 = "The weather is normal today."
    
    print(analyze_sentiment(test1))
    print("\n" + analyze_sentiment(test2))
    print("\n" + analyze_sentiment(test3)
