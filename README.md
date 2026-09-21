# 📝 Customer Feedback Intelligence & Recommendation System

An end-to-end **NLP, Machine Learning, and Business Intelligence** project that analyzes large-scale customer reviews to understand **sentiment, recurring customer issues, and product feedback**, and provides data-driven recommendations.

The system processes customer feedback using **Natural Language Processing (NLP)** and **Machine Learning**, performs analytical exploration using Python, visualizes business insights through **Power BI**, and exposes the trained model through a **Flask API** for prediction.

---

## 🎯 Project Objective

Customer reviews contain valuable information about product quality, delivery experience, payment issues, taste, and overall customer satisfaction.

The objective of this project is to transform unstructured customer reviews into meaningful and actionable insights.

The system is designed to:

* Analyze large-scale customer reviews
* Clean and preprocess review text
* Perform sentiment analysis
* Classify customer feedback
* Identify recurring customer issues
* Analyze sentiment patterns
* Generate recommendation-oriented insights
* Build an interactive Power BI dashboard
* Deploy the Machine Learning model using Flask
* Test predictions using Postman

---

# 🚀 Project Highlights

* 📦 **500K+ customer reviews**
* 📝 Natural Language Processing
* 🔤 TF-IDF text vectorization
* 🤖 Logistic Regression classification
* 📊 Approximately **90% model accuracy**
* 🔍 Customer issue detection
* 💡 Recommendation-oriented analysis
* 📈 Interactive Power BI dashboard
* 🌐 Flask REST API
* 🧪 Postman API testing
* 🐍 Python-based end-to-end pipeline

---

# 🛠️ Technologies Used

| Technology           | Purpose                                   |
| -------------------- | ----------------------------------------- |
| **Python**           | Data processing, NLP and Machine Learning |
| **Pandas**           | Data manipulation                         |
| **NumPy**            | Numerical operations                      |
| **Matplotlib**       | Data visualization                        |
| **Seaborn**          | Statistical visualization                 |
| **Scikit-learn**     | Machine Learning                          |
| **TF-IDF**           | Text feature extraction                   |
| **NLTK**             | NLP preprocessing                         |
| **Power BI**         | Business intelligence and dashboard       |
| **Flask**            | REST API deployment                       |
| **Postman**          | API testing                               |
| **Jupyter Notebook** | Data analysis and model development       |
| **GitHub**           | Version control                           |

---

# 📊 Dataset

The project uses the **Amazon Fine Food Reviews** dataset.

The dataset contains a large collection of customer reviews and ratings for food products.

### Important Information

The dataset contains review-related information such as:

```text
Product ID
User ID
Profile Name
Score
Summary
Review Text
Time
Helpfulness
```

The review text is the primary input used for NLP-based sentiment analysis.

---

# 🔄 End-to-End Project Workflow

```text
Amazon Customer Reviews
          ↓
     Data Cleaning
          ↓
   Text Preprocessing
          ↓
Exploratory Data Analysis
          ↓
   Sentiment Analysis
          ↓
   TF-IDF Vectorization
          ↓
  Machine Learning Model
          ↓
   Sentiment Prediction
          ↓
     Issue Detection
          ↓
 Recommendation Insights
          ↓
     Power BI Dashboard
          ↓
      Flask API
          ↓
      Postman Testing
```

---

# 🧹 1. Data Cleaning

The raw customer review dataset is cleaned before performing NLP and Machine Learning.

The preprocessing workflow includes:

* Handling missing values
* Removing duplicate records
* Converting text to lowercase
* Removing unnecessary characters
* Removing punctuation
* Removing unwanted spaces
* Preparing review text for NLP analysis

---

# 📝 2. NLP Text Preprocessing

Customer reviews are unstructured text, so NLP preprocessing is performed before applying Machine Learning.

### Processing Pipeline

```text
Raw Review
    ↓
Lowercase Conversion
    ↓
Remove Unwanted Characters
    ↓
Remove Punctuation
    ↓
Tokenization
    ↓
Stopword Removal
    ↓
Text Normalization
    ↓
Clean Review
```

### Example

**Original Review:**

```text
"This product was AMAZING! I really loved the taste."
```

**Processed Review:**

```text
"product amazing really loved taste"
```

---

# 🔤 3. TF-IDF Feature Extraction

Since Machine Learning models cannot directly understand raw text, **TF-IDF (Term Frequency-Inverse Document Frequency)** is used to convert review text into numerical features.

TF-IDF assigns importance to words based on how frequently they occur in a document relative to the complete collection of documents.

### Pipeline

```text
Clean Review Text
        ↓
TF-IDF Vectorizer
        ↓
Numerical Feature Matrix
        ↓
Machine Learning Model
```

The trained vectorizer is saved so that new reviews can be transformed using the same feature representation during prediction.

---

# 🤖 4. Machine Learning

The project treats sentiment analysis as a classification problem.

### Model Used

**Logistic Regression**

Logistic Regression is used to classify customer reviews based on their textual features.

Approximate model performance:

```text
Accuracy ≈ 90%
```

> Model accuracy may vary depending on the dataset version, preprocessing steps, train-test split, and model configuration.

---

# 📈 5. Model Evaluation

The trained model is evaluated using standard classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

These metrics help understand how well the model classifies customer sentiment.

---

# 😊 6. Sentiment Analysis

The trained model analyzes customer reviews and determines the sentiment associated with the feedback.

Example:

```text
Customer Review
      ↓
Text Preprocessing
      ↓
TF-IDF Transformation
      ↓
Logistic Regression
      ↓
Sentiment Prediction
```

Example:

```text
Input:
"The product was excellent and tasted great."

Output:
Positive Sentiment
```

---

# 🔍 7. Customer Issue Detection

In addition to sentiment analysis, the project identifies common categories of customer issues.

The system focuses on areas such as:

### 🚚 Delivery

Issues related to:

* Late delivery
* Damaged delivery
* Shipping problems
* Packaging during delivery

### 📦 Quality

Issues related to:

* Product quality
* Freshness
* Packaging
* Product condition

### 💳 Payment

Issues related to:

* Payment problems
* Billing
* Transaction-related feedback

### 🍽️ Taste

Issues related to:

* Taste
* Flavor
* Food quality
* Customer preferences

This helps convert unstructured customer feedback into more understandable business categories.

---

# 💡 8. Recommendation System

The analysis can be used to generate recommendation-oriented insights from customer feedback.

For example:

```text
Customer Feedback
       ↓
Sentiment Analysis
       ↓
Issue Detection
       ↓
Identify Recurring Problems
       ↓
Business Insight
       ↓
Recommendation
```

Possible recommendations include:

* Improve delivery processes
* Improve product packaging
* Address recurring quality complaints
* Investigate payment-related issues
* Improve products with repeated negative feedback
* Monitor frequently mentioned customer concerns

---

# 📊 9. Power BI Dashboard

Power BI is used to convert the processed feedback data into an interactive business intelligence dashboard.

### Dashboard KPIs

The dashboard can provide metrics such as:

* Total Reviews
* Positive Reviews
* Negative Reviews
* Sentiment Distribution
* Issue Categories
* Product Feedback
* Customer Rating Analysis

### Dashboard Analysis

The dashboard helps analyze:

* Overall customer sentiment
* Positive vs negative feedback
* Common customer issues
* Product-related complaints
* Sentiment patterns
* Review trends
* Customer feedback categories

---

# 🌐 10. Flask API

The trained sentiment model is integrated with a **Flask REST API**.

The API allows a user or external application to submit customer feedback and receive a prediction.

### API Architecture

```text
Client
  ↓
Flask API
  ↓
Input Review
  ↓
Text Preprocessing
  ↓
TF-IDF Vectorizer
  ↓
Trained ML Model
  ↓
Prediction
  ↓
JSON Response
```

---

# 🧪 11. Postman Testing

Postman is used to test the Flask API.

### Example Request

```http
POST /predict
```

Example JSON:

```json
{
    "review": "The product quality was excellent and I really enjoyed it."
}
```

### Example Response

```json
{
    "prediction": "Positive"
}
```

The exact response format depends on the Flask implementation in the application.

---

# 💾 Model Files

The project uses saved Machine Learning artifacts for prediction.

```text
sentiment_model.pkl
vectorizer.pkl
```

### `sentiment_model.pkl`

Contains the trained Machine Learning sentiment classification model.

### `vectorizer.pkl`

Contains the fitted TF-IDF vectorizer used to transform review text into numerical features.

These files allow the Flask application to perform predictions without retraining the model.

---

# 📂 Project Structure

The project is organized around the following major components:

```text
Customer-Feedback-Intelligence-Recommendation-System/
│
├── Dataset/
│
├── Notebooks/
│   ├── Data Cleaning
│   ├── EDA
│   ├── NLP
│   ├── Model Training
│   └── Analysis
│
├── Models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── Flask/
│   └── API Application
│
├── Power BI/
│   └── Dashboard
│
├── Reports/
│
├── Screenshots/
│
├── .gitignore
│
└── README.md
```

> Folder names should be updated if the actual repository structure uses different names.

---

# 🚀 How to Run the Project

## 1. Clone the Repository

```bash
git clone https://github.com/surajkadam1056/Customer-Feedback-Intelligence-Recommendation-System.git
```

Navigate to the project:

```bash
cd Customer-Feedback-Intelligence-Recommendation-System
```

---

## 2. Install Required Libraries

Install the required Python packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn nltk flask
```

If the repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## 3. Run the Flask Application

Navigate to the Flask application directory and run:

```bash
python app.py
```

The Flask server will start locally.

---

## 4. Test the API

Open Postman and send a `POST` request to the prediction endpoint.

Example:

```text
http://127.0.0.1:5000/predict
```

Send the review text in JSON format.

---

## 5. Open the Power BI Dashboard

Open the `.pbix` dashboard file.

Refresh the data if required to view the latest analysis.

---

# 📌 Key Business Insights

The project demonstrates how customer feedback can be converted into business intelligence.

It can help organizations:

* Monitor customer satisfaction
* Identify recurring complaints
* Understand product-related problems
* Detect delivery issues
* Analyze customer opinions at scale
* Identify areas requiring improvement
* Support data-driven business decisions

---

# 🎓 Skills Demonstrated

## Python

* Data manipulation
* Data cleaning
* Exploratory Data Analysis
* Visualization
* Machine Learning

## NLP

* Text preprocessing
* Tokenization
* Stopword removal
* TF-IDF
* Sentiment analysis

## Machine Learning

* Classification
* Logistic Regression
* Model evaluation
* Confusion matrix
* Model serialization

## Power BI

* Data visualization
* KPI creation
* Interactive dashboard
* Business insights

## Deployment

* Flask REST API
* Saved ML models
* API integration
* Postman testing

---

# 🔮 Future Improvements

The project can be further enhanced with:

* Sentiment probability scores
* Aspect-based sentiment analysis
* Advanced NLP models such as BERT
* Automatic topic detection
* More sophisticated recommendation logic
* Real-time customer feedback analysis
* Cloud deployment
* Automated Power BI refresh
* Customer feedback alert system
* Product-level sentiment tracking

---

# 👨‍💻 Author

## Suraj Kadam

**B.E. Electronics & Telecommunication Engineering**

### Technical Skills

```text
Python
SQL
Power BI
Excel
Machine Learning
NLP
Pandas
NumPy
Scikit-learn
Flask
Postman
GitHub
```

### Areas of Interest

* Data Analytics
* Data Science
* Machine Learning
* Natural Language Processing
* Business Intelligence

---

# ⭐ Project Summary

```text
500K+ Customer Reviews
          ↓
     NLP Processing
          ↓
    TF-IDF Features
          ↓
 Logistic Regression
          ↓
 Sentiment Analysis
          ↓
    Issue Detection
          ↓
 Recommendation Insights
          ↓
    Power BI Dashboard
          ↓
       Flask API
          ↓
   Postman Testing
```

This project demonstrates an end-to-end approach to transforming **large-scale unstructured customer feedback into sentiment insights, issue analysis, recommendations, and business intelligence**.
