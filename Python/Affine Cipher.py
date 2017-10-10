import random


# Check Greatest Common Denominator
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Check co prime
def coprime(a, b):
    return gcd(a, b) == 1


# Modular inverse
def modinv(A, N=26):
    #
    #  √ Constantly changing number and this whole expression must divide evenly
    # (i * N)+1
    # ----------
    #     A

    i = 1
    while ((i * N)+1)%A != 0:
        i += 1

    return int(((i * N)+1)/A)


class Affine:
    def __init__(self, keys=True):
        # Never changing
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.n = len(self.alphabet)
        # Incase keys are wanted to be submitted manually for encryption
        if keys:
            self.create_keys()

    def create_keys(self):
        # Creating options
        self.A = [i for i in range(self.n) if coprime(i, self.n) and i != 1]  #  Lists all the coprimes in a list
        self.B = [i for i in range(1, self.n)]  # All numbers up to n-1
        # Choosing actual values
        self.a = random.choice(self.A)
        self.b = random.choice(self.B)
        self.aprime = modinv(self.a)

    def encrypt(self, a, b, message):
        message = message.upper()
        encrypted = []
        for letter in message:
            if letter in self.alphabet:
                # Ex = (Ax + B) % 26
                # Then immediately converting to letter
                encrypted.append(self.alphabet[(((a * self.alphabet.index(letter)) + b) % self.n)])
            else:
                encrypted.append(letter)
        return ''.join(encrypted)

    def decrypt(self, aprime, b, message, brute=False):
        message = message.upper()
        if not brute == True:
            decrypted = []
            for letter in message:
                if letter in self.alphabet:
                    # Ex = aprime(x - B) % 26
                    # Then immediately converting to letter
                    decrypted.append(self.alphabet[((aprime * (self.alphabet.index(letter) - b)) % self.n)])
                else:
                    decrypted.append(letter)
            return ''.join(decrypted)

        elif brute == True:
            for a2 in self.A:
                for b2 in self.B:
                    decrypted = []
                    for letter in message:
                        if letter in self.alphabet:
                            # Ex = aprime(x - B) % 26
                            # Then immediately converting to letter
                            decrypted.append(self.alphabet[((modinv(a2) * (self.alphabet.index(letter) - b2)) % self.n)])
                        else:
                            decrypted.append(letter)
                    print("A:%s B:%s\n%s\n" % (a2, b2, ''.join(decrypted)))

    def plain_text(self, p1, p2, d1, d2):
        # RETURNS THE A AND B VALUE -- DECRYPT SEPERATELY
        # P1 and P2 are encrypted
        # D1 and D2 are the decrypted versions
        p1 = p1.upper()
        p2 = p2.upper()
        d1 = d1.upper()
        d2 = d2.upper()
        p1 = self.alphabet.index(p1)  # y1
        p2 = self.alphabet.index(p2)  # y2
        d1 = self.alphabet.index(d1)  # x1
        d2 = self.alphabet.index(d2)  # x2
        # y1 = A*x1 + B
        # y2 = A*x2 + B
        # y1-y2 = (Ax1)-(Ax2)
        p3 = p1-p2
        p3 = p3 % self.n  # As negatives or over the mod ruin everything
        d3 = d1-d2
        d3 = d3 % self.n  # As negatives or over the mod ruin everything

        # Subtracted value
        # A = (y1-y2) / (x1-x2)
        # A = (y1-y2) * (x1-x2)^-1
        # A = p3 * modularInverse(d3) % 26
        A = (p3 * modinv(d3)) % 26  # Finds A value
        # y1 = A1*x1 + B
        # B = y1 - A*x1
        B = p1 - (A*d1) % 26

        # y = A*x + B
        return A, B

if __name__ == "__main__":

    while True:
        cipher = Affine()
        try:
            type = input("What would you like to do:\n<1> Encrypt\n<2> Decrypt\n<3> Plain Text Attack\n")

            if type == '1':
                msg = input("What would you like to encrypt?\nTIP: Punctuation will not be changed\n")
                encrypted = cipher.encrypt(cipher.a, cipher.b, msg)

                print("A value: %s\nB value: %s\nEncrypted message:\n%s" % (cipher.a, cipher.b, encrypted))

            elif type == '2':
                brute = input("Would you like to bruteforce the 300+ possibilities?\n<y>   ||   <n>\n")
                if brute.lower() == 'n':
                    msg = input("What would you like to decrypt?\nTIP: Punctuation will not be changed\n")
                    a = int(input("What was the A value given: "))
                    while not isinstance(a, int):
                        print("Please enter only whole numbers.\n\n")
                        a = int(input("What was the A value given: "))
                    print()

                    b = int(input("What was the B value given: "))
                    while not isinstance(b, int):
                        print("Please enter only whole numbers.\n\n")
                        b = int(input("What was the B value given: "))
                    print()

                    aprime = modinv(a)
                    decrypted = cipher.decrypt(aprime, b, msg)

                    print("The decrypted message:\n%s" % (decrypted))
                elif brute.lower() == 'y':
                    msg = input("What would you like to decrypt?\nTIP: Punctuation will not be changed\n")
                    cipher.decrypt(1,1,msg,brute=True)

            elif type == '3':
                e1 = input("Letter which is encrypted: ")
                d1 = input("The decrypted version: ")
                e2 = input("2nd letter which is encrypted: ")
                d2 = input("The decrypted version: ")

                msg = input("What was the encrypted message?\nTIP: Punctuation will not be changed\n")

                A, B = cipher.plain_text(e1, e2, d1, d2)
                decrypted = cipher.decrypt(modinv(A), B, msg)
                print(decrypted)

        except Exception as e:
            print("Oops! Something went wrong... Re-Running\n\n")
            print(e)

