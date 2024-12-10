immutable_var = 0, "апельсин", True, ["абрикос", "тыква", 8, False]
print(immutable_var)
#immutable_var[0] = 9
#immutable_var[1] = "банан"
#immutable_var[2] = False
immutable_var[3][0] = "банан"
print(immutable_var)
immutable_var[3][0] = 1
print(immutable_var)
mutable_list = [2,10,"кот",True]
print(mutable_list)
mutable_list[0] = False
mutable_list.append("собака")
mutable_list.remove("кот")
mutable_list.extend("птица")
mutable_list.extend(["птица", True, 555])
print(mutable_list)