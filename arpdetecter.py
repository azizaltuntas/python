#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Tkinter import *
from tkMessageBox import *

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def arpA():
	showwarning("Alarm", "Arp Poisoning Tespit Edildi !")
	
print colors.GREEN + 'ARP POİSONİNG DETECTED' + colors.END

gateip = (os.popen("route | grep 'UG[ /t]' | awk '{print $2}'")).read()

print colors.BLUE + 'Gateway İP Tespit Edildi : %s' %gateip + colors.END

arp = (os.popen("arp -a '%s' | awk '{print $4}' | uniq -1" %gateip )).read()

print colors.BLUE + "Gateway Mac Tespit Edildi : %s" %arp + colors.END


while True:
	arp2 = (os.popen("arp -a '%s' | awk '{print $4}' | uniq -1" %gateip )).read()
	if arp != arp2:
		print colors.RED + 'Arp Poisoning Tespit Edildi !\n' + colors.END
		print colors.RED + 'Saldırıyı Gerçekleştirenin Mac Adresi : %s' %arp2 + colors.END
		
		arpA()
		break

		
		
	

