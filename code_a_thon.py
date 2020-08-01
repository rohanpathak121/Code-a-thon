# importing required libraries
import os
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup

# title
width = os.get_terminal_size().columns
print("\n\n\n" +"Amazon WebScraping".center(width))


print("Enter Amazon site url without page number\n\n")

# inserting url
inp = input("https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031")
print(inp)

# if the link contains more than 1 pages we insert here
# but we hat only one page so insert 1 here
pg = input("Enter the number of pages to scrap\n\n")



for a in range(1,int(pg)+1):
	print("Acessing page " + str(a))

	temp_url = 'https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031'

	my_url = temp_url + str(a)
	req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
	page_html = urlopen(req).read()    

	page_soup = soup(page_html, "html.parser")   

	containers = page_soup.findAll("div",{"class":"s-item-container"})

	filename = "Amazon products.csv"
	f = open(filename,"a" , encoding='utf-8')   

	headers ="brand , proudct_name , retail_price , price , rating,  offer\n"
	f.write(headers)

	for container in containers:
		product_name = container.h2['data-attribute'].strip()
    	
		price_container = container.findAll("span",{"class":"a-size-base a-color-price s-price a-text-bold"})
		try:
			price = price_container[0].text.strip()
		except IndexError:
			price = 'null'

		Rating_container = container.findAll("span",{"class":"a-icon-alt"})
		try:
			rating = Rating_container[1].text.strip()
		except IndexError:
			rating = 'null'
		
		brand_container = container.findAll("span",{"class":"a-size-small a-color-secondary"})
		try:
			brand = brand_container[1].text.strip()
		except IndexError:
			brand = "null"
		
		ret_container = container.findAll("span",{"class":"a-size-small a-color-secondary a-text-strike"})
		try:
			retail_price = ret_container[0].text.strip()
		except IndexError:
			retail_price = "null"

		offer_container = container.findAll("span",{"class":"a-list-item"})
		offer = ""
		for i in range(10):
			try:
				offer = str(offer) + " " +offer_container[i].text.strip()
			except IndexError:
				break

		print("Brand         :" + brand)
		print("Product       :" + product_name + "\n")
		print("Orginal price :" + retail_price)
		print("Current price :" + price)
		print("Offer         :" + offer +"\n\n")
		   

		f.write(brand.replace(",","") + "," +product_name.replace(",","") + "," + retail_price.replace(",","") + "," + price.replace(",","") + ","+ offer.replace(",","") + "\n" )
	f.close()
	print("page " + str(a) + " finished " + "\n")