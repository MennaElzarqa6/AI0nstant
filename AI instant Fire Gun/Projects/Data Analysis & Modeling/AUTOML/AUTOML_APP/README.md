# AutoML App

## Overview

The AutoML App is a web-based application designed to streamline the machine learning workflow. Built using Streamlit and leveraging various AutoML libraries, the app allows users to easily train, evaluate, and visualize machine learning models without needing extensive programming knowledge. It supports different machine learning tasks, including regression, classification, and clustering.

## Features

- **User-Friendly Interface**: An interactive web interface for effortless model training and evaluation.
- **Multiple Model Support**: Supports various algorithms for regression, classification, and clustering.
- **Data Upload**: Users can upload datasets in CSV format for analysis.
- **Model Evaluation**: Provides comprehensive performance metrics and visualizations.
- **Model Selection**: Users can choose from a variety of AutoML libraries.

## Requirements

To run the AutoML App, ensure you have the following installed:

- Python 3.7 or later
- Streamlit
- PyCaret
- Other required libraries (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MennaElzarqa6/AI0nstan.git
   cd your-repository
```
2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
3.Install the required packages:
```bash
pip install -r requirements.txt
```
## Usage
1.Start the Streamlit app:
```bash
streamlit run app.py
```
2. Open your web browser and go to http://localhost:8501 to access the app.
3. Upload your dataset and select the desired machine learning task. Follow the prompts to train and evaluate your models.

## Project Structure
auto_ml_app/
│
├── app.py                   # Main application file
├── requirements.txt         # Python dependencies
├── icon.png                 # Application icon
├── mainpage.png                 # Application icon
├── sample_data.csv      # Example dataset for testing
└── README.md                # Project documentation

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
- Streamlit
- PyCaret
- Additional libraries as required by your app.


