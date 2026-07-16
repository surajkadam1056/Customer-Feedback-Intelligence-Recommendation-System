from flask import Flask, request, jsonify
import pickle
import re

app = Flask(__name__)

model = pickle.load(open(r"C:\Users\User\OneDrive\Desktop\DS project 2\Model\sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open(r"C:\Users\User\OneDrive\Desktop\DS project 2\Model\vectorizer.pkl", "rb"))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def detect_issues(text):
    issues = []

    if any(word in text for word in ['late', 'delay', 'delayed', 'shipping']):
        issues.append('delivery')

    if any(word in text for word in ['bad', 'poor', 'broken', 'damaged', 'quality']):
        issues.append('quality')

    if any(word in text for word in ['refund', 'payment', 'charged', 'money']):
        issues.append('payment')

    if any(word in text for word in ['taste', 'flavor', 'smell', 'stale']):
        issues.append('product experience')

    if len(issues) == 0:
        issues.append('general')

    return issues

def recommend_action(issues):
    recommendations = []

    if 'delivery' in issues:
        recommendations.append("Improve delivery speed and logistics support")

    if 'quality' in issues:
        recommendations.append("Improve product quality and packaging checks")

    if 'payment' in issues:
        recommendations.append("Improve payment and refund support process")

    if 'product experience' in issues:
        recommendations.append("Improve product freshness, taste, and customer experience")

    if 'general' in issues:
        recommendations.append("Review customer feedback manually")

    return recommendations

#FINAL SENTIMENT FUNCTION
negative_words = [
    'bad', 'poor', 'late', 'delay', 'delayed',
    'broken', 'damaged', 'refund', 'worst',
    'terrible', 'awful', 'not good', 'disappointed',
    'waste', 'stale', 'expired', 'slow', 'missing'
]

positive_words = [
    'good', 'great', 'excellent', 'amazing',
    'fast', 'best', 'happy', 'satisfied',
    'fresh', 'perfect', 'love'
]

def final_sentiment_prediction(review):

    cleaned = clean_text(review)

    vector = vectorizer.transform([cleaned])

    ml_sentiment = model.predict(vector)[0]

    negative_count = sum(
        1 for word in negative_words if word in cleaned
    )

    positive_count = sum(
        1 for word in positive_words if word in cleaned
    )

    if negative_count > positive_count:
        final_sentiment = "Negative"

    elif positive_count > negative_count:
        final_sentiment = "Positive"

    else:
        final_sentiment = ml_sentiment

    issues = detect_issues(cleaned)

    recommendations = recommend_action(issues)

    return final_sentiment, issues, recommendations

@app.route('/')
def home():
    return "Customer Feedback Intelligence API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    review = data['review']

    cleaned_review = clean_text(review)

    review_vector = vectorizer.transform([cleaned_review])

    sentiment = model.predict(review_vector)[0]

    issues = detect_issues(cleaned_review)

    recommendations = recommend_action(issues)

    return jsonify({
        "review": review,
        "sentiment": sentiment,
        "issues": issues,
        "recommendations": recommendations
    })

if __name__ == '__main__':
    app.run(debug=True)