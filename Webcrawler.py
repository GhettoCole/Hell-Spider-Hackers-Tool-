from os import name
from os import getuid
from os import system
import pip

class WebCrawler():
    def __init__(self, base_url):
        self.base_url = base_url

    def get_absolute_url(self):
        if self.base_url[:7] == "https://":
            return self.base_url
        elif self.base_url[:6] == "http://":
            return self.base_url
        else:
            return "https://" + self.base_url

    def update_tool(self):
        cont = """
#!/bin/bash

cd /usr/share/HellSpider
python3 HellSpider "$@"
        """
        #  windows
        if name != "nt":
            if getuid() == 0:
                system("git clone https://github.com/GhettoCole/Hell-Spider-Hackers-Tool- /usr/share/HellSpider")
                packages = ["requests", "bs4", "prettytable", "lxml"]
                for pkg in packages:
                    pip.main(["install", pkg])

                file = open("/usr/bin/HellSpider", "w")
                file.write(cont)
                file.close()

                system("chmod +x /usr/bin/HellSpider")
                print("Tool Updated")
            else:
                print("\033[1;91mRUN AS ROOT\033[0m")
        else:
            print("Unsupported OS")
