#!/usr/bin/python

import sys, getopt
import re
from copy import *

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'cleanGCode.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'cleanGCode.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      
      # Open g-code file
   print "Input: " + inputfile + " Output: " + outputfile
   fin = open(inputfile,'r');
   fout = open(outputfile,'w');      

      # Iterate through g-code file
   l_count = 0
   for line in fin:
         l_count += 1 # Iterate line counter
         
         # Strip comments/spaces/tabs/new line and capitalize. Comment MSG not supported.
         block = re.sub('\s|\(.*?\)','',line).upper() 
         block = re.sub('\\\\','',block) # Strip \ block delete character
         block = re.sub('%','',block) # Strip % program start/stop character
    
         if len(block) == 0 :  # Ignore empty blocks        
            print "Skipping: " + line.strip()        
         else :            
            fout.write(block + '\n')

   print 'Done!'

   # Close files
   fin.close()
   fout.close()

if __name__ == "__main__":
   main(sys.argv[1:])







