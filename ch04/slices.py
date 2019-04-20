cubes_list=[num**3 for num in range(1,11)]
print(cubes_list)

print("The first three items in the list are:"+str(cubes_list[0:3]))
print("Three items from the middle of the list are:"+str(cubes_list[int(len(cubes_list)/2)-1:int(len(cubes_list)/2)+2]))
print("The last three items in the list are:"+str(cubes_list[-3:]))
