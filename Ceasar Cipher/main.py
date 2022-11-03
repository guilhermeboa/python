import art
import os

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift):
  result = ''
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      if direction == 'decode':
        new_position = position - shift
      elif direction == 'encode':
        new_position = position + shift
      result += alphabet[new_position]
    else:
      result += letter
  print(f"The {direction}d text is {result}")

print(art.logo)
caesar_run = 'yes'

while caesar_run == 'yes':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n")) % 26
  caesar(text, shift)
  caesar_run = input("Type 'yes' if you want to go again. Otherwise type 'no'")
  os.system('cls||clear')
