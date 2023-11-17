import sys
import read_file

if len(sys.argv) < 2:
    print("Usage: python main.py <file_path> ")
    sys.exit(1)

file_path = sys.argv[1]

_, generic_object_list, _, _ = read_file.read_object_file(file_path)
