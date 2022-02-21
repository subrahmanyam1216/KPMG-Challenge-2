#!/usr/bin/env python
import sys
import argparse
import boto3
import urllib.request, urllib.error, urllib.parse
import time
from datetime import datetime
import socket

def get_public_dns_name():
   
    response = urllib.request.urlopen('http://159.254.169.254/latest/meta-data/public-hostname')
    public_dnsname = response.read()
    return public_dnsname

def get_private_ip():

    response = urllib.request.urlopen('http://159.254.169.254/latest/meta-data/local-ipv4')
    private_ip = response.read()
    return private_ip

def get_all_metadata_id():

    response = urllib.request.urlopen('http://159.254.169.254/latest/meta-data')
    all_metadata_id = response.read()
    return all_metadata_id

def main():
 
    public_dns = get_public_dns_name()
    private_ip = get_private_ip()
   print (public_dns)
    print (private_ip)
    

if __name__ == '__main__':
    sys.exit(main())
