from flask import Flask, request, jsonify, render_template
from sentiment import SentimentAnalyzer
from mongodb import MongoDBClient
from visualization import aggregate_sentiment_data
import os

app = Flask(__name__)

# Initialize services
analyzer = SentimentAnalyzer()
db_client = MongoDBClient()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
        
    # Analyze sentiment
    result = analyzer.analyze(text)
    
    # Save to database
    if db_client.connected:
        db_client.insert_record(
            text=result['text'],
            classification=result['classification'],
            scores=result['scores']
        )
        
    return jsonify(result)

@app.route('/api/history', methods=['GET'])
def history():
    records = db_client.get_recent_records(limit=100)
    chart_data = aggregate_sentiment_data(records)
    
    return jsonify({
        "records": records,
        "chart_data": chart_data,
        "db_connected": db_client.connected
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
