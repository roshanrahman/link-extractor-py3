# linkextractor.py

A simple python script that extracts all links from a URL, uses BeautifulSoup and regex modules

## Requirements:

This is a Python 3 script, and therefore will not work on Python 2 versions.
Uses `urllib` and `re` modules, along with `bs4`

If you do not have Beautiful Soup 4 installed, use pip to install it: 

```python
pip install beautifulsoup4
```

## Usage:

### Run the python script from its location:

The script will ask you the following:
1. #### Mode of fetching links:

    * Beautiful Soup - fetches all links in \<a\> tags in the source code.
    * Regular Expressions - fetches all links wherever located in the source code. (fetches more links)

2. #### URL:
    
    A valid URL must be specified.

3. #### Extension:

    The extension the URL must end with.
    Example, to fetch all links to PDFs, enter `pdf`
    
    Leave it empty if you want __all__ links.

4. #### File where results must be stored:

    A valid file name must be specified. The script will record all fetched links in the specified file. By default, it will write to `results.txt`

### Use from another script:

1. #### Copy the module `linkextractor.py` to a location where it can be imported into your script.

2. #### Import the module.

3. #### Use the procedures to perform the required operation. 
    The procedures are documented with docstrings. Use `help(module_name)` to get information about the module and its contents. 

    #### Example:
    ```python
    import linkextractor
    
    url = "https://github.com/EbookFoundation/free-programming-books/blob/master/free-programming-books.md"

    print(linkextractor.get_all_links_by_soup(url, 'pdf'))
    ```
    
    #### Outputs:

    
    ```
    ['https://people.gnome.org/%7Eswilmet/glib-gtk-dev-platform.pdf', 'https://www.math.upenn.edu/%7Ewilf/AlgoComp.pdf', 'http://cslibrary.stanford.edu/110/BinaryTrees.pdf', 'http://www-inst.eecs.berkeley.edu/%7Ecs61b/fa14/book2/data-structures.pdf', 'http://lib.mdp.ac.id/ebook/Karya%20Umum/Dsa.pdf', 'http://cslibrary.stanford.edu/103/LinkedListBasics.pdf', 'http://cslibrary.stanford.edu/105/LinkedListProblems.pdf',
    ...]
    ```

    
    


*Feedback of all kinds is welcome!*
