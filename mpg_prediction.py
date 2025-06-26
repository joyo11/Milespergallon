import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pickle

# Load the Auto MPG dataset 
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']
data = pd.read_csv(url, delim_whitespace=True, header=None, names=columns)

data.replace('?', float('nan'), inplace=True)


data = data.apply(pd.to_numeric, errors='ignore')


data = data.dropna()

# The Feature and the target separation
X = data.drop(columns=['mpg', 'car_name'])
y = data['mpg']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a basic model (Linear Regression)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print the evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Saving the model locally using pickle
model_filename = "mpg_model.pkl"
with open(model_filename, 'wb') as f:
    pickle.dump(model, f)

# Loading the saved model and make prediction
with open(model_filename, 'rb') as f:
    loaded_model = pickle.load(f)

# Exampls
new_data = [[6, 160, 110, 3000, 15, 1975, 1]]  # Example data (same structure as the training data)
predicted_mpg = loaded_model.predict(new_data)
print(f'Predicted MPG for the new data: {predicted_mpg[0]}')

# Visualizing the actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted MPG")
plt.show()
