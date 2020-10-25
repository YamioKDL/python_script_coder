import os
import ctypes
import time
try:
	kernel32 = ctypes.windll.kernel32
	kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
except:
	pass

start = True
BASE_DIR = os.getcwd()

def crypt_de(message, key):
	text = ''
	for i in message:
		text += chr(ord(i) ^ key)
	return text

def ls():
	files = os.listdir(BASE_DIR)
	text = "\n"
	for file in files:
		text += f"{file}\n"
	return text

def coder(file, key):
	coder = open(file, "r", encoding='utf-8')
	code = open(f'{file}{int(time.time())}.txt', 'w+', encoding='utf-8')
	new_code = crypt_de(coder.read(), key)
	code.write(new_code)
	coder.close(); code.close()
	print("Done..")

print('''\033[34m
 , __           _                                                                           
/|/  \         | |                     ()            o                         |            
 |___/     _|_ | |     __   _  _       /\  __   ,_        _ _|_    __   __   __|   _   ,_   
 |    |   | |  |/ \   /  \_/ |/ |     /  \/    /  |  |  |/ \_|    /    /  \_/  |  |/  /  |  
 |     \_/|/|_/|   |_/\__/   |  |_/  /(__/\___/   |_/|_/|__/ |_/  \___/\__/ \_/|_/|__/   |_/
         /|                                            /|                                   
         \|                                            \|                                   
\033[0m''')
print("More info: help")

while start:
	try:
		command = str(input("PSC> ")).lower()
		if command == 'ls':
			print(ls())
		elif command == 'help':
			print("\nCommands:\nhelp - more info\nls - file in directory\ncoder - coder python script\nstart - start coder python script\n")
		elif command == 'coder':
			while True:
				file_name = str(input("PSC: enter a file name> "))
				files = ls().split()
				if file_name not in files:
					print("Not found..")
				else:
					while True:
						try:
							key = int(input("PSC: enter a numeric code> "))
							coder(file_name, key)
							break
						except Exception as ex:
							print(ex)
							print("Please enter a numeric code!")
					break
		elif command == 'start':
			while True:
				file_name = str(input("PSC: enter a file name> "))
				files = ls().split()
				if file_name not in files:
					print("Not found..")
				else:
					while True:
						try:
							key = int(input("PSC: enter a numeric code> "))
							coder = open(file_name, "r", encoding='utf-8')
							code = crypt_de(coder.read(), key)
							coder.close()
							try:
								exec(code)
							except Exception as ex:
								print(ex)
								print("closed file..")
							break
						except Exception as ex:
							print(ex)
							break
					break
		elif command == 'decoder':
			while True:
				file_name = str(input("PSC: enter a file name> "))
				files = ls().split()
				if file_name not in files:
					print("Not found..")
				else:
					while True:
						try:
							key = int(input("PSC: enter a numeric code> "))
							decoder = open(file_name, "r", encoding='utf-8')
							code = crypt_de(decoder.read(), key)
							decode = open(f'decode_{file_name}', 'w+', encoding='utf-8')
							decode.write(code)
							decoder.close()
							decode.close()
							print("done")
							break
						except Exception as ex:
							print(ex)
							break
	except:
		print("Goodbye")
		start = False