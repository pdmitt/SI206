
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

fout = open('output.html', 'w')
base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
html = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(html, 'html.parser')
#y = soup.find_all('p') #soup holds contents

a = soup.prettify() #html_doc
a = a.replace("student", "AMAZING student")

a = a.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "missny.jpg")

a = a.replace("https://raw.githubusercontent.com/cvanlent/SI206/master/HW3-StudentCopy/media/logo.png","media/logo.png")

fout.write(a)

# fout = open('output.html', 'w')
# fout.write(result)
# fout.close()



