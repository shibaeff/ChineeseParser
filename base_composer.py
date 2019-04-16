from bs4 import BeautifulSoup
from requests import *
import csv


from dotenv import *
import os
from os.path import join, dirname
dotenv_path = join(dirname(__file__), './.env')
load_dotenv(dotenv_path)
LINKS_DIST=os.getenv('LINKS_DIST')
TIMEOUT=60

def read_links_list(file):
    with open(file) as f:
        return f.readlines()

def get_entry(link):
    global TIMEOUT
    try:
        c = get(link, timeout=TIMEOUT).content
        soup = BeautifulSoup(c)
        phone_way = soup.find_all("div", "phone-way")[0]
        phone, name = phone_way.p.getText().split()
        return name, phone
    except Exception as e:
        # TIMEOUT *= 2
        # if TIMEOUT > 100:
        #     TIMEOUT = 20
        print("The link us %s" % link)
        print(e)
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
    links = read_links_list(LINKS_DIST)
    print("Got links")
    links = list(set(links))
    with open('base.csv', mode='a') as employee_file:
        print("Writing to csv")
        untermensch = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for link in links:
            try:
                print("Current link is ", link)
                if link is not None:
                    name, phone = get_entry(link)
                    province, industry = get_prov(link), get_sector(link)
                    print(name, phone, industry)
                    untermensch.writerow([name, phone, province, industry])
            except:
                continue
            


        
