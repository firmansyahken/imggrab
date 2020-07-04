import json
import os, sys, shutil
import base64
import requests
def help():
	print """
help command tool
------------------------------------
help	: menampilkan help
clear	: clear
banner	: menampilkan banner
exit	: keluar
cd	: ganti directory
	  ex: cd /sdcard
ls	: list
upload	: upload gambar
	  ex: upload namafile.jpg
ch	: ganti token api
	  ex: ch 728dj929292sjiw
"""
def banner():
	os.system("clear")
	print """
.___               ___.  ___.
|   | _____    ____\_ |__\_ |__
|   |/     \  / ___\| __ \| __ \

|   |  Y Y  \/ /_/  > \_\ \ \_\ \

|___|__|_|  /\___  /|___  /___  /
          \//_____/     \/    \/
Author	: Wibucode
Github	: https://github.com/wibucode
ketik help untuk menampilkan bantuan
"""
banner()
def main():
	key = "58d46e23a3edecf448226741dc15224c"
	while True:
		cmd = raw_input("> command@->: ")
		if cmd == "help":
			help()
		elif cmd == "clear":
			os.system("clear")
		elif cmd == "exit":
			sys.exit()
		elif cmd == "banner":
			banner()
		elif cmd == "cd":
			print os.getcwd()
		elif "cd" in cmd:
			dir = cmd.split()[-1]
			os.chdir(dir)
			print os.getcwd()
		elif cmd == "ls":
			d = os.getcwd()
			l = os.listdir(d)
			for ls in l:
				print "> "+ls
		elif "ch" in cmd:
			key = cmd.split()[-1]
			print "> Token api berhasil diubah menjadi "+key
		elif "upload" in cmd:
			nama_file = cmd.split()[-1]
			with open(nama_file, "rb") as file:
				url = "https://api.imgbb.com/1/upload"
	    			payload = {
       					 "key": key,
       					 "image": base64.b64encode(file.read()),
   			 	}
    			res = requests.post(url, payload)
			data = res.json()
    			print "\033[91mLink gambar =>: "+"\033[96m", data['data']['url']
			print "\033[97m"
		else:
			print "> ketik help untuk menampilkan bantuan command"
try:
	main()
except KeyboardInterrupt:
	print "Ctrl + C (exit)"
except EOFError:
	print "Ctrl + Z (exit)"
