# -*- coding: utf-8 -*-
"""
Created on Sun May 13 16:26:52 2018

@author: Roshan
"""

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
    regex = r "https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if(re.search(regex, url)):
        return url
    else:
        println("Invalid URL\n")
        get_url()


def get_extension():
    extension = input(
        "Enter the file EXTENSION the urls must end with (ex. pdf, doc, mp3 etc): ")
    extension = extension.replace(".", "")
    if(len(extension) == 0):
        println("No EXTENSION specified. All urls on the webpage will be fetched.")
    return extension


def get_all_links_by_soup(url, extension):

    results = []
    regex_string = '(http[s]?:\/\/)?[^\s(["<,>]*\.[^\s[",><]*' + \
        '.' + EXTENSION + '$'

    println("Fetching the webpage...")
    soup = urllib.request.urlopen(url)

    println("Parsing using BeautifulSoup...")
    web_obj = BeautifulSoup(soup, "html5lib")
    web_obj = web_obj.findAll('a', attrs={'href': re.compile(regex_string)})
    for url in web_obj:
        results.append(url.get('href'))
    return results


def get_all_links_by_regex(url, extension):

    results = []
    regex_string = '(http[s]?:\/\/)?[^\s(["<,>]*\.[^\s[",><]*' + \
        '.' + EXTENSION

    println("Fetching the webpage...")
    soup = urllib.request.urlopen(url)

    println("Capturing URLs using regex...")
    results = re.findall(regex_string, soup)
    return results


def write_results_to_file(results, filename):
    if(len(results) == 0):
        println("No urls were found.")
    else:
        sys.stdout = open(filename, "a+")
        for url in results:
            print(url)
        sys.stdout = sys.__stdout__
        println("Results written to file " + filename)

if __name__ == "__main__":

    PRINT_ENABLED = True
    try:
        choice = int(input("Select option: \n1. Get all <a> links (using BeautifulSoup)\n2. Capture every URL in webpage text (using Regex)"))
    except:
        println("Incorrect option.\n")
        exit(0)

    if(choice == 1):
        write_results_to_file(get_all_links_by_soup(get_url(), get_extension()), get_file_name())
    elif(choice == 2):
        write_results_to_file(get_all_links_by_regex(get_url(), get_extension()), get_file_name())

