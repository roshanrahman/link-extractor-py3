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
write_file_name = "" 

def get_write_file_name():
    file_name = input("Enter the file name where you want to store the fetched links: ").strip()
    if(len(file_name) == 0):
        print("You did not specify the file name. The results will be stored in link.txt")
        return "link.txt"
    if("." not in file_name):
        print("You didn't specify the file extension. It will be saved as a txt file.")
        file_name = file_name + ".txt"
    return file_name
    
if(len(sys.argv) == 1):
    link = input("Enter a valid URL: ")
    write_file_name = get_write_file_name()
else:
    link = sys.argv[1]
    if(len(sys.argv) == 3):
        write_file_name = sys.argv[2]
    else:
        write_file_name = get_write_file_name()
    

extension = input("Enter the file extension the links must end with (ex. pdf, doc, mp3 etc): ")
extension = extension.replace(".", "")
if(len(extension) == 0):
    print("No extension specified. All links on the webpage will be fetched.")
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
    sys.stdout = open(write_file_name, "a+")
    for link in link_list:
        print(link.get('href'))
    sys.stdout = sys.__stdout__
    print("Links written to file " + write_file_name)
exit(0)