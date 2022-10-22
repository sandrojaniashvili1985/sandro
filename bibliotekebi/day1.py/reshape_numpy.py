def flattening_arr(arr):
    final_arr = []
    for i in arr:
       for i1 in i:
           for i2 in i1:
            final_arr.append(i2)
    return final_arr


arr = [[[1,2,3], [4,5,6]], [[8,9,10], [11,12,13]]]
print(flattening_arr(arr))