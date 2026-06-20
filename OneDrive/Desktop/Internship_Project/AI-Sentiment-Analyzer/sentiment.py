from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze(self, text):
        """
        Analyzes the text and returns a dictionary with the sentiment score
        and overall classification.
        """
        scores = self.analyzer.polarity_scores(text)
        
        # Determine classification based on compound score
        compound = scores['compound']
        if compound >= 0.05:
            classification = "Positive"
        elif compound <= -0.05:
            classification = "Negative"
        else:
            classification = "Neutral"
            
        return {
            "text": text,
            "scores": scores,
            "classification": classification
        }
