#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

print "eScCopyright DirBuster"

try:
     site = raw_input('Url Yaz : ')
    
     connect = httplib.HTTPConnection(site)
     connect.connect()
     print ("[+] Bağlantı Var Devam")
except:
     print ("[-] Bağlantı yok")
     exit()
dizinFile = raw_input('Dizinler: ')
dizin = open(dizinFile).readlines()

for diz in dizin:
	
 	diz = diz.strip()
	connect.request('HEAD', '/' + diz)
	
	
    	url = "http://{0}/{1}" .format(site, diz)
    	print "Denenen: {0}" .format(url)

    	response = connect.getresponse()
    	print ' Yanıt: ', response.status, response.reason

    	connect.close()

    	if response.status == 200:
		print (" (!!!) '{0}' adında bir dizin var").format(diz)
		
