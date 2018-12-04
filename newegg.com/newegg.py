from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&N=-1&isNodeId=1"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container "})


#container = containers[0]

filename = "graphicscard_2.csv"
f = open(filename, "w")

headers = "Brand, Product Description, Price\n"

f.write(headers)
#open()

for container in containers:
    item_info = container.find("div", {"class":"item-info"})
    brand = item_info.div.a.img["title"]
    
    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text
    
    price = container.findAll("li", {"class":"price-current"})
    strip_price = price[0].text.strip()
    strip_price2 = strip_price[0:-14]
    final_price = strip_price2.replace("|", "").replace("\n","")

    print("brand: " + brand)
    print("product_name: "+ product_name)
    print("final_price" + final_price)

    f.write(brand + "," + product_name.replace(",", "|") + "," + final_price + "\n")

f.close()