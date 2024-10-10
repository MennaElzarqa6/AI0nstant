# Kaggle Project: Earthquake Prediction Using Machine Learning 🌍

This project explores earthquake prediction using various Machine Learning models, including Linear Regression (LR), Random Forest (RF), and XGBoost. The focus is on predicting earthquake magnitudes and alert levels, as well as assessing the potential for tsunamis following seismic events.

## Table of Contents

1. [Introduction](#introduction)
2. [Project Objectives](#project-objectives)
3. [Dataset Overview](#dataset-overview)
4. [Key Aspects](#key-aspects)
5. [Modeling](#modeling)
6. [Conclusion](#conclusion)
7. [How to Run This Project](#how-to-run-this-project)

---

## Introduction

Earthquakes pose significant risks to life and property. Accurate predictions can help in formulating early warning systems and disaster preparedness plans. This project aims to utilize machine learning techniques to predict earthquake magnitudes and classify potential earthquake impacts.

## Project Objectives

The primary goals of this project are:

1. **Regression**: Predicting earthquake magnitudes based on historical data.
2. **Classification**: Predicting earthquake alert levels (e.g., orange, yellow, etc.).
3. **Classification**: Assessing the likelihood of a tsunami triggered by an earthquake.

## Dataset Overview

The dataset includes historical earthquake data with features such as:

- `depth`: Depth of the earthquake in kilometers.
- `magnitude`: Magnitude of the earthquake.
- `location`: Geographical location of the earthquake.
- `date`: Date of the earthquake event.
- `latitude`: Latitude of the earthquake location.
- `longitude`: Longitude of the earthquake location.
- `tsunami`: Indicator of whether a tsunami was triggered.

## Key Aspects

### 🔍 Feature Engineering
Incorporated key earthquake characteristics like depth, location, and magnitude to improve model performance.

### 📊 Class Balancing
Applied Synthetic Minority Over-sampling Technique (SMOTE) to balance the classification dataset for better prediction accuracy in alert levels and tsunami occurrence.

### ⚙️ Modeling
- **Linear Regression (LR)**: For predicting earthquake magnitudes.
- **Random Forest (RF)**: Used for both regression and classification tasks.
- **XGBoost**: Delivered strong results, particularly in handling non-linear relationships and providing robust predictions for both regression and classification tasks.

## Conclusion

This project showcases the power of machine learning in predicting natural disasters, enhancing early warning systems, and reducing risks. The findings can contribute to improving disaster response strategies and public safety measures.

---

## How to Run This Project

1. Clone the repository:
   ```bash
   git clone https://github.com/MennaElzarqa6/AI0nstant.git
   ```
2. Navigate to the project directory
3. Install the necessary libraries
4. Open the Jupyter Notebook in your preferred environment.
5. Follow the instructions within the notebook to explore the analysis and visualizations.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.


