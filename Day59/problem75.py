'''

Question:

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

'''
from zlib import compress,decompress 

str1 = b"hello world!hello world!hello world!hello world!"
cs = compress(str1)
ds = decompress(cs)

print(f'String {str1} \nCompressed {cs} \nDecompressed {ds}')

