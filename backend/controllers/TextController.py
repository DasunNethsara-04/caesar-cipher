class TextController:
    '''
    TextController class is a class that handles the encryption and decryption of text using the Caesar Cipher algorithm.
    '''

    def __init__(self) -> None:
        pass

    def encrypt(self, key: int, text: str) -> str:
        '''
        Encrypts the given text using the Caesar Cipher algorithm.
        >>> text_controller = TextController()
        >>> text_controller.encrypt(3, "Hello, World!")
        'Khoor, Zruog!'
        '''
        cipher_text: str = ""
        for char in text:
            rotated: str = self.rotate(char, key)
            cipher_text += rotated
        return cipher_text

    def decrypt(self, text: str, key: int) -> str:
        '''
        Decrypts the given text using the Caesar Cipher algorithm.
        >>> text_controller = TextController()
        >>> text_controller.decrypt("Khoor, Zruog!", 3)
        'Hello, World!'
        '''
        plain_text: str = ""
        for char in text:
            derotated: str = self.derotate(char, key)
            plain_text += derotated
        return plain_text

    def rotate(self, char: str, shift: int) -> str:
        '''
        Rotates the given character by the given shift.
        >>> text_controller = TextController()
        >>> text_controller.rotate("A", 3)
        'D'
        '''
        # c = (p + k) % 26
        #       p -> character
        #       k -> position / shift
        rotated: str | None = None
        if (not char.isalpha()):
            rotated = char
        else:
            # check if the character if upper or lower
            if char.isupper():
                rotated_digit: int = (ord(char) - 65 + shift) % 26
                rotated = chr(rotated_digit + 65)
            elif char.islower():
                rotated_digit: int = (ord(char) - 97 + shift) % 26
                rotated = chr(rotated_digit + 97)
        return rotated

    def derotate(self, char: str, shift: int) -> str:
        '''
        Derotates the given character by the given shift.
        >>> text_controller = TextController()
        >>> text_controller.derotate("D", 3)
        'A'
        '''
        derotated: str | None = None
        if not char.isalpha():
            derotated = char
        else:
            if char.isupper():
                derotated_digit: int = (ord(char) - 65 - shift) % 26
                derotated = chr(derotated_digit + 65)
            elif char.islower():
                derotated_digit: int = (ord(char) - 97 - shift) % 26
                derotated = chr(derotated_digit + 97)
        return derotated
