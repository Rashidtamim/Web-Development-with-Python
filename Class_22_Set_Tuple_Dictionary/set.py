#Create a set of 5 fruits and print it.

# berry = {'peach','blueberry','plum','raspberry','pear','fig'}
# for i in berry:
#     print(i)




#Check if an item exists in a set.


# berry = {'peach','blueberry','plum','raspberry','pear','fig'}
# print("peach" in berry)

#Add and remove items from a set.

'''berry = {'peach','blueberry','plum','raspberry','pear','fig'}
berry.add('kiwi')
print(berry)
berry.update(['lichi','melon'])
print(berry)
#berry.remove('peache')
berry.discard('peach')
print(berry)'''



#Remove duplicates from a list using a set.

'''berry = ['peach','blueberry','plum','raspberry','pear','peach','fig']
berry1=set(berry)
print(berry1)

'''

#Find union, intersection, and difference of two sets.


'''set1={1, 2, 3, 4, 5}
set2= {4, 5, 6}

print(set1.union(set2))        
print(set1.intersection(set2))  
print(set1.difference(set2)) '''


#Loop through a set and print each item.


'''berry = {'peach','blueberry','plum','raspberry','pear','fig'}
for i in berry:
    print(i)'''


#Find items present in one set but not in another using symmetric_difference().
#Jegulo set1 set2 te ache oigula bad dibo symmetric_difference diye 
set1={1, 2, 3, 4, 5}
set2={4, 5, 6, 7}


#difference = set1.symmetric_difference(set2)
difference=set2.symmetric_difference(set1)
print(difference)









#Copy a set and modify the copy without changing the original.


'''real_set= {10, 20, 30, 40}

copy_set= real_set.copy()

copy_set.add(50)
copy_set.remove(20)

print(real_set) 
print(copy_set)   '''   














