## Tool Title: SQLI Vulnerability Sites finder
## Tool Descrption: This tool is used to find SQLI Vulnerability Sites using google dork
## Tool Author: G0dsecurity
## Tool Version: 1.0



from bs4 import BeautifulSoup
import requests
import argparse
import os
import sys
from termcolor import colored
import threading
import random

argparser = argparse.ArgumentParser()
argparser.add_argument('-d', '--dork', help='Specify the dork', required=True)
argparser.add_argument("-p", "--page", help="Specify the page number", required=True)
args = argparser.parse_args()
args_dork = args.dork
args_page = args.page




def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')

print ("")
A = """             
                    |
  ,_._._._._._._._._T__________________________________________________________
  |G|o|o|g|l|e|_|_|_O_________________________________________________________/
                    R                                                           V1.0
                    |
                    
    King Dork Scanner (king) coded by G0dsecurity
    please use -h to see help
    """
print ("")
print(A)




website_list=[] #list of websites
dork = "inurl:" + input(colored("Please input the sqli Dork(eg- php?id=, aspx?id=) ---->  ",'cyan'))
extension = "site:" + input(colored("Please specify the website extension(eg- .in,.com,.pk) [default: none] -----> ",'cyan')) #Add none as extension
total_output = int(input(colored("Pleases specify the total no. of websites you want) ----> ",'cyan')))
page_no = int(input(colored("From which Google page you want to start(eg- 1,2,3) ----> ",'cyan')))

def web_headers():
    web_headers = "mozilla/5.0 (x11; linux x86_64) applewebkit/537.36 (khtml, like gecko) chrome/51.0.2704.103 safari/537.36"
    return web_headers
while (page_no <= total_output):
    url = "https://www.google.com/search?q="+dork+extension+"&start="+str(page_no)
    req = requests.get(url, headers={'User-Agent': web_headers()})
    source = req.text
    soup = BeautifulSoup(source, 'html.parser')
    for a in soup.find_all('a'):
        link = a.get('href')
        if "google" not in link:
            website_list.append(link)
    page_no = page_no + 10
    if page_no > total_output:
        break




 


        

def dorks_google():
    dorks_google = "https://www.google.com/search?= site:shop"+dork+extension+"&start="+str(page_no)
    return dorks_google
dorks_google = requests.get(dorks_google(), headers={'User-Agent': web_headers()})
dorks_google = dorks_google.text
dorks_google = BeautifulSoup(dorks_google, 'html.parser')
for a in dorks_google.find_all('a'):
    link = a.get('href')
    if "google" not in link:
        website_list.append(link)
    else:
        pass




## Saving file
def output():
    output = open("sqli.txt", "w")
    for i in website_list:
        output.write(i+"\n")
    output.close()
output()
print (colored("All vulnerable sites are saved in sqli.txt",'green'))

## google timetout
def timeout():
 timeout = requests.get("https://www.google.com/search?= site:shop"+dork+extension+"&start="+str(page_no), headers={'User-Agent': web_headers()}, timeout=5)
timeout()

## Function to use proxy list to not being blocked by google
def proxy():
    proxy = open(args.proxy, "r")
    proxy = proxy.readlines()
    proxy = [x.strip() for x in proxy]
    proxy = random.choice(proxy)
    proxy = {"http": proxy, "https": proxy}
    return proxy
proxy = proxy()
proxy = requests.get("https://www.google.com/search?= site:shop"+dork+extension+"&start="+str(page_no), headers={'User-Agent': web_headers()}, proxies=proxy)
proxy = proxy.text
proxy = BeautifulSoup(proxy, 'html.parser')
for a in proxy.find_all('a'):
    link = a.get('href')
    if "google" not in link:
        website_list.append(link)
    else:
        pass

    def threads():
        threads = args.threads
        return threads
    threads = threads()
    threads = requests.get("https://www.google.com/search?= site:shop"+dork+extension+"&start="+str(page_no), headers={'User-Agent': web_headers()}, threads=threads)
    threads = threading.Thread(target=threads)
    threads.daemon = True
    threads = threading.max_thread(threads)
    threads.start()




