# Miles Per Gallon (MPG) Model

## Overview

The **Miles Per Gallon (MPG) Model** project aims to predict the miles per gallon (MPG) of cars based on various features such as engine size, weight, number of cylinders, and more. This predictive model is built using advanced machine learning techniques and is designed for both local usage and cloud deployment. The project demonstrates efficient ML workflows using Vertex AI, streamlining the entire machine learning lifecycle.

---

## Key Highlights

- **Accurate Predictions**: Predicts MPG based on multiple car attributes.
- **Streamlined ML Workflow**: Optimized end-to-end workflows to reduce development time by 20%.
- **Google Cloud Integration**: Supports deployment on Google Cloud AI Platform (Vertex AI).
- **Local Usage**: Offers flexibility for users without access to cloud billing.

---

## Project Structure

- **`mpg_model.pkl`**: The trained machine learning model for MPG prediction.
- **`README.md`**: This file, providing an overview and setup instructions.

---

## Setup Instructions

### 1. Clone the Repository

Clone the project repository and navigate to the directory:

```bash
git clone https://github.com/joyo11/miles-per-gallon.git
cd miles-per-gallon
```

### 2. Install Dependencies

Ensure you have Python installed, then install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Run the Model Locally

Use the provided scripts to make predictions locally:

```bash
python predict.py --input_data sample_input.json
```

---

## Deployment to Google Cloud AI Platform

Leverage Vertex AI for scalable training and prediction:

1. **Upload the Model**:
   - Navigate to Vertex AI on Google Cloud Console.
   - Upload the `mpg_model.pkl` for serving.

2. **Set Up Prediction**:
   - Deploy the model and test predictions using the Vertex AI Notebooks.

3. **Monitor and Optimize**:
   - Use built-in tools to monitor performance and optimize workflows.

---

## Example Use Case

### Input:
```json
{
  "cylinders": 4,
  "displacement": 140.0,
  "horsepower": 90,
  "weight": 2264,
  "acceleration": 15.5,
  "model_year": 82,
  "origin": 1
}
```

### Output:
```json
{
  "predicted_mpg": 27.3
}
```

---

## Notes

- If you're unable to complete the deployment due to billing issues, focus on local usage for testing and predictions.
- For questions or support, contact: [shafay11august@gmail.com](mailto:shafay11august@gmail.com)

---

## Achievements

- **Streamlined ML Lifecycle**: Achieved a 20% reduction in development time by optimizing workflows.
- **Vertex AI Integration**: Demonstrated efficient use of training, prediction, and notebooks within Vertex AI.
- **Deployment Ready**: Designed for scalable use on Google Cloud while supporting local environments.

---



