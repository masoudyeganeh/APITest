import json
import generalMethods

# f = open('port_man_contract_14020929_1051841')
#
# data = json.load(f)
#
# c = generalMethods.count_keys(data)
#
# print(len(list(c)))
# # all_keys_list = list(dict.fromkeys(list(get_keys(data))))
# #
# # print(all_keys_list)
#
# f.close()


a = [[10,15,12], [12], [15,45], [45,12]]
b = [[10,17,12], [13], [15,46], [46,12]]
dif = []
for i in range(len(a)):
    x = list(set(a[i]) - set(b[i]))
    dif.append(x)
    print(x)
