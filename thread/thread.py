import os
import sys
import requests
from bs4 import BeautifulSoup as bs
from colorama import Fore, Back, Style
import shutil
import subprocess


print('you might grab the pics from threads\nnow i am offering that')

#TODO: multi threads at the same time
shows = input('\ngive me thread(s)\neg: b/thread/883854783\n\n--> ')
for show in shows.split():
  threads = 'https://boards.4chan.org/' + show
  if requests.get(threads).status_code != 200:
    print(Fore.RED + '\nERROR: ' + Style.RESET_ALL + 'woo bro hold up check your threads url first')
    print(Fore.RED + threads + Style.RESET_ALL)
    sys.exit(0)
  
  # if working >>>>>>
  
  # >>>>>> ask user to continue?
  result = subprocess.run(['curl', 'ip.sb'], capture_output=True, text=True)
  print(Fore.GREEN, f'\nYour IP address is {result.stdout.strip()}\ntake it eazy yo\nyou know im not watching this')
  print(Fore.YELLOW, '\nIF CONTINUE, TAKE YOUR OWN RISK, RECREATIONAL USE ONLY, TOO MUCH REQUESTS COULD GET BANNED BY 4CHAN.\nIF YOU ARE NOT SURE EXIT NOW. (CTRL+C)')
  print(Fore.YELLOW, '\nPROCEED? (y/n)', Style.RESET_ALL)
  proceed = input()
  if proceed != 'y':
    sys.exit(0)
  
  r = requests.get(threads)
  html = bs(r.content, 'html.parser')
  ret = []
  for link in html.find_all('img'):
    if 'image' not in link['src']:
      ret.append('https:' + link['src'][:-5] + link['src'][-4:])
  print(Fore.GREEN, ret, Style.RESET_ALL)
  print('\n\n>>>>>> URL ALL GOOOD! <<<<<<\n\n')
  prepared_cnt = len(ret)
  
  
  # >>>>>> create folder for ???EACH??? thread
  default_name = show.split('/')[-1]
  folder_name = input(f"Enter a folder name (press ENTER to use default: {default_name}): ")
  if not folder_name:
    folder_name = default_name
  
  while os.path.exists(folder_name):
    print(Fore.RED + f"ERROR: the folder '{folder_name}' already exists. Please choose a different name or delete the existing folder.", Style.RESET_ALL)
    folder_name = input('Enter a new folder name: ')
  
  os.mkdir(folder_name)
  
  
  cnt, error_move = 0, 0
  for i in range(len(ret)):
    filename = str(ret[i].split('/')[-1])
    if os.path.isfile('%s'%filename):
      print('\n%s'%filename, 'exists! you may have downloaded this link already\n')
    else:
      r = requests.get(ret[i])
      with open('%s'%filename, 'wb') as f:
        for image_link in r:
          f.write(image_link)
      print(f"--> new download succeed!\n[No.{cnt}] *filename:", filename, "\n*filesize:", int(os.stat(filename).st_size)/1000000, "MB", "\n")
      cnt+=1
  
      # move to ?each folder
      try:
        shutil.move(filename, folder_name)
      except:
        error_move += 1
        print(colored('Something went wrong while moving files', red))
  
  
  if prepared_cnt == cnt:
    print(Fore.GREEN, f'\n*** ALL {cnt} PHOTOS DOWNLOADED! ***\n')
  else:
    print(Fore.GREEN, f'\n*** {cnt} photos downloaded! ***\n', Fore.RED, f'but {prepared_cnt-cnt} photos could not be downloaded\n', Style.RESET_ALL)
  
  size = subprocess.run(['du', '-hs', folder_name], capture_output=True, text=True)
  print(size.stdout.split('\n')[0])
  
  if error_move:
    print(Fore.RED, f'but {error_move} photos could not be moved to some folder\n', Style.RESET_ALL)
  print("thread finished\n--------------------\n')
