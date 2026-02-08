parts = input("Expression: ").strip().split()

x = float(parts[0])
y = parts[1]
z = float(parts[2])

if y == "+":
	result = x + z
elif y == "-":
	result = x - z
elif y == "*":
	result = x * z
else:
	result = x / z

print(f"{result:.1f}")
