from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup


url = 'https://www.dickssportinggoods.com/f/home-gyms#bazaarRating:&facet:&productBeginIndex:0&orderBy:5&pageView:grid&minPrice:&maxPrice:&pageSize:&'

# Opening up connection, grabbing the page
uClient = uReq(url)
raw_html = uClient.read()
uClient.close()

#Responsible for parsing file
page_soup = soup(raw_html, "html.parser")

#Grabs all products on page
container = page_soup.findAll("div",{"class":"product-grid"})
