    
import json

def write_proceudral_objects (dummy_object, file_name = './three/reconstruct.json'):
    result = []

    for obj in dummy_object:
        pos = list(obj.position)
        data = {'obj':
            {
            'start_x': float(obj.position[0]),
            'start_y': float(obj.position[1]),
            'start_z': float(obj.position[2]),
            'scale_x': float(obj.scope[0]),
            'scale_y': float(obj.scope[1]),
            'scale_z': float(obj.scope[2])
            }
        }
        result.append(data)

    with open(file_name, 'w') as f:
        json.dump(result, f, indent=2)
