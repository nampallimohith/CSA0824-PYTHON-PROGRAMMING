def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula: SI = P * R * T / 100
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Input: Principal amount, rate of interest, and time (in years)
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest: "))
time_in_years = float(input("Enter the time (in years): "))

# Calculate and print Simple Interest
simple_interest_result = calculate_simple_interest(principal_amount, interest_rate, time_in_years)
print(f"Simple Interest: {simple_interest_result}")
