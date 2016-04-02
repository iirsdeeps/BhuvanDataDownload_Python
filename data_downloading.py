#-------------------------------------------------------------------------------
# Name:        DataDownloading from Bhuvan
# Purpose:     Automated data download from open sources
#              The output is in KML format for:
#              asi:prohibited_boundary
# Author:      SHIKHAR
#
# Created:     19/03/2016
# Copyright:   (c) SHIKHAR 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import urllib2, sys

#-------------------------------------------------------------------------------
#configuration:
url = r'http://bhuvan5.nrsc.gov.in/bhuvan/wms?service=WMS&version=1.1.0&request=GetMap&layers=asi:prohibited_boundary&styles=&bbox=66.0,6.0,102.0,42.0&width=512&height=512&srs=EPSG:4326&format=application/vnd.google-earth.kml+xml'
output_file_path = r'D:/ahmedabad/' # output folder path
output_filename = 'data_1.kml'  # output file name
kml_file = output_file_path+output_filename
data_chunk = 1024*1024          # data chunk size to be downloaded at once

#-------------------------------------------------------------------------------


def main():
    response = urllib2.urlopen(url)  # opening the url
    with open(kml_file, "wb") as data: # creating/writing the desired output file
        try:
            #fetching the total size from the header
            total_size = response.info().getheader('Content-Length').strip()
            header = True
        except AttributeError:
            header = False # a response doesn't always include the "Content-Length" header
        data_bytes_so_far = 0 # Varibles defining the bytes downloaded at run time

        while True:
            chunk =  response.read(data_chunk) # reading the response
            if not chunk:
                sys.stdout.write('\n')
                break

            data_bytes_so_far += len(chunk) #getting the data size
            data.write(chunk) # writing the downloaded data into the kml file

            if not header:
                total_size = data_bytes_so_far # unknown size

            percent = float(data_bytes_so_far) / total_size
            percent = round(percent*100, 2)
            print("Downloaded %d of %d KB (%0.2f%%)\r" % (data_bytes_so_far/1000, total_size/1000, percent))


if __name__ == '__main__':
    main()
