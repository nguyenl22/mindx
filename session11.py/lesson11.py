# Dictionary: including pairs of keys and corresponding values
# myFavourtie={
#     key:value,
#     key:value
# }
# create:
information = {
    "do_kho": ["snack", 'thit bo kho'],
    "dong_lanh": {
        "do_song": [],
        "do_chet": "ugh"
    },
    "is_open": True,
    "gia_dung": "chao ran"
}
# keys cannot include special symbols or spaces (etc:@#$) and must be in string.
# values can be of all data types.
print(information)

# read: retrieve value by key: print(dictionary["key"])
print(information["do_kho"])

# update:
information["dong_lanh"]["do_song"].append("ca map")
information["dong_lanh"]["do_chet"]="ca chep"
print(information["dong_lanh"]["do_song"],information["dong_lanh"]["do_chet"])

# add pair of key value in preexisting dictionary: dictionary.update(pair)
information.update("wow":True)

# delete: del dictionary["key"]
del information["is_open"]
print(information)

class_info = [
    {
        "name": "Nam Khanh",
        "age": 16,
        "sex": "Male"
    },
    {
        "name": "Linh",
        "age": 17,
        "sex": "Female"
    }

]
for item in class_info:
    if item["sex"]=="Female":
        print(item)



