
# 2. Dictionary editor

# Write replace_dict_value(d, bad_val, good_val), which returns a dictionary with changed values

# The parameters of the function are the dictionary d to be processed 
# and the values ​​bad_val to be changed to good_val

# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10},
# because 5 was the value to be replaced

def replace_dict_value(d, bad_val, good_val):
    new_dict = {}
    for key, value in d.items():
        if value != bad_val:
            new_dict[key] = value
        if value == bad_val:
            new_dict[key] = good_val
    return new_dict

print(replace_dict_value({'a': 5, 'b': 6, 'c': 5}, 5, 30)) 

# my_dict = {'a': 5, 'b': 6, 'c': 5, 'd':3, 'e': 5, 'f': 5, 'g':8}	
# new_dict = replace_dict_value(my_dict, 8)
# print(new_dict)
# print(my_dict)