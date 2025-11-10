#list name = [item1,item2]
fruits=["apple", 'banana' , 'cherry']
print(fruits)
#find the item no 2 from fruits list
'''print(fruits[1])

numbers = [10 , 20 , 30 , 40 , 50]
mixed = [1 , 'hello' , 3.14 , True]

print(numbers[4])

print(mixed[-3])'''



#modify list elements
#fruits=["apple", 'banana' , 'cherry']
print(fruits)
fruits[1]='mango'
print(fruits)

num = [10 ,20 ,30 ,40 ,50]
print(num[:3])
print(num[-2])

num[-2:] = [60 ,70]
print(num)

#[10, 20, 30, 60, 70]
num[1:3] = [45, 56]
print(num)


#append
fruits.append("mango")
print(fruits)
fruits.append('lichi')
fruits.append('grapes')
print(fruits)


#insert

fruits.insert(1,"Guava")
print(fruits)


# fruits.remove("cherry")
# print(fruits)
# fruits.pop()
# print(fruits)
# fruits.clear()
# print(fruits)

# fruits.pop()
# print(fruits)




nums2=[1,5,8,3,6]
# nums1.sort()
# print(nums1)
print(max(nums2))
print(min(nums2))
print("average" , sum(nums2)/len(nums2))
print("thishdifndklfndskflndfkl", sum(nums2)/len(nums2))



text = "Python is fun and Python is powerful"
words = text.split()
print(words)
# unique_words = list(set(words))
# print(unique_words)


#make a cart list
#add item in to the cart
#and print the cart 

cart = []
cart.append("Cricket_bat")
cart.append('Helmet')
cart.append('golves')
cart.append('abdomin guard')
print(cart)
cart.remove("golves")
print(cart)
