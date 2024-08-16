#!/usr/bin/python
# Version 1.0 Michael Liu

import yaml
import sys

debug = 1
podname = sys.argv[1][0:4]
with open(sys.argv[1], 'r') as f:
 doc = yaml.safe_load(f)
 apppublicip1 = doc["MLM"]["appip"]["public1"]["ip"]
 applbip1 = doc["MLM"]["appip"]["lb1"]["ip"]
 appwebip1 = doc["MLM"]["appip"]["web1"]["ip"]
 appwebip2 = doc["MLM"]["appip"]["web2"]["ip"]
 if debug :
  print ("app ==============")
  print (apppublicip1)
  print (applbip1)
  print (appwebip1)
  print (appwebip2)
 munchkinpublicip1 = doc["MLM"]["munchkin"]["public1"]["ip"]
 munchkinlbip1 = doc["MLM"]["munchkin"]["lb1"]["ip"]
 munchkinwebip1 = doc["MLM"]["munchkin"]["web1"]["ip"]
 munchkinwebip2 = doc["MLM"]["munchkin"]["web2"]["ip"]
 if debug :
  print ("munchkin ===========")
  print (munchkinpublicip1)
  print (munchkinlbip1)
  print (munchkinwebip1)
  print (munchkinwebip2)
 mdpublicip1 = doc["MLM"]["mktodesigner"]["public1"]["ip"]
 mdlbip1 = doc["MLM"]["mktodesigner"]["lb1"]["ip"]
 mdwebip1 = doc["MLM"]["mktodesigner"]["web1"]["ip"]
 mdwebip2 = doc["MLM"]["mktodesigner"]["web2"]["ip"]
 if debug :
  print ("md ==================")
  print (mdpublicip1)
  print (mdlbip1)
  print (mdwebip1)
  print (mdwebip2)
 mktoapipublicip1 = doc["MLM"]["mktoapi"]["public1"]["ip"]
 mktoapilbip1 = doc["MLM"]["mktoapi"]["lb1"]["ip"]
 mktoapiwebip1 = doc["MLM"]["mktoapi"]["web1"]["ip"]
 mktoapiwebip2 = doc["MLM"]["mktoapi"]["web2"]["ip"]
 if debug :
  print ("mktoapi===============")
  print (mktoapipublicip1)
  print (mktoapilbip1)
  print (mktoapiwebip1)
  print (mktoapiwebip2)
f.close()

replacements = {
          '#pod#':podname, 
          '#podappweb1#':appwebip1, '#podappweb2#':appwebip2,'#podapplb1#':applbip1,
          '#podmchweb1#':munchkinwebip1, '#podmchweb2#':munchkinwebip2, '#podmchlb1#':munchkinlbip1, 
          '#podmdweb1#':mdwebip1, '#podmdweb2#':mdwebip2, '#podmdlb1#':mdlbip1, 
          '#podmktoapilb1#':mktoapilbip1, 
          '#podapppublicip1#':apppublicip1, 
          '#podmunchkinpublicip1#':munchkinpublicip1, 
          '#podmdpublicip1#':mdpublicip1, 
          '#podmktoapipublicip1#':mktoapipublicip1 }


with open('MLM.lb') as infile, open('MLM-out.txt', 'w') as outfile:
 for line in infile:
    for src, target in replacements.items():
      line = line.replace(src, target)
    outfile.write(line)

if podname.startswith('ab'):
  with open('MLM-ab.fw') as infile, open('MLM-out.fw', 'w') as outfile:
   for line in infile:
    for a, b in replacements.items():
      line = line.replace(a, b)
    outfile.write(line)
elif podname.startswith('sj'):
  with open('MLM-sj.fw') as infile, open('MLM-out.fw', 'w') as outfile:
   for line in infile:
    for a,b in replacements.items():
      line = line.replace(a,b)
    outfile.write(line)
   
print  ("output file: MLM-out.txt for LB and MLM-out.fw for firewall")

