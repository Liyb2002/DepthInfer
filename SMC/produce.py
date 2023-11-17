import generic_objects
import procedural_objects
import numpy as np

def execute_model(generic_object_list, start_obj, steps):
    production_list = []
    
    cur_obj = start_obj
    production_list.append(cur_obj)

    #processing
    count = 0
    not_end = True
    while(count < steps or not_end):

        tempt_count = count
        next_type = None

        while(tempt_count >= 0 and next_type == None):
            cur_obj = production_list[tempt_count]
            cur_type = production_list[tempt_count].type
            cur_generic_obj = generic_object_list[cur_type]
            next_type = cur_generic_obj.get_nextType(cur_obj.connected)
            tempt_count -=1

        if next_type == None:
            return []
        
        next_generic_obj = generic_object_list[next_type]
        next_scope = next_generic_obj.scope
        next_hash = next_generic_obj.generate_hash()
        next_rotation = next_generic_obj.rotation
        next_offset = cur_generic_obj.get_offset(next_type)
        next_obj = procedural_objects.Procedural_object(next_type, np.array([0,0,0]), next_scope, next_hash, next_rotation, next_offset)
        next_choice = cur_generic_obj.execute_rule(next_type)
        cur_obj.add_connected(next_choice)
        next_obj.add_connected(opposite_direction(next_choice))
        next_obj.set_position(cur_obj, next_choice)

        production_list.append(next_obj)
        cur_obj = next_obj

        if next_generic_obj.canTerminate == "False":
            not_end = True
        else:
            not_end = False
    
        count += 1
    production_list.pop(0)
    return production_list


def opposite_direction(direction):
    if direction == '+x':
        return '-x'
    if direction == '-x':
        return '+x'
    if direction == '+y':
        return '-y'
    if direction == '-y':
        return '+y'
    if direction == '+z':
        return '-z'
    if direction == '-z':
        return '+z'
    
    return '+x'