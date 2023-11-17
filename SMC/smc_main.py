import sys
import read_file
import generate

if len(sys.argv) < 2:
    print("Usage: python main.py <file_path> ")
    sys.exit(1)

file_path = sys.argv[1]

visual_bridge_info, generic_object_list, _, _ = read_file.read_object_file(file_path)
class_generate = generate.generate_helper(generic_object_list, visual_bridge_info)
result_list = class_generate.smc_process()

for obj in result_list.procedural_objects:
    print("pos:", obj.position, "type:", obj.type, "size:", obj.length)