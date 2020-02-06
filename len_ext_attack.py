import sys
import urllib
from codecs import decode
from pymd5 import md5, padding

def main():
	if len(sys.argv) < 2:
		print("There were no URL's entered as a command line argument")
	else:
		for i in range(1,len(sys.argv)):
			address = sys.argv[i]
			split_address = address.split("=", 2)
			get_token = split_address[1].split("&")
			m = get_token[0]
			print(m)
			length_of_m = 8
			bits = (length_of_m + len(padding(length_of_m * 8))) * 8
			h = md5(state = decode(m, "hex"), count = bits)
			x = "Good advice"
			h.update(x)
			print(decode(m, "hex"))
			#print(h.hexdigest())
			answer = m.encode() + padding(length_of_m * 8) + x.encode()
			#print(answer)

if __name__ == '__main__':
	main()