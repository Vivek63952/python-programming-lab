# PROGRAM TO FLATTEN THE NESTED A LIST
lst = [[1], [2, 3], [4, 5, 6, 7]]

flat_lst = []
for sublist in lst:
    for num in sublist:
        flat_lst.append(num)

print(flat_lst)
