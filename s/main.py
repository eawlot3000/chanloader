import requests
from bs4 import BeautifulSoup as bs
import os

chan = 'https://boards.4chan.org/s/'
howmanypages = input('\nhow many pages do you want?\neg1: 1 (only the first page)\neg2: 10 (download all from page1 to page10)\n\n--> ')
if howmanypages == type(int):
  howmanypages = int(input())
else:
  howmanypages = 10

def main():
  r = requests.get(url)
  html = bs(r.content, 'html.parser')
  num, ret = 0, []
  for link in html.find_all('a'):
    link = link.get('href')
    if 'i.4cdn.org' in link and num%2==0:
      ret.append(link)
    num += 1
  
  for i in range(len(ret)):
    #TODO: for each page create a directory with page name to store files
    filename = str(ret[i][13:].replace('/', '_'))
    if os.path.isfile('%s'%filename):
      print('\n%s'%filename, 'exists! you may have downloaded this link already\n')
    else:
      r = requests.get(str("https:") + ret[i])
      with open('%s'%filename, 'wb') as f:
        for image_link in r:
          f.write(image_link)
      print("--> new download succeed!\n*filename:", filename, "\n*filesize:",
          int(os.stat(filename).st_size)/1000000, "MB", "\nready to download next one.\n")

if howmanypages != 1:
  for i in range(howmanypages+1):
    url = str(chan) + str(i+1)
    main()
else:
  url = str(chan)
  main()
print('*** all photos has been downloaded! ***\n')
