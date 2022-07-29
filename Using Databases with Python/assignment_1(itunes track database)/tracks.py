import xml.etree.ElementTree as ET      #API implementation for working with XML files in Python
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()
