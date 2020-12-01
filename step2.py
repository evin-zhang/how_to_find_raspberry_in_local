import requests
from bs4 import BeautifulSoup

def get_company_info(mac_address):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}
    url = 'https://mac.51240.com/'+mac_address+"__mac/"
    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, "lxml")
    company_info = soup.table.table.find_all('td')
    print(company_info[3].text)


