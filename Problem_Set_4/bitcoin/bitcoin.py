import requests
import sys

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        user_input = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e72723ddb84c212ff9a1372988b356bdf2fcbd9ca6577d343c5b423bcf7634a7")
    content = response.json()

    price_string = content["data"]["priceUsd"]
    price = float(price_string)
    amount = user_input * price
    print(f"${amount:,.4f}")


except requests.RequestException:
    sys.exit("")

