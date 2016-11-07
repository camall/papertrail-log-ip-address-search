import csv
#!/usr/bin/env python 
from urllib2 import urlopen
from contextlib import closing
import json
import socket
    
def find_country(ip_address):
    url = 'https://freegeoip.net/json/'+ip_address
    try:
        with closing(urlopen(url)) as response:
            location = json.loads(response.read())
            return location['country_name']
    except:
        print("Location could not be determined automatically")

def valid_ip(address):
    try: 
        socket.inet_aton(address)
        return True
    except:
        return False

def get_lines_with_ips_from_country(read_file, read_params, write_file, write_params, country)
    with open(read_file,'rb') as tsvin, open(write_file, 'wb') as csvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        csvout = csv.writer(csvout)
        
        for row in tsvin:
            row_splitted = row[9].split(' ')
            for split in row_splitted:
                if valid_ip(split) and len(split) > 5:
                 if find_country(split) == country: 
                    csvout.writerow([tsvin.line_num, row[9]])

dates = ['10-27','10-28','10-29','10-30','10-31','11-01','11-02']

get_lines_with_ips_from_uk('2016-10-27.tsv', 'rb', 'united-kingdom-10-27.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-10-28.tsv', 'rb', 'united-kingdom-10-28.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-10-29.tsv', 'rb', 'united-kingdom-10-29.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-10-30.tsv', 'rb', 'united-kingdom-10-30.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-10-31.tsv', 'rb', 'united-kingdom-10-31.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-11-01.tsv', 'rb', 'united-kingdom-11-01.csv', 'wb', 'United Kingdom')
get_lines_with_ips_from_uk('2016-11-02.tsv', 'rb', 'united-kingdom-11-02.csv', 'wb', 'United Kingdom')
