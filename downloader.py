import requests as req
import os
from pathlib import Path
from urllib.parse import urlparse

class downloader:
    def getUrl():
        urlList = []
        url = 'filler'
        while url != '':
            url = input("Input a URL: ")
            if url != '':
                urlList.append(url)
        return urlList

    def downFile(urlList):
        print('There are: ' + str(len(urlList)) + ' files to be downloaded....')
        for url in urlList:
            try:
                print('Starting download from: ' + url)
                res = req.get(url)
                parse = urlparse(url)
                downloadFolder = downloads_path = str(Path.home() / "Downloads")
                save = downloadFolder + '\\' + os.path.basename(parse.path)
                print('File saved to: ' + save)
                open(save, "wb").write(res.content)
            except req.exceptions.MissingSchema:
                print(url + ' was not a valid url!')
