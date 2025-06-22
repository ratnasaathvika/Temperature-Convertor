import argparse

parser = argparse.ArgumentParser(description="Temperature Converter")

parser.add_argument("--C", type=float, help="Convert °C to °F")
parser.add_argument("--F", type=float, help="Convert °F to °C")

args = parser.parse_args()

if args.C is not None:
    result = (args.C * 9/5) + 32
    print(f"{args.C}°C = {result:.2f}°F")

elif args.F is not None:
    result = (args.F - 32) * 5/9
    print(f"{args.F}°F = {result:.2f}°C")

else:
    print("Please provide --C or --F.")
