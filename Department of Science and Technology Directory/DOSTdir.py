from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = "http://helpdesk.dost.gov.ph/alldirectory"

page = urllib.request.urlopen(urlpage)
soup = BeautifulSoup(page, "html.parser")


agency_items = soup.findAll("div", {"class": "agency-item"})

rows =[]
rows.append(["Name", "Web Url", "Email Address", "Address and Contact Number"])

for agency_item in agency_items:
    try:
        name = agency_item.strong.text
        weburl = agency_item.find("a",{"class":"website-link"}).get("href")
        emailadd = agency_item.find("a",{"class":"website-link"}).getText().replace(weburl, "").strip()
        add_no = agency_item.getText().replace(name, "").replace(weburl, "").replace(emailadd, "").strip()
        
    except:
        name = None
        weburl = None
        emailadd = None
        add_no = None

    rows.append([name, weburl, emailadd, add_no])

print(rows)

with open("DOSTDirectory.csv", "w", newline="") as f_output:
	csv_output = csv.writer(f_output)
	csv_output.writerows(rows)
