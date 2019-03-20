# avg_num.py
#
# nums = [5,0,8,3,4,1,6]
# sum_of_nums = 0
# avg = (sum_of_nums)/len(nums)
#
#
# for num in nums:
#     sum_of_nums += num
#     avg = (sum_of_nums)/len(nums)
#
#
# print(sum_of_nums)
# print(avg)


nums_list = []


while True:
    try:
        user_nums = input("enter a number, or 'done'>")
        if user_nums == 'done':
            print(sum(nums_list)/len(nums_list))
            break

        else:
            nums_list.append(int(user_nums))
            print(nums_list)
    except ZeroDivisionError:
        print(0)
    except ValueError:
        pass
