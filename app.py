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

