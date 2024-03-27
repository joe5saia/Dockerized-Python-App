import requests
import argparse

# Create the parser to handle the arguments
parser = argparse.ArgumentParser(description="Process some integers.")

# Add the arguments
parser.add_argument("--first_name", type=str, required=True, help="The first name")
parser.add_argument("--last_name", type=str, required=True, help="The last name")

# This line makes the arguments available in the args variable
args = parser.parse_args()


if __name__ == "__main__":
    # Everthing in this block will be executed when the script is run
    # and only this code is run as a script and not when imported as a module
    print(f"Hello {args.first_name} {args.last_name}")

    response = requests.get("https://httpbin.org/get")

    print(response.text)
