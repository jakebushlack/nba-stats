from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from NBA_Player import Player
import csv
import io


def scrape(url):
    uClient = uReq(url)
    html = uClient.read() # STORE HTML DATA FROM WEBPAGE TO A VARIABLE
    uClient.close()
    page_soup = soup(html, "html.parser")
    html_table = page_soup.select_one("sortable stats_table now_sortable")
    headers = [th.text.encode("utf-8") for th in page_soup.select("tr th")] # FIND HEADERS AND ENCODE
    with open(url[54:-5], "w") as f:
        wr = csv.writer(f)
        wr.writerow(headers)
        # FIND DATA AND ENCODE
        wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in page_soup.select("tr + tr")])


def pull(url):
    try:
        with open(url[54:-5], 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if len(line) > 29:
                    del line[29:]
                if line:
                    for stats in line:
                        print(stats)
    except OSError:
        print(OSError)

