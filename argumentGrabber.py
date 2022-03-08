import argparse
# Writed by: Sepandi
# Date: 2020-04-24
# Description: This script is used to grab the arguments from the command line.
# Usage: python3 argumentGrabber.py name
parser = argparse.ArgumentParser(description='gets username')
parser.add_argument("argName")
username = parser.parse_args()

print("Hello {}".format(username.argName))