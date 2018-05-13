# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:26:52 2018

@author: Roshan
"""

import sys
import urllib
import re
from bs4 import BeautifulSoup

link= "" 
link_list = []
web_text = ""

if(len(sys.argv) == 1):
    link = input("Enter a valid URL: ")
else:
    link = sys.argv[1]

extension = input("Enter the file extension the links must end with: ")
regex_string = "." + extension + "$"

print("Fetching the webpage...")
try:
    web_text = urllib.request.urlopen("https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md")
except:
    print("Could not fetch the webpage.")
    exit(0)

print("Parsing using BeautifulSoup...")
try:
    web_obj = BeautifulSoup(web_text, "html5lib")
    link_list = web_obj.findAll('a', attrs={'href': re.compile(regex_string)})
except:
    print("Could not parse the webpage.")
    exit(0)
    
if(len(link_list) == 0):
    print("No links were found.")
else:
    print("No. of links found: " + str(len(link_list)))
    for link in link_list:
        print(link.get('href'))
exit(0)