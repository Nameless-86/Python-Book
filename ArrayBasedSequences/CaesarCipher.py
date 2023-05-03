class CaesarCipher():
    def __init__(self, shift) -> None:
        """Construct caesar cipher using given integer shift for rotation"""
        encoder = [None] * 26  # Temp array for encryption
        decoder = [None] * 26  # Temp array for decryption
        for k in range(26):
            encoder[k] = chr(((k+shift) % 26) + ord('A'))
            decoder[k] = chr(((k-shift) % 26) + ord('A'))

        self._forward = "".join(encoder)  # Will store as string
        self._backward = "".join(decoder)  # since fixed

    def encrypt(self, message):
        """Return string reperesenting encrypted message"""
        return self._transform(message, self._forward)

    def decrypt(self, message):
        """Return string reperesenting decrypted message"""
        return self._transform(message, self._backward)

    def _transform(self, original, code):
        """utility to perform transformation based on given code string"""
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # Index ' to 25
                msg[k] = code[j] # Replace this character
        return "".join(msg)



if __name__ == '__main__':
    cypher = CaesarCipher(3)
    message = "THIS SHIT ONLY WORKS IN UPPERCASE"
    coded = cypher.encrypt(message)
    print("Secret: ", coded)
    answer = cypher.decrypt(coded)
    print("Decoded: ", answer)