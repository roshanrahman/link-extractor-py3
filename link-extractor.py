# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:26:52 2018

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
    url = input("Enter a valid URL: ")
    regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if(re.search(regex, url)):
        return url
    else:
        println("Invalid URL\n")
        return(get_url())


def get_extension():
    extension = input(
        "Enter the file EXTENSION the URLs must end with (ex. pdf, doc, mp3 etc) or ignore: ")
    extension = extension.replace(".", "")
    if(len(extension) == 0):
        println("No EXTENSION specified. All URLs on the webpage will be fetched.")
    return extension


def get_all_links_by_soup(url, extension):

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
        choice = int(input("Select option: \n1. Get all <a> links (using BeautifulSoup)\n2. Capture every URL in webpage text (using Regex)\n> "))
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
