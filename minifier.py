import sys
import compressor

file = sys.argv[1]

try:
    extension = file.split('.')[1]
except IndexError:
    print('File without extension! please enter the complete file name.')
    exit(0)

compressor.compress(file)