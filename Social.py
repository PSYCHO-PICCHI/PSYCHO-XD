import os, sys
try:
    __import__("hacking").chk()
except Exception as e:
    exit(str(e))     
