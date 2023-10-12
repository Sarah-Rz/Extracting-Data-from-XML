# Using Python and urllib to extract Data from XML.
# read the XML data from that URL (http://py4e-data.dr-chuck.net/comments_1862742.xml) using urllib and then parse and extract the comment counts from the XML data,
# compute the sum of the numbers in the file and enter the sum.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter -')
xml = urllib.request.urlopen(url).read()

tags = ET.fromstring(xml)
comments = tags.findall('comments/comment')

sum = 0
for comment in comments:
    count = comment.find('count').text
    sum = sum + float(count)
print('Sum:', sum)
