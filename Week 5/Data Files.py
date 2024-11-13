input("Please enter a letter for a list of countries beginning with that letter:")
def requests():

import csv
import requests

url = "https://tinyurl.com/countries-css"
data = requests.get(url)
lines = data.text.splitlines()
csv_reader = csv.reader(lines)

for row in csv_reader:
    print(row)