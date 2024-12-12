import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def linear_fit(data, filename='scatter_plot.png'):
    
    X = data[['Study_Hours']].values
    y = data['Sleep_Quality'].values

    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    plt.figure()
    plt.scatter(X, y, color='blue', label='Actual')
    plt.plot(X, y_pred, color='red', label='Fitted Line')
    plt.xlabel('Study Hours')
    plt.ylabel('Sleep Quality')
    plt.title('Linear Fit: Study Hours vs Sleep Quality')
    plt.legend()
    plt.savefig(filename)
    plt.close()
    print(f"Scatter plot saved as {filename}")
