from controllers.TextController import TextController

text_controller: TextController = TextController()


def test_encrypt() -> None:
    assert text_controller.encrypt(1, "HELLO!") == "IFMMP!"
    assert text_controller.encrypt(2, "Hello World") == "Jgnnq Yqtnf"
    assert text_controller.encrypt(3, "Hello, World!") == "Khoor, Zruog!"
    assert text_controller.encrypt(4, "XYZ") == "BCD"


def test_decrypt() -> None:
    assert text_controller.decrypt("IFMMP!", 1) == "HELLO!"
    assert text_controller.decrypt("Jgnnq Yqtnf", 2) == "Hello World"
    assert text_controller.decrypt("Khoor, Zruog!", 3) == "Hello, World!"
    assert text_controller.decrypt("BCD", 4) == "XYZ"


def test_rotate() -> None:
    assert text_controller.rotate("A", 3) == "D"
    assert text_controller.rotate("a", 3) == "d"
    assert text_controller.rotate("Z", 1) == "A"
    assert text_controller.rotate("z", 1) == "a"
    assert text_controller.rotate("!", 1) == "!"
    assert text_controller.rotate(" ", 1) == " "
    assert text_controller.rotate("A", 26) == "A"
    assert text_controller.rotate("a", 26) == "a"
    assert text_controller.rotate("A", 27) == "B"
    assert text_controller.rotate("a", 27) == "b"


def test_derotate() -> None:
    assert text_controller.derotate("D", 3) == "A"
    assert text_controller.derotate("d", 3) == "a"
    assert text_controller.derotate("A", 1) == "Z"
    assert text_controller.derotate("a", 1) == "z"
    assert text_controller.derotate("!", 1) == "!"
    assert text_controller.derotate(" ", 1) == " "
    assert text_controller.derotate("A", 26) == "A"
    assert text_controller.derotate("a", 26) == "a"
    assert text_controller.derotate("A", 27) == "Z"
    assert text_controller.derotate("a", 27) == "z"
