#!/usr/bin/python
# -*- coding: utf-8 -*-
# do9dark
 
import sys
import zipfile
import optparse
from threading import Thread
 
def crack(ZipFile,Word):
   try:
      ZipFile.extractall(pwd=Word)
      print '[+] Found Password: ' + Word
   except:
      pass
 
def main():
   parser = optparse.OptionParser('\n\tpython zipCrack.py -f <zip file> -d <dictionary file>\n\tpython zipCrack.py -f <zip file> -i <number>')
   parser.add_option('-f', dest='zip_name', type='string', help='specify zip file.')
   parser.add_option('-d', dest='dict_name', type='string', help='specify dictionary file.')
   parser.add_option('-i', dest='num_range', type='int', help='specify range of numbers.')
   (options,args) = parser.parse_args()
 
   if(options.zip_name == None):
      print 'Help:\n\tPython zipCrack.py -h\n'
      sys.exit(0)
 
   elif(options.num_range == None) & (options.dict_name == None):
      print 'Help:\n\tPython zipCrack.py -h\n'
      sys.exit(0)
 
   elif(options.zip_name != None) & (options.dict_name != None) & (options.num_range == None):
      zip_name = options.zip_name
      dict_name = options.dict_name
 
      ZipFile = zipfile.ZipFile(zip_name)
      DictFile = open(dict_name)
 
      for line in DictFile.readlines():
         Word = line.strip('\n')
         t = Thread(target=crack, args=(ZipFile,Word))
         t.start()
         
   elif(options.zip_name != None) & (options.dict_name == None) & (options.num_range != None):
      zip_name = options.zip_name
      num_range = options.num_range
 
      ZipFile = zipfile.ZipFile(zip_name)
      Word = num_range+1
 
      for i in range(0,Word):
         t = Thread(target=crack, args=(ZipFile,str(i)))
         t.start()
 
   else:
      print 'Help:\n\tPython zipCrack.py -h\n'
      sys.exit(0)
 
if __name__ == '__main__':
   main()
