#random key generator
import random
new_key = ""
new_key_list = []
string = "abcdefghijklmnopqrstuvwxyz"
for i in string:
  new_key_list.append(i)

new_key_list = random.sample(new_key_list, len(new_key_list))
new_key = new_key.join(new_key_list)
print("Current Decryption Key :" + new_key)
#converting key to bytes
new_key = bytes(new_key, 'utf-8')

#encryption key
encryption_key = b"abcdefghijklmnopqrstuvwxyz"
#decryption key
dcryption_key = new_key
#encryption table mapping
encryption_table = bytes.maketrans(encryption_key, dcryption_key)
#decryption key mapping
decryption_table = bytes.maketrans(dcryption_key, encryption_key)


#function to decrpt with a specific key value
def decrypt(dk, m):
    encryption_key = b"abcdefghijklmnopqrstuvwxyz"
    decrytion_key = dk
    encrytion_table = bytes.maketrans(encryption_key, decrytion_key)

    decryption_table = bytes.maketrans(decrytion_key, encryption_key)
    r = m.translate(decryption_table)

    return r


#initilized Vars:

c = ''
r = ''
m = ''
dk = ''

#main driver code

while c != '0':
    c = input(
        "Do you want to encrypt or decrypt the message: \n 1 to encrypt \n 2 to decrypt \n 3 to decrypt with a key \n Q to Quit \n >>"
    )
    if c == "1":
        m = input("Enter encryption Message: ")
        r = m.translate(encryption_table)
        print("\nEncryption For Given Message: " + r + "\n" + " \n" +
              "Decryption KEY = " + str(new_key) + "\n\n")
    elif c == "2":
        m = input("Enter Decryption message: ")
        r = m.translate(decryption_table)
        print(r + "\n\n")
    elif c == "3":
        m = input("Enter Decrytion Message: ")
        dk = input("Enter Decryption Key: ")
        r = decrypt(bytes(dk, 'utf-8'), m)
        print("Decrpted message with given Key: " + dk + "\n" + r + "\n\n")
    elif c == "Q" or "q":
        exit()
    else:
        print("Invalid Input please try again ")
