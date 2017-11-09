#-------- Exsend -> Exploit Sender ----------
#Simplifies the remote exploit writing process
# By: Sammie Bush
#
#reads a file that contains targetip, targetport, listeningip, listeningport, and a series of inputs(inputN)
#starts listener for reverse shell
#inputs can include exploits

import string
import sys
import argparse

parser = argparse.ArgumentParser(description='Execute remote exploit files.')
parser.add_Argument('--filename', type=str, default=None, help='Name of remote exploit file.')



args = parser.parse_args()


targetip = ''
targetport = ''

listeningip = ''
listeningport= ''

inputs = []




searchfile = open("file.txt", "r")
for line in searchfile:
    if "searchphrase" in line: print line








searchfile.close()
