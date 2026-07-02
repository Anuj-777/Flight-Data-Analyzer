import pandas as pd


def load_flight_data(file_path):
    data = pd.read_csv(file_path)
    return data


def calculate_statistics(data):
    stats = {
        "Maximum Altitude (m)": data["Altitude (m)"].max(),
        "Maximum Velocity (m/s)": data["Velocity (m/s)"].max(),
        "Maximum Acceleration (m/s²)": data["Acceleration (m/s²)"].max(),
        "Simulation Duration (s)": data["Time (s)"].max(),

        "Minimum Altitude (m)": data["Altitude (m)"].min(),
        "Average Altitude (m)": data["Altitude (m)"].mean(),

        "Minimum Velocity (m/s)": data["Velocity (m/s)"].min(),
        "Average Velocity (m/s)": data["Velocity (m/s)"].mean(),

        "Minimum Acceleration (m/s²)": data["Acceleration (m/s²)"].min(),
        "Average Acceleration (m/s²)": data["Acceleration (m/s²)"].mean(),
    }

    return stats
