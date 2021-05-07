def encrypt(s, n):
  return ''.join(chr((ord(char) - 97 + n) % 26 + 97) for char in s)

def decrypt(s, n):
  return ''.join(chr((ord(char) - 97 - n) % 26 + 97) for char in s)
action = input('Would you like to encrypt or decrypt a message?: ')

num = 0

while num == 0:
  if action == 'decrypt':
    msg = input('enter message to be decrpyted: ')
    key = input('enter the shifting key: ')
    print(decrypt(str(msg), int(key)))
    num += 1
    break

  if action == 'encrypt':
    msg = input('enter message to be encrypted: ')
    key = input('enter the shifting key: ')
    print(encrypt(str(msg), int(key)))
    num += 1
    break
    
  else:
    print('action failed')



