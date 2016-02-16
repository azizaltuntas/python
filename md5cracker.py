#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib

al = raw_input('Hash ? : ')
if len(al) != 32:
	print "Dont Md5 Hash ?"
	exit()
list = raw_input('Wordlist ? : ')
temiz = open(list).readlines()

for esc in temiz:
	esc = esc.strip()
	headshot = hashlib.md5(esc).hexdigest()
	if headshot == al:
		print "CRACKED: " + esc
	else:
		print "Don't Cracked..!"
		quit()
