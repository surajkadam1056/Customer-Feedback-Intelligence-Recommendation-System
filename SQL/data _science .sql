CREATE DATABASE review_analysis;
USE review_analysis;

CREATE TABLE reviews (
    review_id INT,
    product_id VARCHAR(50),
    rating INT,
    review_date DATE,
    summary TEXT,
    review_text TEXT,
    sentiment VARCHAR(20)
);

--check data was load 
SELECT * FROM reviews LIMIT 10;

--Total Review 
SELECT COUNT(*) FROM reviews;

--Sentiment count 
SELECT sentiment, COUNT(*) 
FROM reviews
GROUP BY sentiment;

--Average rating 
SELECT AVG(rating) FROM reviews;

--Negative reviews 
SELECT *
FROM reviews
WHERE sentiment = 'Negative';

--Top products 
SELECT product_id, COUNT(*) as total_reviews
FROM reviews
GROUP BY product_id
ORDER BY total_reviews DESC
LIMIT 10;

--low rating product
SELECT product_id, AVG(rating) as avg_rating
FROM reviews
GROUP BY product_id
HAVING avg_rating < 3;

--monthly Trend 
SELECT MONTH(review_date) as month, COUNT(*) as total
FROM reviews
GROUP BY month;

--sentiment vs rating
SELECT rating, sentiment, COUNT(*) as count
FROM reviews
GROUP BY rating, sentiment
ORDER BY rating;

--Low Rating Negative Customer Reviews
SELECT review_text 
FROM reviews
WHERE sentiment = 'Negative'
AND rating <= 2
LIMIT 20; 