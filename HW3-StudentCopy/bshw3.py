
# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

#Part 1: AMAZING Student(s)
import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import re
url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
def webpage(base_url):
	fout = open('output.html', 'w')
	html = urllib.request.urlopen(base_url).read()
	soup = BeautifulSoup(html, 'html.parser')
#y = soup.find_all('p') #soup holds contents

i = soup.prettify()

result = re.sub("student", "AMAZING student", i)





#Part 2: photo update
link = soup.find_all('img')

for i in link:
	href = i["src"]
	if (href) == "https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg":
		# print (href)
		i["src"] = "https://scontent.fdet1-2.fna.fbcdn.net/v/t1.0-9/1504052_952647654753348_7815196908917410115_n.jpg?oh=509d12dab7aa7f8352b70d3bebf42451&oe=58C98A2C"
		# print(a["src"])

#Part 3: Smaller photo updates
for i in link:
	href = i["src"]
	if not href.startswith("https:"):
		print("before changing",i["src"])
		i["src"] = "https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png"
		print(i["src"])

result = str(soup)



fout.write(result)

fout = open('output.html', 'w')
fout.write(result)
fout.close()



