from downloader import downloader as dwnld

print('🏁 This script will download the file from a specified url(s). 🏁')
print('👀 Please make sure you enter a valid url or else an exception will be raised. 👀')
print('⛔ Just leave the prompt blank and hit enter once you have entered all the urls. ⛔ \n \n \n')
dwnld.downFile(dwnld.getUrl())
