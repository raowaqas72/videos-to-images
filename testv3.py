import math

# Set the rate parameter
lam = 50

# Set the number of events we're interested in
k = 60

# Calculate the probability using the Poisson distribution formula
prob = (math.exp(-lam) * lam**k) / math.factorial(k)

print(f"The probability of getting no defective bulbs in a box of 100 is {prob:.4f}")
