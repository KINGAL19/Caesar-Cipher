alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
	shift_text = ""
	for letter in plain_text:
		position = alphabet.index(letter)
		new_position = position + shift_amount
		new_position = new_position % 26
		shift_text += alphabet[new_position]
	return shift_text

def decrypt(shift_text, shift_amount):
	shift_back_text = ""
	for letter in shift_text:
		position = alphabet.index(letter)
		new_position = position - shift_amount + 26
		new_position = new_position % 26
		shift_back_text += alphabet[new_position]
	return shift_back_text
def main():
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	if direction == "encode":
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
		shift_text = encrypt(text, shift)
		print(f"The encoded text is ( {shift_text} )")
	elif direction == "decode":
		text = input("Type your message:\n").lower()
		shift = int(input("Type the shift number:\n"))
		shift_back_text = decrypt(text, shift)
		print(f"The encoded text is ( {shift_back_text} )")	
	else:
		print("make sure your direction")
main()