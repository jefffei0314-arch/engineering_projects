import matplotlib.pyplot as plt

import csv

filename = input("Enter CSV file name(including.csv): ")

times = []
velocities = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        time = float(row["time"])
        discharge = float(row["discharge"])
        area = float(row["area"])

        velocity = discharge / area

        times.append(time)
        velocities.append(velocity)

average_velocity = sum(velocities) / len(velocities)
peak_velocity = max(velocities)

print("Velocity Results:")
for i in range(len(times)):
    print(f"Time = {times[i]}, Velocity = {velocities[i]:.2f}")

print(f"\nAverage Velocity = {average_velocity:.2f}")
print(f"Peak Velocity = {peak_velocity:.2f}")

plt.plot(times, velocities, marker="o")

plt.xlabel("Time")
plt.ylabel("Velocity")
plt.title("Velocity vs Time")
plt.grid()

peak_index = velocities.index(max(velocities))
plt.plot(times[peak_index], velocities[peak_index], marker="o")
plt.text(times[peak_index], velocities[peak_index], f" Peak = {velocities[peak_index]:.2f}")

plt.show()
