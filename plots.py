# import matplotlib.pyplot as plt
# import seaborn as sns

# def create_histogram(data, column, filename='histogram.png'):
    
#     plt.figure()
#     plt.hist(data[column], bins=10, color='blue', edgecolor='black')
#     plt.title(f'Histogram of {column}')
#     plt.xlabel(column)
#     plt.ylabel('Frequency')
#     plt.savefig(filename)
#     plt.close()
#     print(f"Histogram saved as {filename}")
    
# import seaborn as sns

# def create_heatmap(data, filename='heatmap.png'):
    
#     numeric_data = data.select_dtypes(include=[float, int])
    
#     correlation_matrix = numeric_data.corr()

#     plt.figure(figsize=(10, 8))
#     sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
#     plt.title('Correlation Heatmap')
#     plt.savefig(filename)
#     plt.close()
#     print(f"Heatmap saved as {filename}")

import matplotlib.pyplot as plt
import seaborn as sns

def create_histogram(data, column, filename='histogram.png'):
    """
    Creates a histogram of the specified column in the dataset.

    Parameters:
    data (DataFrame): The dataset
    column (str): Column to plot
    filename (str): Name of the file to save the plot
    """
    plt.figure()
    plt.hist(data[column], bins=10, color='blue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.savefig(filename)
    plt.close()
    print(f"Histogram saved as {filename}")

def create_heatmap(data, filename='heatmap.png'):
    """
    Creates a heatmap of correlations in the dataset.

    Parameters:
    data (DataFrame): The dataset
    filename (str): Name of the file to save the plot
    """
    numeric_data = data.select_dtypes(include=[float, int])
    correlation_matrix = numeric_data.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)
    plt.title('Correlation Heatmap')
    plt.savefig(filename)
    plt.close()
    print(f"Heatmap saved as {filename}")

def create_scatter_plot(data, x_column, y_column, filename='scatter_plot.png'):
    """
    Creates a scatter plot between two columns in the dataset.

    Parameters:
    data (DataFrame): The dataset
    x_column (str): Column for the x-axis
    y_column (str): Column for the y-axis
    filename (str): Name of the file to save the plot
    """
    plt.figure()
    plt.scatter(data[x_column], data[y_column], color='blue', edgecolor='black', alpha=0.7)
    plt.title(f'Scatter Plot: {x_column} vs {y_column}')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.savefig(filename)
    plt.close()
    print(f"Scatter plot saved as {filename}")

