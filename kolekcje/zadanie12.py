liczby = [9, 1, 6, 8, 4, 3, 2, 0]


for i in range(len(liczby)):
    mini = min(liczby[i:])             #find minimum element
    min_index = liczby[i:].index(mini) #find index of minimum element
    liczby[i + min_index] = liczby[i]  #replace element at min_index with first element
    liczby[i] = mini                   #replace first element with min element
print (liczby)


#assert liczby == [0, 1,  2, 3, 4, 6, 8, 9]