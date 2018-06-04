# -*- coding: utf-8 -*-
"""
Link extractor

Simple script that can fetch links that end with a specific extension, useful to fetch links to files such as mp3, pdf, etc.

@author: Roshan
"""

import sys
import urllib
import re
from bs4 import BeautifulSoup

# Determines if text will be printed on the console or not.
PRINT_ENABLED = False


def println(str):
    if(PRINT_ENABLED):
        print(str)
    return


def get_file_name():
    '''Gets a file name from the user. Requires text file format. If extension is not specified, 
    it will use txt instead. If nothing is specified, file 'results.txt' will be used instead.
    
    RETURNS: A file name with extension, of type str
    '''

    file_name = input(
        "Enter the file name where you want to store the fetched urls: ").strip()
    if(len(file_name) == 0):
        println(
            "You did not specify the file name. The results will be stored in results.txt")
        return "results.txt"
    if("." not in file_name):
        println(
            "You didn't specify the file extension. It will be saved as a txt file.")
        file_name = file_name + ".txt"
    return file_name


def get_url():
    '''Gets a valid URL from the user. Requires URL to begin with http or https. If the URL entered is invalid,
    the function recursively attempts to get a valid URL.
    
    RETURNS: A regex-matched URL, of type str
    '''
    url = input("Enter a valid URL: ")
    regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if(re.search(regex, url)):
        return url
    else:
        println("Invalid URL\n")
        return(get_url())


def get_extension():
    '''Gets a valid extension from the user. If the extension is not specified, it returns an empty string.
    Removes all dots the user may enter.
    
    RETURNS: An extension with all dots removed, of type str.
    '''
    extension = input(
        "Enter the file EXTENSION the URLs must end with (ex. pdf, doc, mp3 etc) or ignore: ")
    extension = extension.replace(".", "")
    if(len(extension) == 0):
        println("No EXTENSION specified. All URLs on the webpage will be fetched.")
    return extension


def get_all_links_by_soup(url, extension):
    '''Fetches all links from the webpage located by the URL, that end with the extension specified.
    Uses BeautifulSoup to retrieve all href links from the <a> tags in the source code. If no links
    are fetched, the returned list is empty.
    
    RETURNS: A list containing the fetched links.
    '''
    results = []
    regex_string = '(http[s]?:\/\/)?[^\s(["<,>]*\.[^\s[",><]*' + \
        '.' + extension + '$'

    println("Fetching the webpage...")
    soup = urllib.request.urlopen(url)

    println("Parsing using BeautifulSoup...")
    web_obj = BeautifulSoup(soup, "html5lib")
    web_obj = web_obj.findAll('a', attrs={'href': re.compile(regex_string)})
    for url in web_obj:
        results.append(url.get('href'))
    println("No of links found: " + str(len(results)))
    return results


def get_all_links_by_regex(url, extension):
    '''Fetches all links from the webpage located by the URL, that end with the extension specified.
    Uses Regex to retrieve all the matching links in the source code. If no links
    are fetched, the returned list is empty.
    
    RETURNS: A list containing the fetched links.
    '''
    results = []
    regex_string = '(http[s]?:\/\/?[^\s(["<,>]*\.[^\s[",><]*' + \
        '.' + extension + ')'

    println("Fetching the webpage...")
    soup = str(urllib.request.urlopen(url).read())

    println("Capturing URLs using regex...")
    results = re.findall(regex_string, soup)
    println("No of links found: " + str(len(results)))
    return results


def write_results_to_file(results, filename):
    '''Writes the results to file specified, if the result list is not empty.
    If the file already exists, the data will be appended to the end of file, otherwise new file will be created.
    '''
    if(len(results) == 0):
        println("No URLs were found.")
    else:
        sys.stdout = open(filename, "a+")
        for url in results:
            print(url)
        sys.stdout = sys.__stdout__
        println("Results written to file " + filename)


if __name__ == "__main__":

    PRINT_ENABLED = True
    try:
        choice = int(input(
            "Select option: \n1. Get all <a> links (using BeautifulSoup)\n2. Capture every URL in webpage text (using Regex)\n> "))
    except:
        println("Incorrect option.\n")
        exit(0)

    url = get_url()
    extension = get_extension()
    filename = get_file_name()

    if(choice == 1):
        write_results_to_file(get_all_links_by_soup(url, extension), filename)
    elif(choice == 2):
        write_results_to_file(get_all_links_by_regex(url, extension), filename)
