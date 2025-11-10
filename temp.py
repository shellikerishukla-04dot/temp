import sys

# If user provides temperature input
if len(sys.argv) == 2:
    try:
        temp = float(sys.argv[1])
    except ValueError:
        print("Invalid input provided. Please provide a numeric temperature.")
        sys.exit(1)
else:
    # Default temperature if no input is given
    print("No input provided. Using default temperature: 25.0°C")
    temp = 25.0

# Define the thresholds
if temp < 15.0:
    condition = "Cold"
elif temp <= 30.0:
    condition = "Normal"
else:
    condition = "Hot"

# Display results
print("Temperature:", temp)
print("Condition:", condition)
