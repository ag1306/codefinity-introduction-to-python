prices = [29.99, 45.50, 12.75, 38.20]
disc=[0.1,0.2,0.15,0.05]
for i in range(len(prices)):
	prices[i]-=prices[i]*disc[i]
	print(f"Updated price for item {i}: is $ {prices[i]:.2f}")