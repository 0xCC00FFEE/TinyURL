#!/usr/bin/env python2
try:
    import urllib2,urllib,os,sys
except ImportError,err:
    print "[~]Invalid Module(s) !"
    print "[~]%s ." % err
    sys.exit(0)

def usage():
    print """
#################################################
### 		TinyURL v0.1		      ###
#################################################

Usage :
*******

./tiny <uri-goes-here>

"""

url="http://tinyurl.com/api-create.php?url="

if len(sys.argv) != 2:
    usage();
    sys.exit(0);
if str(sys.argv[1]).find("http://") == -1 and  str(sys.argv[1]).find("https://") == -1:
	sys.argv[1]="http://"+sys.argv[1]
req=urllib2.urlopen(url+str(sys.argv[1]))
data=req.read()
print "\n[~] URL : "+str(data) + "\n"


