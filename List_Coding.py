

#1 Exercise 1: Reverse a list in Python
# list1 = [100, 200, 300, 400, 500 ]
                                     # Output : [500, 400, 300, 200, 100]
# length = len(list1)
# reverse_list=[]
# for i in range(length) :
#     reverse_list.append(list1[length-i-1])
# print(reverse_list)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Exercise 2: Concatenate two lists index-wise

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Output ['My', 'name', 'is', 'Kelly']   using this method 0.195 seconds

# list3 = []
# for i in range(len(list1)) :
#     list3.append(list1[i] + list2[i])
# print(list3)


# list3 = [i + j for i, j in zip(list1, list2)]  # using this method 0.182 seconds
# print(list3)



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Exercise 3: Turn every item of a list into its square

# numbers = [1, 2, 3, 4, 5, 6, 7]

# Output:[1, 4, 9, 16, 25, 36, 49]

# sqr = []
# for i in numbers :
#     sqr.append(i*i)
# print(sqr)    #using thie method to take time  0.198 seconds

# l = [i*i for i in numbers]
# print(l) #  using thie method to take time  0.180 seconds


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# Output : ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

# add_list = []
# for i in list1 :
#     for j in list2 :
#         add_list.append(i+j)
# print(add_list)   using thie method to take tim 0.217 seconds



# res = [x + y for x in list1 for y in list2]  #  using thie method to take time 0.189second
# print(res)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Exercise 5: Iterate both lists simultaneously
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

''' Output 
10 400
20 300
30 200
40 100

'''
# length = len(list1)
# for i in range(length):
#     print(list1[i] ,list2[length-i-1] )  # 0.181 seconds


# for x, y in zip(list1, list2[::-1]):
#     print(x, y)   # 0.179 seconds 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# Exercise 6: Remove empty strings from the list of strings

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Output : ["Mike", "Emma", "Kelly", "Brad"]

# method-1
# res = [i for i in list1 if i !=""]
# print(res)    0.204 seconds

# Metho-2
# res = []
# for i in list1 :
#     if i != "":
#         res.append(i)  #0.194 seconds

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Exercise 7: Add new item to list after a specified item   
# (Write a program to add item 7000 after 6000 in the following Python List)
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]








