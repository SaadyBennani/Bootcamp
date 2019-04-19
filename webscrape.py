from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=100007709%2050001312%2050001314%2050001315%2050001402%2050001419%2050001471%2050001561%2050001944%2050012150%204814%20601201888%20601204369%20601301599%20601296379%20601296377%2050001669%20601321570%20601321572%20601323902%20601328427%20601331000%20601331379&IsNodeId=1&cm_sp=Cat_video-Cards_1-_-Visnav-_-Gaming-Video-Cards_1'

# opening up client and reading page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, 'html.parser')

# grabs each Product
containers = page_soup.findAll('div', {'class': 'item-container'})

for container in containers:
    container.a.img['title']
