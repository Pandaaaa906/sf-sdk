from random import choice
from string import digits, ascii_letters


def generate_digits(length=8):
    """
    指定长度的纯数字
    """
    return ''.join(choice(digits) for _ in range(length))


def generate(length=8):
    """
    产出指定长度的随机字符串
    """
    return ''.join([choice(ascii_letters + digits) for _ in range(length)])
