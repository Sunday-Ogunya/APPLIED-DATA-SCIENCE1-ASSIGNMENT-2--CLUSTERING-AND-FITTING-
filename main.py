from linear_fitting import linear_fit
from clustering import perform_clustering, create_elbow_plot
from plots import create_histogram, create_heatmap, create_scatter_plot
from data_loader import load_data

def main():
    file_path = 'student_sleep_patterns.csv' 
    data = load_data(file_path)

    if data is not None:
        create_scatter_plot(data, 'Study_Hours', 'Sleep_Quality')
        create_histogram(data, 'Sleep_Duration')

        create_heatmap(data)

        create_elbow_plot(data)

        perform_clustering(data)

        linear_fit(data)
        
    else:
        print("Failed to load data. Please check the file path.")

if __name__ == "__main__":
    main()
