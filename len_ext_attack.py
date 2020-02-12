import sys
from urllib.parse import quote
from codecs import decode
from pymd5 import md5, padding

PASSWORD_LENGTH = 8
NEW_MESSAGE = "&action2=unlock-all-safes&customer="#&user=admin&action1=unlock-all-safes

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
			token = get_token[1]
			message = split_address[1]
			length_of_m = PASSWORD_LENGTH + len(message)
			bits = (length_of_m + len(padding(length_of_m * 8))) * 8
			h = md5(state = decode(token, "hex"), count = bits)
			h.update(NEW_MESSAGE)
			new_address += h.hexdigest() + "&" + message + quote(padding(length_of_m * 8)) + NEW_MESSAGE
			# new_address = new_address.encode() + padding(length_of_m * 8) + NEW_MESSAGE.encode()
			print(new_address)
			# print(get_token[0] + new_token + message + new_message)
			# # answer = m.encode() + padding(len(m) * 8) + x.encode()
			# # print(answer)

if __name__ == '__main__':
	main()