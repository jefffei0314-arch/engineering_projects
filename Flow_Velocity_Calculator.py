# Open Channel Flow Velocity Calculator using Manning Equation

print("=== Open Channel Flow Velocity Calculator ===")

try:
    n = float(input("Enter Manning roughness coefficient (n): "))
    R = float(input("Enter Hydraulic Radius (m): "))
    S = float(input("Enter Channel Slope: "))

    if n <= 0 or R <= 0 or S <= 0:
        print("\nError: All inputs must be positive numbers.")
    else:
        V = (1 / n) * (R ** (2/3)) * (S ** 0.5)
        print(f"\nFlow Velocity = {V:.3f} m/s")

except:
    print("\nInvalid input. Please enter numerical values only.")