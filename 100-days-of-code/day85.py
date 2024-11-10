# ******************************************** command line utility *****************************************************

# https://github.com/CodeWithHarry/100-days-of-code-youtube/blob/main/85-Day-85-Command-Line-Utility/.tutorial/Tutorial.md

# curl is a command line utility
# curl https://www.filmmovement.com/userFiles/uploads/films/200-meters/200_METERS_Still01_PhotoCAlaa_Aliabdallah.jpg --output dest_name -> hm isse ek link s img download bhi kr skte hai and use apne desired location main store krwa skte hai

# command line utility means jise hm cmd line main cmds dekr kuch kaam krwa skte hai

'''
import argparse #built-in in python

parser = argparse.ArgumentParser()

# Add command line arguments
parser.add_argument("url", help="url of file to download")
parser.add_argument("output", help="by which name u want to save file")

# Parse the arguments
args = parser.parse_args()

# Use the arguments in your code
print(args.url)
print(args.output)
'''

import argparse
import requests

def downloadFile(url, fileName):
    if fileName is None:
        fileName = url.split('/')[-1] #url s le lega file name
    with requests.get(url, stream = True) as r:
        r.raise_for_status()
        with open(fileName, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return fileName
parser = argparse.ArgumentParser()

parser.add_argument("url", help = "url of file to download")
parser.add_argument("-o", "--output", help="Name of file", default=None)

args = parser.parse_args()

print(args.url)
print(args.output)
downloadFile(args.url, args.output)