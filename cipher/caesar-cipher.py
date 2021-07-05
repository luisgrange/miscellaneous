import argparse


def encrypT(key):
	

	ascii_value = 0
	crypt = ''

	for letter in key:
		if ord(letter) >=120:
			ascii_value = ord(letter)-23
			crypt += chr(ascii_value)
		else:
			ascii_value = ord(letter)+3
			crypt += chr(ascii_value)

	return crypt

def decrypT(key):
	ascii_value = 0
	crypt_rev = ''

	for letter in key:
		if ord(letter) <=100:
			ascii_value = ord(letter)+23
			crypt_rev += chr(ascii_value)
		else:
			ascii_value = ord(letter)-3
			crypt_rev += chr(ascii_value)

	return crypt_rev
	

if __name__ == '__main__':

	parser = argparse.ArgumentParser()

	parser.add_argument("--encrypt", '-e', help="set output encrypt")
	parser.add_argument("--decrypt", '-d', help="set output decrypt")

	args = parser.parse_args()

	if args.encrypt:
		print(f"Encrypt: {encrypT(args.encrypt)}")

	elif args.decrypt:
		print(f"Decrypt: {decrypT(args.decrypt)}")
