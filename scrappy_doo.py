#!/usr/bin/python3
import re
import requests
import argparse
import pathlib
from bs4 import BeautifulSoup
from colorama import Fore,Back,Style,init

init(autoreset=True)

def title_ascii():
    print(Fore.RED + "     _____                                      ____")
    print(Fore.WHITE + "    / ___/______________ _____  ____  __  __   / __ \____  ____")
    print(Fore.BLUE + "    \__ \/ ___/ ___/ __ `/ __ \/ __ \/ / / /  / / / / __ \/ __ /")
    print(Fore.RED + "   ___/ / /__/ /  / /_/ / /_/ / /_/ / /_/ /  / /_/ / /_/ / /_/ /")
    print(Fore.WHITE + "  /____/\___/_/   \__,_/ .___/ .___/\__, /  /_____/\____/\____/")
    print(Fore.BLUE + "                      /_/   /_/    /____/                      ")
    print("")
    print(Fore.WHITE + "          -The web scraping assistant-               ")
    print(Fore.BLUE + "                @url54                         ")

HEADERS = {\
"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114",\
"Accept-Language":"en-US",\
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",\
"Accept-Encoding":"gzip, deflate"}

parser = argparse.ArgumentParser(description="Scrape websites for the juicy stuff..")
parser.add_argument("-u", "--url", type=str, required=True, help="Provide the full URL for the target.")
parser.add_argument("-f", "--full", action="store_true", help="Full target scrape.")
parser.add_argument("-a", "--anchor", action="store_true", help="Scrape the hrefs from the anchor tags.")
parser.add_argument("-m", "--meta", action="store_true", help="Scrape the meta tags from the target.")
parser.add_argument("-c", "--comment", action="store_true", help="Scrape comments from the target.")
parser.add_argument("-s", "--source", action="store_true", help="Scrape sources from script tags.")
parser.add_argument("-S", "--string", action="store_true", help="Scrape strings from the target.")
parser.add_argument("-H", "--hidden", action="store_true", help="Scrape hidden form field items.")
args = parser.parse_args()


def web_title(soup):
    print(Fore.RED + ("-" *75 ))
    print(Fore.RED + (" "*30) + "Title of webpage:")
    print(Fore.RED + ("-"*75))
    print(soup.title.string)

def meta_tags(soup):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*25) + "Website Meta Information:")
    print(Fore.RED + ("-"*75))
    meta_t = soup.find_all("meta")
    for x in meta_t:
        print(x)

def find_comments(resp):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*32) + "Any Comments:")
    print(Fore.RED + ("-"*75))
    comments = re.findall("(<!--.*?-->)", resp.text)
    if len(comments) != 0:
        for comment in comments:
            print(comment)
    else:
        print("No comments found..")

def find_hidden(soup):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*32) + "Hidden fields:")
    print(Fore.RED + ("-"*75))
    hidden_fields = soup.find_all("input", type="hidden")
    if len(hidden_fields) != 0:
        for field in hidden_fields:
            print(field)
    else:
        print("No hidden elements found..")

def anchor_tags(soup):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*30) + "Anchor Tag hrefs:")
    print(Fore.RED + ("-"*75))
    hrefs = []
    for link in soup.find_all("a"):
        hrefs.append(link.get("href"))
    if len(hrefs) != 0:
        for href in hrefs:
            print(href)
    else:
        print("No hrefs found..")


def script_sources(soup):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*30) + "Script Tag srcs:")
    print(Fore.RED + ("-"*75))
    srces = []
    for source in soup.find_all("script"):
        if source.get("src") == None:
            pass
        else:
            srces.append(source.get("src"))
    if len(srces) != 0:
        for srce in srces:
            print(srce)
    else:
        print("No srcs found in scripts..")

def webpage_strings(soup):
    print(Fore.RED + ("-"*75))
    print(Fore.RED + (" "*30) + "Webpage Strings:")
    print(Fore.RED + ("-"*75))
    stringer = []
    for string in soup.strings:
        if len(string) <= 4:
            pass
        else:
            stringer.append(string)
    if len(stringer) != 0:
        print(stringer)
    else:
        print("No strings found..")

def full_package(resp, soup):
    print(Fore.YELLOW + ("="*75))
    print(Fore.YELLOW + f" Target: {resp.url} |  Status-Code: [{resp.status_code}]   ")
    print(Fore.YELLOW + ("="*75))
    web_title(soup=soup)
    meta_tags(soup=soup)
    find_comments(resp=resp)
    find_hidden(soup=soup)
    anchor_tags(soup=soup)
    script_sources(soup=soup)
    webpage_strings(soup=soup)
    print(Fore.RED + ("="*75))

if __name__ == "__main__":
    title_ascii()
    try:
        resp = requests.get(args.url, headers=HEADERS)
        if resp.status_code in range(200,299):
            soup = BeautifulSoup(resp.text, "lxml")
            while args.full or args.anchor or args.source or args.string or args.hidden:
                if args.full:
                    full_package(resp, soup)
                    args.full = False
                if args.anchor:
                    anchor_tags(soup)
                    args.anchor = False
                if args.meta:
                    meta_tags(soup)
                    args.meta = False
                if args.comment:
                    find_comments(resp)
                    args.comment = False
                if args.source:
                    script_sources(soup)
                    args.source = False
                if args.string:
                    webpage_strings(soup)
                    args.string = False
                if args.hidden:
                    find_hidden(soup)
                    args.hidden = False
                else:
                    pass
        elif resp.status_code in range(300,399):
            print(Fore.YELLOW + f"REDIRECTED -- [{resp.status_code}] -- at -- {resp.url}")
        elif resp.status_code == 404:
            print(Fore.YELLOW + f"404'ED -- [{resp.status_code}] -- at -- {resp.url}")
        elif resp.status_code in range(400, 403):    
            print(Fore.YELLOW + f"FORBIDDEN -- [{resp.status_code}] -- at -- {resp.url}")
        elif resp.status_code in range(500,599):
            print(Fore.YELLOW + f"JUICY STUFF -- [{resp.status_code}] -- at -- {resp.url}")
        else:
            print(f"I don't know what the hell this status code is for [{resp.status_code}].")
    except Exception as e:
        print(e)