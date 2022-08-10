import subprocess
import sys
import json
import os
import shutil
import time
from pathGen import ranPath
from zipper import zipper
import re


# magnet_link = str(input("Enter magnet link: "))

# Gets the title of the download
def get_title(magnet_link):
    if str(magnet_link)[:15] != "magnet:?xt=urn:":
        return "Invalid magnet link try again"
    else:
        cmd= []
        cmd.append("screen")
        cmd.append("-dm")
        cmd.append("webtorrent")
        cmd.append("info")
        cmd.append(magnet_link)
        try:
            if sys.platform.startswith('linux'):
                fname = json.loads(subprocess.check_output(cmd))['name'] # Gets the name of the file
                return fname
        except Exception as e:
            print(e)


def handler(magnet_link):
    title = get_title(magnet_link)
    rPath = ranPath()
    done = False

    cmd=[]
    cmd.append("screen")
    cmd.append("-dm")
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    cmd.append("-o")
    cmd.append(rPath)
    
    try:
        if sys.platform.startswith('linux'):
            print("downloading...please wait")         
            subprocess.call(cmd) #Downloads the file
            done = True
            zipper(rPath,done)
    except Exception as e:
        print(e)
        done = False
    
    link=str(os.listdir(rPath)[0])
    fPath = str(rPath+'/'+link) 

    return f"{fPath}"


link = "magnet:?xt=urn:btih:B3E689DF0E92AA6D1DCB3945A3B4746D0914B1D4&dn=Too+Much+and+Never+Enough%3A+How+My+Family+Created+the+World%26%23039%3Bs+Most+Dangerous+Man+%7C+EPUB+%2B+MOBI+&tr=udp%3A%2F%2Fexplodie.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.torrent.eu.org%3A451%2Fannounce&tr=udp%3A%2F%2Ftracker.uw0.xyz%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.kamigami.org%3A2710%2Fannounce&tr=https%3A%2F%2Ftracker.nanoha.org%3A443%2Fannounce&tr=udp%3A%2F%2Fretracker.akado-ural.ru%3A80%2Fannounce&tr=http%3A%2F%2Ftracker.files.fm%3A6969%2Fannounce&tr=udp%3A%2F%2Fopentor.org%3A2710%2Fannounce&tr=udp%3A%2F%2Fvalakas.rollo.dnsabr.com%3A2710%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce"