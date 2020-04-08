# program that counts the number of occurrences of each letter in a file

import pprint
import PyPDF2

pdfFile = open('Cisco Catalyst 9300 Series Switches.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdfFile)

count = {}

for pageNum in range(reader.numPages): # reader.numPages is total number of pages in PDF file
    m = reader.getPage(pageNum).extractText() # m is string of page 1, till last page in every iteration
    for char in m:
        count.setdefault(char, 0) #‘key’ part of dictionary is a string, when it first occurs, so that when it
                                  # does not have any value, we are setting it a zero. Next time when it appears,
                                  # we skip this line as it already has a value, and go to the counter in next line,
                                  # We are modifying dictionary count
        count[char] = count[char] + 1

pprint.pprint(count) # to display dictionary more clean