from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

price=[]#store price of product
availability=[]#store availability of product
driver.get("https:/www.takealot.com/russell-hobbs-2200w-crease-control-iron/PLID34147865")

content=driver.page_source
soup=BeautifulSoup(content)
for a in soup.findAll('a',href=True, attrs={'class':'pdp-core-module_actions_mdYzm'})
price=a.find('div', attrs={'class':'buybox-module_price_2YUFa'})
availability=a.find('div', attrs={'class':'cell shrink stock-availability-status'})
price.append(price.text)
availability.append(availability.text)

python.section.py
