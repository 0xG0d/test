## Software Title: King Google Dork Urls Decoder
## Sofware Purpose: This software is used to decode the urls from the king.py
## Software Author: G0dsecurity
## Software Version: 1.0
## Software License: MIT
## Software Language: Python
## Software Path: decoder.py

from bs4 import BeautifulSoup
import requests
import argparse
import os


argparser = argparse.ArgumentParser()
argparser.add_argument("-f", "--file", help="Specify the file name", required=True)
args = argparser.parse_args()
args_file = args.file

## Function to decode the urls from sqli.txt file and changing it to the original url
def decode_url():
    decode_url = []
    for url in open(args_file, "r"):
        url = url.replace("/url?q=", "")
        url = url.replace("%3F", "?")
        url = url.replace("%3D", "=")
        url = url.replace("%26", "&")
        url = url.replace("%2F", "/")
        url = url.replace("%3A", ":")
        url = url.replace("%2C", ",")
        url = url.replace("%3B", ";")
        url = url.replace("%2B", "+")
        url = url.replace("%25", "%")
        url = url.replace("%23", "#")
        url = url.replace("%21", "!")
        url = url.replace("%5B", "[")
        url = url.replace("%5D", "]")
        url = url.replace("%7B", "{")
        url = url.replace("%7D", "}")
        url = url.replace("%7C", "|")
        url = url.replace("%5C", "\\")
        url = url.replace("%5E", "^")
        url = url.replace("%60", "`")
        url = url.replace("%3C", "<")
        url = url.replace("%3E", ">")
        url = url.replace("%22", '"')
        url = url.replace("%27", "'")
        url = url.replace("%3F", "?")
        url = url.replace("%3D", "=")
        url = url.replace("%26", "&")
        url = url.replace("%2F", "/")
        url = url.replace("%3A", ":")
        url = url.replace("%2C", ",")
        url = url.replace("%3B", ";")
        url = url.replace("%2B", "+")
        url = url.replace("%25", "%")
        url = url.replace("%23", "#")
        url = url.replace("%21", "!")
        


        url = url.split("&sa=")
        url = url[0]
        decode_url.append(url)




## Create a function to select the encoded urls from the file
def select_urls():
    select_urls = open(args_file, "r")
    select_urls = select_urls.read()
    select_urls = select_urls.split("\n")
    return select_urls
select_urls = select_urls()

## Create a function to decode the urls from sqli.txt file
def decode_urls():
    decode_urls = []
    for url in select_urls:
        url = url.replace("/url?q=", "")
        url = url.split("&sa=")
        url = url[0]
        decode_urls.append(url)
    return decode_urls
decode_urls = decode_urls()

## Function to save decoded urls in a file called ""decoded.txt"
def save_urls():
    save_urls = open("decoded.txt", "w")
    for url in decode_urls:
        save_urls.write(url + "\n")
    save_urls.close()
save_urls()
print("Decoded urls saved in decoded.txt file")




