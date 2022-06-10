import sys

from zipfile import ZipFile

from io import BytesIO


inp = bytes.fromhex(sys.stdin.read())
zipper = ZipFile(BytesIO(inp), 'r')
list_zipper = zipper.infolist()
counter, volume = 0, 0
i = 0
leng = len(list_zipper)
while i < leng:
    if not list_zipper[i].is_dir():
        volume += list_zipper[i].file_size
        counter += 1
    i += 1
print(counter, volume)
