#list menjadi set
data_list = [3,5,7,9,2,3,4,6,5,7,8,9,1,1,2,5,5]
print("Data sebelum dikonversi: ", data_list)
data_set = set(data_list)
print('Data sesudah dikonversi: ', data_set)
print()

#set menjadi list
data_sett = {4,7,6,3,4,2,8,9,1,2,5,6,7,4,3,8,9}
print("Data sebelum dikonversi: ", data_sett)
data_list = list(data_set)
print("Data sesudah dikonversi: ", data_list)
print()

#set menjadi tuple
dataa_sett = {5,2,4,7,9,3,1,6,8,3,5}
print("Data sebelum dikonversi: ", data_sett)
data_tuple = tuple(data_sett)
print("Data sesudah dikonversi: ", data_tuple)
print()