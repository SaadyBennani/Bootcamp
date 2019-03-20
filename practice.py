# #practice.py
#
# def is_even (a):
#     if a % 2 == 0:
#         return True
#     else:
#         return False
#
# # same as return a % 2 == 0
# print(is_even(5))
# print(is_even(6))
#
# def opposite (a, b):
#     if (a >= 0 and b >= 0) or (a < 0 and b < 0):
#         return False
#
#     else: return True
#
# print(opposite(1, 2))
# print(opposite(-1, -2))
# print(opposite(1,-2))
# print(opposite(-1,2))
#
# mult_3 = list(range(3,100,3))
# mult_5 = list(range(5,101,5))
# print(mult_3)
# print(mult_5)
#
# total = 0
# for num in range(0,101):
#     if num %3 ==0 or num%5 == 0:
#         total += num
# print(total)

# def near_100(num):
#     if num not in range(90,111):
#         return False
#     else:
#         return True

# def max_of_three(a,b,c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c
#
# print(max_of_three(5,6,2))
# print(max_of_three(-4,3,10))
# print(max_of_three(1,1,4))

# def exp_to_twenty(num):
#     for e in range(0, 21):

# def double_letters(text):
#     double = []
#     for item in text:
#         double.append(item*2)
#     return ''.join(double)
# #
# # print(double_letters('hello'))
# import random
# def random_element(l):
#     if len(l) == 0:
#         return 'empty list'
#     index = random.randint(0,len(l)-1)
#     print(index)
#     return l[index]
# print(random_element([]))


# turning lists into dicts

# def lists_to_dict(keys, values):
#     combined = {}
#     for i in range(len(keys)):
#
#         combined[keys[i]] = values[i]
#     return combined
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
#
# print(lists_to_dict(fruits, prices))

# scoping

# x = 'global'
#
# def f():
#     x = 'enclosed'
#     print('in f', x)
#
#     def g():
#         x = 'local'
#         print('in g', x)
#
# print(x)
# f()
# # print(g()) #g is only in the scope of f


# sock sorter
# import random
# sock_types = ['ankle', 'crew', 'calf', 'thigh']
# sock_list = []
# sock_counter = {}
# sock_colors = ['black','white','blue']
#
# for i in range(100):
#     sock = random.choice(sock_types)
#     color = random.choice(sock_colors)
#     sock_list.append((color,sock))
#     sock_counter[(color,sock)]= sock_counter.get((color, sock), 0) + 1
#
# print(sock_list)
# print(sock_counter)
#
# for sock in sock_counter:
#     print(f'{sock} has {sock_counter[sock]%2} loner(s)')

# valid_move.py
# while True:
#     try:
#         move = int(input('Enter a position: '))
#         if move <1 or move >7:
#             raise ValueError
#         break
#     except ValueError:
#         print('Invalid move: enter a number between 1 and 7.')
# # print('It worked!')
#
# def lists_to_dict(keys, values):
#     # combined = {}
#     # for i in range(len(keys)):
#     #
#     #     combined[keys[i]] = values[i]
#     # return combined
#
#     return dict(zip(keys, values)) # same as above
# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
#
# print(lists_to_dict(fruits, prices))
#
#
# def average_values(dictionary):
#     return round(sum(dictionary.values())/len(dictionary), 1)
#
#     pass
#
# fruits = {'apple': 1.2, 'banana': 3.3, 'pear': 2.1}
# print(f'Average price of {fruits} = {average_values(fruits)}')

#
# def eveneven(x):
#     evens = [num for num in x if num %2 == 0] #comprehension
#     return len(evens)%2 == 0  #same as below
#     # nums = 0
#     # for item in x:
#     #     if item %2 == 0:
#     #         nums += 1
#     # return nums %2 == 0
#
#
# list= [5,6,2]
# list2 = [5,5,2]
# list3= [4,4,4,]
# list4= [2,2,7,9]
# print(eveneven(list))
# print(eveneven(list2))
# print(eveneven(list3))
# print(eveneven(list4))

#
# def powers_of_two(n):
#
#     return [2**i for i in range(0, n)]
#
# print(powers_of_two(10))
#
# def evens_to_n(n):
#     return [i*2 for i in range(1,n+1)]
#
# print(evens_to_n(10))
#
# def evens_from_n(n):
#     retun [i for i in range(n) ]

# nums = [24, 20, 11, 9, 8, 2, -1, 50]
# nums2 = [24, 20, 9, 'b', 'c', -1]
#
#
# def extract_less_than_ten(nums):
#     # extracted = []
#     # for i in nums:
#     #     if i <10:
#     #         extracted.append(i)
#     # return extracted
#     return [i for i in nums if i < 10]  # same as above
#
# # print(extract_less_than_ten(nums))
#
#
# def common_elements(nums1, nums2):
#     return list(set(nums1) & set(nums2))
#     # return [n for n in nums1 if n in nums2]
#
#
# print(nums, nums2, common_elements(nums, nums2))

# practice; string 6

# def count_letter(letter, word):
#     '''
#     >>> count_letter('i', 'antidisestablishmentterianism')
#     5
#     >>> count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')
#     2
#     '''
#     counter = 0
#     for i in word:
#         if i == letter:
#             counter += 1
#     return counter


# print(count_letter('l', 'hello'))

# practice lists 10 & 11 & 12
# def merge(list1, list2):
#     return [list(i) for i in zip(list1, list2)]
#
#
# out_list = merge([1, 2, 3], [4, 5, 6])
# print(out_list)
#
#
# def combine_all(list_of_lists):
#     return sum(list_of_lists, [])
#
#
# nums = [[5, 2, 3], [4, 5, 1], [7, 6, 3]]
# combined = combine_all(nums)
# print(combined)

# def find_unique(nums):
#     unique_nums = []
#     for i in nums:
#         if i not in unique_nums:
#             unique_nums.append(i)
#
#     return unique_nums
#
#
# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# print(find_unique(nums))

#
# d = {'a1': 5, 'a2': 2, 'a3': 3, 'b1': 10, 'b2': 1, 'b3': 1, 'c1': 4, 'c2': 5, 'c3': 6, 'd': 4}
#
#
# def unify(d):
#     running_sum = {}
#     for k, v in d.items():
#         if k[0] in running_sum:
#
#             current_sum, count = running_sum[k[0]]
#             running_sum[k[0]] = (current_sum + v, count + 1)
#         else:
#             running_sum[k[0]] = (v, 1)
#     return {key: rsum/count for (key, (rsum, count)) in running_sum.items()}
#
#
# print(unify(d))

class Dog:
    # A dog class
    def __init__(self):
        # each dog has a name and breed
        self.name = None
        self.breed = None

    def bark(self):
        # barks and says hello
        print('Wooof! My name is ' + self.name + " . I'm a " + self.breed + '!')


my_dog = Dog()
my_dog.name = 'Ellie Bear'
my_dog.breed = 'Golden Retriever'

my_dog.bark()
