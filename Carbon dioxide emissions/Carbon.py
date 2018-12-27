from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = "https://www.ucsusa.org/global-warming/science-and-impacts/science/each-countrys-share-of-co2.html#.XAsxjmgzY2w"

page = urllib.request.urlopen(urlpage)

soup = BeautifulSoup(page, "html.parser")

table = soup.find("table")

results = table.findAll("tr")

rows = []
rows.append(["Rank", "Country", "Total Emissions", "Per Capita"])

for result in results:
	data = result.findAll("td")
	if len(data) == 0:
		continue
	rank = data[0].getText().strip()
	country = data[1].getText().strip()
	carbon = data[2].getText().strip()
	perCapita = data[3].getText().strip()
	rows.append([rank, country, carbon, perCapita])

print(rows)

with open("carbonemissions.csv", "w", newline="") as f_output:
	csv_output = csv.writer(f_output)
	csv_output.writerows(rows)