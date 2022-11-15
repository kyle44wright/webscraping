
from urllib.request import urlopen
from bs4 import BeautifulSoup
import openpyxl as xl
from openpyxl.styles import Font





#webpage = 'https://www.boxofficemojo.com/weekend/chart/'
webpage = 'https://www.boxofficemojo.com/year/2022/'

page = urlopen(webpage)			

soup = BeautifulSoup(page, 'html.parser')

title = soup.title

print(title.text)
##
##
##
##

table_rows = soup.findAll("tr")


for row in table_rows[1:6]:
    td = row.findAll("td")
    rank = (td[0].text)
    name = (td[1].text)
    theater_num = int(td[6].text.replace(",",""))
    total_gross = (td[7].text)
    total_gross2 = int(td[7].text.replace("$","").replace(",",""))
    dist = (td[9].text)
    tgross = (total_gross2/theater_num)
    print(f"Rank: {rank}")
    print(f"Name: {name}")
    print(f"Total Gross: {total_gross}")
    print(f"Distributor: {dist}")
    print(f"Average Gross per Theater: {tgross}")
    print()
    print()
    



