# link-extractor.py

A simple python script that extracts all links from a URL, uses BeautifulSoup and regex modules

## Usage:

Run the python script from its location, with arguments (optional):

`python link-extractor.py [URL] [FILE-TO-STORE-LINKS-TO]`

Example: `python link-extractor.py http://www.google.com link-list.txt`

*If the arguments are not specified, the script will ask you.*

You will be asked to specify the file extension the link should end with. Leave it empty if you want __all__ links.

_Example: If you want pdf files, then specify `pdf`_

