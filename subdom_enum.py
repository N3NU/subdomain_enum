#! /usr/bin/env python3

#import the modules
import requests
import sys

#Assigning varible with file content
subdomain_list = open("subdomains.txt").read()
#Assigning varible with a list of lines from subdomain_list
subdomains = subdomain_list.splitlines()

#Iterating through the list of words in subdomains variable
for sub in subdomains:
    #Assigning the variable with FQDN
    new_subdomains = f"http://{sub}.{sys.argv[1]}"
    print(new_subdomains)
    #Check to see if new_subdomains give valid response
    try:
        requests.get(new_subdomains)

    #Except ConnectionError if it occurs
    except requests.ConnectionError:
        pass
    
    #If new_subdomains has valid response, print
    else:
        print("Valid domain: ",new_subdomains)