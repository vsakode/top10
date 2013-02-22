#!/usr/bin/python
'''
Created on May 13, 2012

@author: vsakode
'''
import sys
import os
import operator

def usage():
    """
    Prints the Usage if the script is invoked incorrectly
    """
    print "[INFO:] Prints top 10 most repeated log messages"
    print "[Usage]", sys.argv[0]
    print "\t" ,sys.argv[0] , " filename" 
    print "\t-h [Help Options]"
    print "\t--help [Help Options]"
    sys.exit()


def getFileName():
    """
    Retrieves filename based on the way script is invoked
    No argument - /var/log/messages
    single argument - argv[1]
    """
    if len(sys.argv) == 1:
        filename = "/var/log/messages"
    else:
        filename = sys.argv[1]
    return filename 


def isReadable(infile):
    """
    Checks if the log file is readable
    """
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
            dictlog = {}
            token = open(infile,'rU')
            ##Read file line by line ###
            while 1:
                line = token.readline()
                if not line:
                    break
                else:
                    sline = line.split()
                    strline = " ".join(sline[3:])
                    ###Store the stripped log entry in the dictionary dictlog{}
                    if dictlog.has_key(strline):
                        dictlog[strline] = dictlog[strline] + 1
                    else:
                        dictlog[strline] = 1
            
            ##Sorts the dictionary over the values###
            sorted_logs = sorted(dictlog.iteritems(), key=operator.itemgetter(1), reverse = True)
            print "*********************** TOP 10 log messages in %s ************************" %(infile)
            print "    Count            Message"
            print "---------------------------------------------------------------------"
            ###Prints top 10 log messages####
            for slog in sorted_logs[0:10] :
                (log, repeat) = slog
                print repeat, "\t",log
                
        else:
            print infile, " does not exists"
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass