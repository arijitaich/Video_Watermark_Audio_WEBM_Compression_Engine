#!/usr/bin/python

import sys, getopt

def main(argv):
   inputfile = ''
   keypass = ''
   try:
      opts, args = getopt.getopt(argv,"hi:k:",["ifile=","key="])
   except getopt.GetoptError:
      print ('in.py -i <inputfile> -k <user_key>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('in.py -i <inputfile> -k <user_key>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-k", "--key"):
         keypass = arg
   print(inputfile)
   print(keypass)

if __name__ == "__main__":
   main(sys.argv[1:])


