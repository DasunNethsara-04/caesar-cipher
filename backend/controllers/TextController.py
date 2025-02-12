class TextController:

    def __init__(self) -> None:
        pass

    def encrypt(self, key: int, text: str) -> str:
        cipher_text: str = ""
        for char in text:
            rotated: str = self.rotate(char, key)
            cipher_text += rotated
        return cipher_text

    def decrypt(self, text: str, key: int) -> str:
        plain_text: str = ""
        for char in text:
            derotated: str = self.derotate(char, key)
            plain_text += derotated
        return plain_text

    def rotate(self, char: str, shift: int) -> str:
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
