#!/usr/bin/env python3
# encoding: utf-8

import sys
import subprocess

def fp_con(spf):
         values = {"9b":"1", "98":"2", "99":"3", "9e":"4", "9f":"5", "9c":"6", "9d":"7", "92":"8", "93":"9", "9a":"0",
                  "cb":"a", "c8":"b", "c9":"c", "ce":"d", "cf":"e", "cc":"f", "cd":"g", "c2":"h", "c3":"i", "c0":"j", 
                  "c1":"k", "c6":"l", "c7":"m", "c4":"n", "c5":"o", "da":"p", "db":"q", "d8":"r", "d9":"s", "de":"t",
                  "df":"u", "dc":"v", "dd":"w", "d2":"x", "d0":"y", "d3":"z", "91":"ö", "8d":"ä", "f1":"ü", "f5":"ß",
                  "eb":"A", "e8":"B", "e9":"C", "ee":"D", "ef":"E", "ec":"F", "ed":"G", "e2":"H", "e3":"I", "e0":"J",
                  "e1":"K", "e6":"L", "e7":"M", "e4":"N", "e5":"O", "fa":"P", "fb":"Q", "f8":"R", "f9":"S", "fe":"T",
                  "ff":"U", "fc":"V", "fd":"W", "f2":"X", "f0":"Y", "f3":"Z"}

         r = ""

         try : 
	         fp = spf
	 
         except :
	            print ("USAGE: python3 fpconvert.py <firmware_pw>")
	            exit()

         list = fp.split("%") 
 
         for i in list :                
             if i in values :             
                 r += values[i]
         print(r)

def fp_read():
    sp = subprocess.Popen (["sudo nvram -p | grep security-password"], stdout=subprocess.PIPE, shell=True) 
    tmp = str(sp.stdout.read())
    tmp2 = tmp[21:]
    lgtmp2 = len(tmp2)
    spf = tmp2[:lgtmp2-3]
    return spf


x = fp_read()

fp_con(x)



