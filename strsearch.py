#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Coded : azizaltuntas

import os
import sys
import re
from optparse import OptionParser

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

try:

    parser = OptionParser('/Usage %prog <Python Version 2> ' + \
                          '-d </home/dirs/> --filetype <txt> -s <string>', version="%prog v1")
    parser.add_option("-d", "--dir", dest="dizi",
                      help="Scan Dir PATH")
    parser.add_option("-f", "--filetype", dest="filety",
                      help='Cat - Filetype <txt>')
    parser.add_option("-s", "--string", dest="dddd",
                      help='Search string to file')
    (options, args) = parser.parse_args()

    dizin = options.dizi
    fil = options.filety
    ddd = options.dddd

    #dizin = sys.argv[1]
    #fil = sys.argv[2]
    stri = []
    say =+ 0

    for root, dizin, files in os.walk("{}".format(dizin), topdown=True):
        for file in files:
            if file.endswith(".{}".format(fil)):
                 bak = os.path.join(root, colors.RED + "----->", file + colors.END)
                 with open(root + '/' + file  , 'r') as f:
                     data = f.readlines()
                     for a in data:
                         if ddd in a:
                             a = stri.append(bak)
                             print(stri[-0-1])
    if len(stri) == 0:
       print("Sorry")
    if dizin == None or fil == None or ddd == None:
        print(parser.usage)


except:
    print()
