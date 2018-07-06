import os,csv,re
from time import localtime, strftime

os.system("speedtest-cli > speedtest.txt")
results = open(r"speedtest.txt", "r").readlines()
print (results[6], results[8])

downloadSpeed = results[6].replace('Download: ', '').replace('\n','')
uploadSpeed = results[8].replace('Upload: ', '').replace('\n','')

with open('internetspeed.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    time = strftime("%d %b %Y %H:%M:%S", localtime())
    writer.writerow([time, downloadSpeed, uploadSpeed])

os.system("DEL speedtest.txt")
print("Recorded internet Speed")
