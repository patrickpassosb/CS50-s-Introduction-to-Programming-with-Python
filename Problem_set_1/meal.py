def main():
	time = input("What time is it? ")
	hour = convert(time)
	if 7 <= hour <= 8:
		print("breakfast time")
	elif 12 <= hour <= 13:
		print("lunch time")
	elif 18 <= hour <= 19:
		print("dinner time")

def convert(time):
	hours, minutes = time.split(":")
	hours = float(hours)
	minutes = float(minutes)
	total = hours + minutes / 60
	return total

if __name__ == "__main__":
    main()
