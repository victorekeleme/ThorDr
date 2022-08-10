import random
import os

def ranPath():
    codeGen ='122'+ str(random.randint(1000,10000))
    currentPath = os.path.dirname(os.path.abspath(__file__))
    downloadPath = currentPath+'/'+codeGen
    return downloadPath

