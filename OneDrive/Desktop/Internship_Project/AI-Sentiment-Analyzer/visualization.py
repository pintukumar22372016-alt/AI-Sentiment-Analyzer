def aggregate_sentiment_data(records):
    """
    Aggregates a list of sentiment records into counts for visualization.
    Returns data formatted for Chart.js.
    """
    counts = {
        "Positive": 0,
        "Negative": 0,
        "Neutral": 0
    }
    
    for record in records:
        cls = record.get("classification")
        if cls in counts:
            counts[cls] += 1
            
    return {
        "labels": ["Positive", "Neutral", "Negative"],
        "data": [counts["Positive"], counts["Neutral"], counts["Negative"]],
        "colors": ["#10b981", "#6b7280", "#ef4444"] # Green, Gray, Red
    }
