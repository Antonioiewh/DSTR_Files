smal_index = 0
output_datalist = []

#test_list 
test_list = [8,5,7,6,2,2,0,-5,0,-8,9]
# NOTE: this will defer , smaller/largerc
# For each element in test_list , replace with the smallest SO FAR - will defer down the list as more elements are being compared
for i in range(len(test_list)):
    if test_list[smal_index] > test_list[i]:
        smal_index = i
    #test_list[i] = test_list[smal_index]
    output_datalist.append(test_list[smal_index])   

#print(test_list)
print(output_datalist) 