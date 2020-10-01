import os
import sys
import datetime
import requests
import urllib.request
import shutil

from bs4 import BeautifulSoup

urlBase = 'https://dilemaveche.ro/galerie/coperta-saptamanii?image='

def downloadCovers(covers, path):
    for i in range(covers):
        index = i + 1
        url = urlBase + str(index)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")
        aas = soup.find_all("figure", class_='foto-large')

        image_info = []
        for a in aas:
            image_tag = a.findChildren("img")
            image_info.append(image_tag[0]["src"])

        r = requests.get(image_info[0], allow_redirects=True)
        filename = "Dilema Veche " + str(index) + ".jpg"
        open(path + filename, 'wb').write(r.content)
        print("Saved " + filename)
    print ("Finished " + covers + " items.")

def main():
    path = sys.argv[1]
    if not os.path.isdir(path): os.makedirs(path)

    numberOfFiles = sys.argv[2]
    downloadCovers(int(numberOfFiles), path)

if __name__ == '__main__':
    main()