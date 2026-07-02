import os

def generate_report(stats):

    os.makedirs("reports", exist_ok=True)

    with open("reports/flight_report.txt", "w") as report:

        report.write("="*45 + "\n")
        report.write("      FLIGHT DATA ANALYZER REPORT\n")
        report.write("="*45 + "\n\n")

        for key, value in stats.items():
            report.write(f"{key:<35}: {value:.2f}\n")

        report.write("\n")
        report.write("="*45)

    print("Report saved successfully.")