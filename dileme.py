import os
import sys
import datetime as dt
import requests as req

urlBase = 'https://assets.dilemaveche.ro/'
firstDate = dt.datetime(2020, 7, 14)

path = './'
numberOfFiles = 1

def downloadCovers(covers, path):
    date = firstDate
    for i in range(covers):
        formattedDate = date.strftime("%Y/%m/%d")
        url = urlBase + formattedDate + '/01.jpg'
        print(url)
        
        r = req.get(url, allow_redirects=True)
        filename = 'Dilema Veche ' + date.strftime("%Y %m %d") + '.jpg'
        open(path + filename, 'wb').write(r.content)
        print("Saved "  + filename)
        
        date = date + dt.timedelta(weeks=1)

def main():
    path = sys.argv[1]
    if not os.path.isdir(path): os.makedirs(path)

    numberOfFiles = sys.argv[2]
    downloadCovers(int(numberOfFiles), path)

if __name__ == '__main__':
    main()