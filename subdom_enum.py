#! /usr/bin/env python3

#import the modules
import requests
import sys

#Assigning varible with file content
subdomain_list = open("subdomains.txt").read()
#Assigning varible with 
subdomains = subdomain_list.splitlines()
print(subdomain_list)
