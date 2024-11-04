import pandas as pd
import matplotlib.pyplot as plt

def plot_column_data(file_path, column_name):
    try:
        df = pd.read_csv(file_path)
        df[column_name].value_counts().plot(kind='bar')
        plt.title(f"Distribution of {column_name}")
        plt.xlabel(column_name)
        plt.ylabel("Frequency")
        plt.show()
    except FileNotFoundError:
        print("File not found.")
    except KeyError:
        print(f"Column '{column_name}' does not exist in the data.")

# usage
file_path = "data_output.csv"
column_name = "Category"
plot_column_data(file_path, column_name)
