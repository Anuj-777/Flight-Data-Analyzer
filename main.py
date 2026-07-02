from analyzer import load_flight_data, calculate_statistics
from plots import plot_altitude, plot_velocity, plot_acceleration
from report import generate_report
import os

print("Current working directory:")
print(os.getcwd())
print("Files in the current directory:")
print(os.listdir())
data = load_flight_data("sample_data/flight_data.csv")

stats = calculate_statistics(data)

print("\n========== FLIGHT SUMMARY ==========\n")

for key, value in stats.items():
    print(f"{key:<35}: {value:.2f}")

print("\n====================================")
plot_altitude(data)
plot_velocity(data)
plot_acceleration(data)
generate_report(stats)