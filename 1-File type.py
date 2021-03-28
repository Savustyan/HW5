import os
class NoExtension(Exception):
    pass
# 1-st variant without exception
for name in os.listdir(r'C:\Program Files\Git'):
    filename, file_extension = os.path.splitext(name)
    if file_extension:
        print(filename, 'has extention', file_extension)

# with exception
name = 'examplejpeg'
try:
    if '.' in name:
        print(name.split('.')[-1])
    else:
        raise NoExtension
except NoExtension:
    print('Cant determine the extension')
