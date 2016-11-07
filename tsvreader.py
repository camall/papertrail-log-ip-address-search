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

def get_lines_with_ips_from_country(read_file, read_params):
    with open(read_file,read_params) as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        
        for row in tsvin:
            yield tsvin.line_num, row
    
def write_lines_to_new_file(write_file, write_params, read_file, read_params, country):
    with open(write_file, write_params) as csvout:
        csvout = csv.writer(csvout)
        for line_num,row in get_lines_with_ips_from_country(read_file, read_params):
            row_splitted = row[9].split(' ')
            for split in row_splitted:
                if valid_ip(split) and len(split) > 5:
                    if find_country(split) == country: 
                        csvout.writerow([line_num, row[9]])

write_lines_to_new_file('united-kingdom-10-27.csv', 'wb', '2016-10-27.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-10-28.csv', 'wb', '2016-10-28.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-10-29.csv', 'wb', '2016-10-29.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-10-30.csv', 'wb', '2016-10-30.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-10-31.csv', 'wb', '2016-10-31.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-11-01.csv', 'wb', '2016-11-01.tsv', 'rb', 'United Kingdom')
write_lines_to_new_file('united-kingdom-11-02.csv', 'wb', '2016-11-02.tsv', 'rb', 'United Kingdom')
