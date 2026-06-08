# Blood Donation Forecast

## Project Overview

This project uses Machine Learning to predict whether a blood donor is likely to donate blood again in the future. The prediction is based on the donor's previous donation history.

The model is trained using historical blood donation records and helps healthcare organizations identify potential future donors.

---

## Problem Statement

Predict whether a donor will donate blood in the future using historical donation data.

---

## Dataset Information

The dataset contains the following features:

| Feature | Description |
|----------|-------------|
| Recency | Months since the last donation |
| Frequency | Total number of donations made |
| Monetary | Total blood donated (c.c.) |
| Time | Months since first donation |
| whether he/she donated blood in March 2007 | Target variable |

Target Values:

- 1 = Donated blood
- 0 = Did not donate blood

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Google Colab

---

## Machine Learning Algorithm

Random Forest Classifier

Why Random Forest?

- Easy to implement
- Good prediction accuracy
- Handles tabular data effectively

---

## Project Workflow

1. Load Dataset
2. Explore Dataset
3. Separate Features and Target
4. Split Data into Training and Testing Sets
5. Train Random Forest Model
6. Make Predictions
7. Evaluate Accuracy
8. Predict Future Donations

---

## Evaluation Metrics

- Accuracy Score
- Precision
- Recall
- F1-Score

---

## Results

The model successfully predicts the likelihood of future blood donations based on donor history.

---

## Future Improvements

- Use larger datasets
- Compare multiple algorithms
- Deploy as a web application
- Create a donor recommendation system

---

## Author

Syed Basha Shaik
