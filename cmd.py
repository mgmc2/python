import webbrowser
import os
import sys
from subprocess import call
import time
login = "no"
user = "admin"
passw = "login"
while login == "no":
     u=input("<> u: ")
     if u == user:
          p=input("<> p: ")
          if p == passw:
               print("Welcome to cmd_exe, created by Max Gowers in Nov 2018 in Python.")
               print("If you are unsure what to do, type 'helpme'.")
               while True:
                    cmd=input(">")
                    if cmd == "it.google":
                        print("<> Opening 'http://www.google.co.uk'...")
                        webbrowser.open("http://www.google.co.uk")
                        
                    elif cmd == "op.calc":
                         print("<> Opening calculator...")
                         call(["calc.exe"])
                         
                    elif cmd == "op.note":
                        print("<> Opening notepad...")
                        call(["notepad.exe"])

                    elif cmd == "op.chrome":
                         print("<> Opening Chrome...")
                         call(["chrome.exe"])
                    
                    elif cmd == "it.in":
                        topen=input("<> Enter a web adress. Be sure to add the http:// or https:// at the end, unless it is an ip adress, or an 'about:' site: ")
                        print("Opening",topen,"...")
                        if topen == "cancel":
                             cmd=input(">")
                        else:
                             webbrowser.open(topen)

                    elif cmd == "srch.google":
                         srch=input("<> Enter a single search term: ")
                         if srch == "cancel":
                              cmd=input(">")
                         yn=input("<> Do you want to add another word? y/n: ")
                         if yn == "y":
                              srchtwo=input("<> Type another search term: ")
                              if srchtwo == "cancel":
                                   cmd=input(">")
                              if yn == "n":
                                   webbrowser.open("http://www.google.co.uk/search?q="+srch)
                              srchtot="http://www.google.co.uk/search?q="+srch+"+"+srchtwo
                         webbrowser.open(srchtot)
                         print("<> Opening",srchtot,"...")

                    elif cmd == "type":
                         typed=input("<> Type what you want to be displayed: ")
                         if typed == "cancel":
                              cmd=input(">")
                         else:
                              print("<>",typed)
                    elif cmd == "srch.yt":
                         ytsrch=input("<> Enter a search term: ")
                         if ytsrch == "cancel":
                              cmd=input(">")
                         yn=input("<> Do you want to add another search term? y/n: ")
                         if yn == "y":
                              ytsrchtwo=input("<> Type another search term: ")
                              ytsrchone="https://www.youtube.com/results?search_query="+ytsrch
                              if ytsrchtwo == "csncel":
                                   cmd=input(">")
                              if yn == "n":
                                   webbrowser.open(ytsrchone)
                                   print("<> Opening",ytsrchone,"...")
                              ytsrchtot="https://www.youtube.com/results?search_query="+ytsrch+"+"+ytsrchtwo
                              webbrowser.open(ytsrchtot)
                              print("<>Opening",ytsrchtot,"...")
                         

                    elif cmd == "helpme":
                         print("<> Welcome to cmd_exe, coded in Python by Max Gowers in November 2018. The current list of accepted commands is below:")
                         print("it.google: Directs you to google.co.uk in a new browser window.")
                         print("op.calc: Opens the Calculator program on your computer.")
                         print("op.note: Opens the Notepad program on your computer.")
                         print("op.chrome: Opens Chrome, if it is installed.")
                         print("it.in: Allows you to enter a web adress, then be directed to it in a new browser window.")
                         print("srch.google: Allows you to enter up to 2 search terms, then search Google for them.")
                         print("type: Allows you to type anything, then have it displayed.")
                         print("srch.yt: Allows you to enter up to 2 search terms, then search YouTube for them.")
                         print("Type 'cancel' whenever the CMD asks you to type, and the operation will be cancelled.")

                    else:
                        cmd=input(">")
