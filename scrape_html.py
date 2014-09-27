from bs4 import BeautifulSoup
import sys
import urlparse

with open(sys.argv[1], 'r') as originalhtml:
	soup = BeautifulSoup(originalhtml.read())
f = open('names.txt', 'r')
names = f.readlines()

def get_image (name):
	img = soup.find('img', title=name)
	if img != None:
		return urlparse.urljoin("http://princeton.edu", img.get('src'))
	else: 
		print 'Error with: ' + name

# print (get_image("Utsarga Sikder"))
# print (get_image("Junya Takahashi"))

allnames = []
allimages = []
for name in names:
	s = name.partition(',')
	# Put in format: First Last
	fullname = str(s[2][1:].rstrip('\n') + ' ' + s[0])
	allnames.append((fullname, get_image(fullname)))

for entry in allnames:
	print entry