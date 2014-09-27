from bs4 import BeautifulSoup
import sys
import urlparse

with open(sys.argv[1], 'r') as utsarga:
	uts = utsarga.read()
soup = BeautifulSoup(uts)

# print (soup.prettify())

# for img in soup.find_all('img'):
# 	print img

print urlparse.urljoin("http://princeton.edu", soup.find('img', title="Utsarga Sikder").get('src'))