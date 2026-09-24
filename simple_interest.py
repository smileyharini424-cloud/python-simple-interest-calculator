principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100
amount = principal + simple_interest

print("Simple Interest:", simple_interest)
print("Total Amount:", amount)
