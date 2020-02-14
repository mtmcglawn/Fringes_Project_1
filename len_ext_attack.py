import sys
from urllib.parse import quote
from codecs import decode
from pymd5 import md5, padding

PASSWORD_LENGTH = 8
NEW_MESSAGE = "&action2=unlock-all-safes&customer="

def main():
	if len(sys.argv) < 2:
		print("There were no URL's entered as a command line argument")
	else:
		for i in range(1,len(sys.argv)):
			address = sys.argv[i]
			new_address = ""
			split_address = address.split("&", 1)
			#Splits directly after the token
			get_token = split_address[0].split("=")
			#Splits directly before the token
			new_address += get_token[0] + "="
			#Gets the token
			token = get_token[1]
			#Gets the message behind the token
			message = split_address[1]
			#Calculates the length of the message to mimic
			length_of_m = PASSWORD_LENGTH + len(message)
			print(str(length_of_m))
			#Calculates the bits of message
			bits = (length_of_m + len(padding(length_of_m * 8))) * 8
			#"Preps" the md5 algorigthm
			h = md5(state = decode(token, "hex"), count = bits)
			#Hashes the message to be appended with the old message
			h.update(NEW_MESSAGE)
			#Creates the new URL with the binary padding
			new_address += h.hexdigest() + "&" + message + quote(padding(length_of_m * 8)) + NEW_MESSAGE
			print(new_address)

if __name__ == '__main__':
	main()