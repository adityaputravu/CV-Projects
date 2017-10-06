class Caesar:

    def __init__(self, n=6):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.n = n

    def encrypt(self, text):
        a = []
        for i in text:

            if i in self.alphabet:
                #  Caesar cipher ting
                a.append(self.alphabet[self.alphabet.index(self.alphabet[(self.alphabet.index(i) + 1 + self.n - 1) % 26])])
            else:
                a.append(i)

        return ''.join(a)

    def decrypt(self, text):

        b = []

        for i in text:
            if i in self.alphabet:
                #  Caesar cipher ting
                b.append(self.alphabet[self.alphabet.index(self.alphabet[(self.alphabet.index(i) + 1 - self.n - 1) % 26])])
            else:
                b.append(i)

        return ''.join(b)

if __name__ == '__main__':
    from random import randint

    while True:
        try:
            type = input("What would you like to do:\n<1> Encrypt\n<2> Decrypt\n")

            if type == '1':
                specify = input("Would you like to specify the key?\n<y> || <n>\n")
                if specify.lower() == 'y':
                    while True:
                        try:
                            key = int(input('Please enter a key between 1 and 25: '))
                            break
                        except Exception:
                            print("Please enter only numbers\n")
                else:
                    key = randint(4, 19)

                cipher = Caesar(n=key)

                message = input("What would you like to encrypt?\nTIP: Only letters are going to be encrypted.\n").upper()

                encrypted = cipher.encrypt(message)

                print("The new message: \n%s\nKey: %d\n" % (encrypted, key))

            elif type == '2':

                message = input("What would you like to decrypt?\nTIP: Enter as is given please...\n")
                while True:
                    try:
                        key = int(input("Enter key: "))
                        break
                    except Exception:
                        print("Enter numbers only\n")

                cipher = Caesar(n=key)
                decrypted = cipher.decrypt(message)

                print("*************************************************"
                      "\nThe original message was:\n\n"
                      "%s\n"
                      "*************************************************\n"
                      "TIP: If this isn't right try mess around with the key"
                      " (THIS ONLY WORKS WITH CAESAR CIPHERS)\n" % decrypted)


            ask = input("Is that it?\n<y> || <n>\n")
            if ask.lower() == 'y':
                break
            elif ask.lower() != 'n':
                print("Sorry I didn't understand. I am re-running anyway!")
        except Exception as e:
            print("OOPS!\nSomething went wrong... :/\n"+str(e))

