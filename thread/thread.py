import requests
from bs4 import BeautifulSoup as bs
import os
print('you might grab the pics from threads\nnow i am offering that')

#TODO: multiply threads at the same time
show = input('\ngive me thread(s)\neg: b/thread/883854783\n\n--> ')
threads = 'https://boards.4chan.org/' + show
if 'thread' not in threads:
  print('woo bro check your threads right')
print(threads)
r = requests.get(threads)
html = bs(r.content, 'html.parser')
ret = []
for link in html.find_all('img'):
  if 'image' not in link['src']:
    ret.append('https:' + link['src'][:-5] + link['src'][-4:])
print(ret)
for i in range(len(ret)):
  #TODO: for each page create a directory with page name to store files
  filename = str(ret[i][13:].replace('/', '_'))
  if os.path.isfile('%s'%filename):
    print('\n%s'%filename, 'exists! you may have downloaded this link already\n')
  else:
    r = requests.get(ret[i])
    with open('%s'%filename, 'wb') as f:
      for image_link in r:
        f.write(image_link)
    print("--> new download succeed!\n*filename:", filename, "\n*filesize:",
        int(os.stat(filename).st_size)/1000000, "MB", "\nready to download next one.\n")

print('*** all photos has been downloaded! ***\n')
