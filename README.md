# Customer Analytics on Ecommerce Transaction Data

This is a full-stack data science pipeline for customer behavior analysis starting from the engineering of metrics, analyzing them and then commnicating them with the help of visuals. This work depicts the use of RFM principles to segment the customers for target marketing. It also includes the prediction of customer lifetime value (CLTV) based on the same RFM principles. Customers have different purchase thoughts. To increase their engagement with the platform there are numerous marketing strategies built and one of them is recommendation system.

## Business Problems

<li>What is the percentage change in Revenue & Sales and what is the Customer Acquisition rate over the time?
<li>Which cohort perfromed well in terms of retention, average sales and revenue? 
<li>What are the key changes in the product or features that are driving the varied cohort performances for the e-commerce business?
<li>Which customers are frequrntly purschasing and who are not? Identify the set of customers driving most of the revenue for the buniness?
<li>What personalized marketing techniques shall we use to grow sales and customer base?
<li>What is the best combination of products to recommend to the customers?
<li>How to enhance the customer experience and engagement by recommending products in a more personalized manner?
  
## Approach and Analysis

### Discovering Key Metrics
focussing to engineer the key metrics which capture the core values that our product delivers to cusomters. Figuring this out will help to do a deep dive analysis

### Conducting Cohort Analysis
Analyzing how our customers behave towards our product. Conducting cohort analysis can help us understand if the customer is retained on the platform and is using our products frequently

### Customer Segmentation
Focussed on Segmenting Customers as every customer has different needs and they have their own distinct profile. I would be segmenting customers based on RFM (Recency - Frequency - Monetary Value) using k-means clustering

### Customer Lifetime Value (CLTV) Segments Prediction
CLTV indicates the total revenue from the customer during the entire relationship. CLTV helps companies to focus on those potential customers who can bring in the more revenue in the future. I would be building a machine learning model that predicts our Customer Lifetime Value Segments based on RFM principles

### Market Basket Analysis
Market Basket Analysis is a association method used to mine data and identify the frequency with which different products are purchased together. I would be using Apriori Algorithm for recommending products to customers strategizing cross-selling

### Product Recommendation System
Built a more personalized product recommnedation system for the customers using Collaborative Filtering and deployed it on Tableau

## Technolgies Used
<li>AWS (S3, CLI, RDS)
<li>PostgreSQL (RDS DB Instance)
<li>Python
<li>Tableau
