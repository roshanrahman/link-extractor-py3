# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:26:52 2018

@author: Roshan
"""

import sys
import urllib
import re
from bs4 import BeautifulSoup

LINK_URL= "" 
RESULTS = []
URL_SOUP = ""
WRITE_FILE_NAME = ""
PRINT_ENABLED = True

def println(str):
    if(PRINT_ENABLED):
        print(str)
    return

def get_WRITE_FILE_NAME():
    file_name = input("Enter the file name where you want to store the fetched LINK_URLs: ").strip()
    if(len(file_name) == 0):
        println("You did not specify the file name. The results will be stored in LINK_URL.txt")
        return "LINK_URL.txt"
    if("." not in file_name):
        println("You didn't specify the file extension. It will be saved as a txt file.")
        file_name = file_name + ".txt"
    return file_name
    
if(len(sys.argv) == 1):
    LINK_URL = input("Enter a valid URL: ")
    WRITE_FILE_NAME = get_WRITE_FILE_NAME()
else:
    LINK_URL = sys.argv[1]
    if(len(sys.argv) == 3):
        WRITE_FILE_NAME = sys.argv[2]
    else:
        WRITE_FILE_NAME = get_WRITE_FILE_NAME()
    

extension = input("Enter the file extension the LINK_URLs must end with (ex. pdf, doc, mp3 etc): ")
extension = extension.replace(".", "")
if(len(extension) == 0):
    println("No extension specified. All LINK_URLs on the webpage will be fetched.")
regex_string = "." + extension + "$"

println("Fetching the webpage...")
try:
    URL_SOUP = urllib.request.urlopen(LINK_URL)
except:
    println("Could not fetch the webpage.")
    exit(0)

println("Parsing using BeautifulSoup...")
try:
    web_obj = BeautifulSoup(URL_SOUP, "html5lib")
    RESULTS = web_obj.findAll('a', attrs={'href': re.compile(regex_string)})
except:
    println("Could not parse the webpage.")
    exit(0)
    
if(len(RESULTS) == 0):
    println("No LINK_URLs were found.")
else:
    println("No. of LINK_URLs found: " + str(len(RESULTS)))
    sys.stdout = open(WRITE_FILE_NAME, "a+")
    for LINK_URL in RESULTS:
        println(LINK_URL.get('href'))
    sys.stdout = sys.__stdout__
    println("LINK_URLs written to file " + WRITE_FILE_NAME)
exit(0)