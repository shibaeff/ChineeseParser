from bs4 import BeautifulSoup
from requests import *
import csv

def read_links_list(file):
    with open(file) as f:
        return f.readlines()

def get_entry(link):
    try:
        c = get(link, timeout=120).content
        soup = BeautifulSoup(c)
        phone_way = soup.find_all("div", "phone-way")[0]
        phone, name = phone_way.p.getText().split()
        return name, phone
    except:
        print("The link us %s" % link)
    # soup = BeautifulSoup(phone_way)
    # raw = soup.find_all("p")
    # print(raw)

def get_sector(link):
    return link.split('/')[-2]

def write_entry_db_name():
    pass

def get_prov(link):
    return link.split('/')[2].split('.')[0]

if __name__ == "__main__":
    links = read_links_list('links.txt')
    print("Got links")
    links = list(set(links))
    with open('base.csv', mode='a') as employee_file:
        untermensch = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for link in links:
            try:
                if link is not None:
                    name, phone = get_entry(link)
                    province, industry = get_prov(link), get_sector(link)
                    print(name, phone, industry)
                    untermensch.writerow([name, phone, province, industry])
            except:
                continue
            


        