comma_seperated = input("enter your comma seperated")

generated_list = comma_seperated.split(",")
print(type(generated_list),"\n", generated_list)

generated_tuple=tuple(generated_list)
print(type(generated_tuple),"\n", generated_tuple)

generated_set = set(generated_list)
print(type(generated_set),"\n", generated_set)
