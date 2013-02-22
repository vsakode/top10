#!/usr/bin/python
'''
Created on May 13, 2012

@author: vsakode
'''
import sys
import os
import subprocess

def usage():
    print "[INFO:] Prints top 10 most repeated log messages"
    print "[Usage]", sys.argv[0]
    print "\t" ,sys.argv[0] , " filename" 
    print "\t-h [Help Options]"
    print "\t--help [Help Options]"
    sys.exit()

def getFileName():
    if len(sys.argv) == 1:
        filename = "/var/log/messages"
    else:
        filename = sys.argv[1]
    return filename 

def isReadable(infile):
    try :
        token = open(infile, 'rU')
        token.close()
    except:
        print "%s exists but not readable..... check the permissions or Run as root" %(infile)  
        sys.exit()
    return True

def main():
    if len(sys.argv) > 2:
        usage()
    elif len(sys.argv) == 2 and (str(sys.argv[1]) == '-h' or str(sys.argv[1]) == '--help'):
            usage()
    else:
        infile = getFileName()
        if os.path.exists(infile) and isReadable(infile):
            cmd = "awk '{$1=\"\"; $2=\"\"; $3=\"\"; print}' "+ infile + " | sort | uniq -c | sort -nr | head -10"
            proc = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout = subprocess.PIPE)
            print "*********************** TOP 10 log messages in %s ************************" %(infile)
            print "    Count            Message"
            print "---------------------------------------------------------------------"
            for line in proc.stdout:
                print (line.rstrip())
        else:
            print infile, " does not exists"
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass