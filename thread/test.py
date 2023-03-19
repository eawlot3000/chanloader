show = input('\ngive me thread(s)\neg: b/thread/883854783\n\n--> ')
single = 'https://boards.4chan.org/' + show

if 'thread' not in threads:
  print('woo bro check your threads right')
r = requests.get(threads)
html = bs(r.content, 'html.parser')
ret = []
for link in html.find_all('img'):
  if 'image' not in link['src']:
    ret.append('https:' + link['src'][:-5] + link['src'][-4:])
