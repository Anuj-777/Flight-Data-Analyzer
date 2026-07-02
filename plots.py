import matplotlib.pyplot as plt



def plot_altitude(data):
    plt.figure(figsize=(8,5))

    plt.plot(
    data["Time (s)"],
    data["Altitude (m)"],
    linewidth=2,
    label="Altitude"
)

    plt.title("Altitude vs Time")

    plt.xlabel("Time (s)")
    plt.ylabel("Altitude (m)")

    plt.grid(True)

    plt.legend()

    plt.tight_layout()

    plt.savefig("screenshots/altitude_vs_time.png")

    plt.show()

def plot_velocity(data):
    plt.figure(figsize=(8,5))

    plt.plot(
        data["Time (s)"],
        data["Velocity (m/s)"],
        linewidth=2, label="Velocity"
    )

    plt.title("Velocity vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.grid(True)
    plt.legend()
    plt.savefig("screenshots/velocity_vs_time.png")
    plt.show()

def plot_acceleration(data):
    plt.figure(figsize=(8,5))

    plt.plot(
        data["Time (s)"],
        data["Acceleration (m/s²)"],
        linewidth=2, label="Acceleration"
    )

    plt.title("Acceleration vs Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    plt.grid(True)
    plt.legend()
    plt.savefig("screenshots/acceleration_vs_time.png")

    plt.show()