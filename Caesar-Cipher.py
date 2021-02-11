alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
  shift_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift
    new_position = new_position % 26
    shift_text += alphabet[new_position]
  return shift_text

  
shift_text = encrypt(text, shift)
print(f"The encoded text is ( {shift_text} )")