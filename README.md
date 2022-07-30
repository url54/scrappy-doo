# About Scrappy-Doo
Scrappy-doo, scrapes the juicy goodness from websites. Providing a full-url, Scrappy-doo will print off the the following items from the website's page:
- The website title.
- Website Meta Information.
- Any comments in the page.
- Any hidden form fields in the page.
- All anchor tag hrefs.
- All script tag srcs.
- And all webpage strings.

# Screenshot
![Main Image](Images/scrappy-doo.png)

# Installation
```bash
git clone https://github.com/url54/scrappy-doo.git
```

# Recommend Python Version
Scrappy-doo was written in Python 3.10.5. This is the only version that it has been tested with, however, most of the requirements are pretty generic, and should work with other versions of Python. 

# Dependencies
Srappy-doo was written with Requests, Re, Argparse, BeautifulSoup, pathlib, and colorama. This dependencies can be installed using the requirements.txt file.

- Installation on Linux:
```bash
sudo pip install -r requirements.txt
```

# Usage
Currently the only required switch is the -u switch, followed by the full-url of the target. I added argparse, as I intend to add more functionality to it over time.
Short | Long | Description
------|------|------------
-u | --url | Full URL of your target.
X | X | XXXX

# Examples
- Basic usage
```bash
./scrappy_doo.py -u https://www.google.com
```

