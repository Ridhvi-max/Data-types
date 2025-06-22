import array as arr
array_num=arr.array('i',[1,3,5,3,7,9,3])
print('Orignal array: '+str(array_num))
print("NUmber of occurrences of the number 3 is the said array: "+str(array_num))
array_num.reverse()
print("Reverse the oder of the items:")
print(str(array_num))