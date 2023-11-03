import zipfile
import zlib

text = b'hello world, i am kunal!'
print('Original length:', len(text))

compressed_text = zlib.compress(text)
print('Length after compression:', len(compressed_text))
print(compressed_text)