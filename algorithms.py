# Search
import time
# start_time = time.clock()
# main()
# print time.clock() - start_time, "seconds"

search_list = [2, 3, 4, 23, 33, 44, 55, 66, 77]
elem = 66


def linear_search_elem(search_list, elem):
    for i in search_list:
        if i == elem:
            print(i)

# start_time = time.time()
# linear_search_elem(search_list, elem)
# print(time.time() - start_time, "seconds")



def binary_search_recoursive(search_list, elem):
    left_index = 0
    right_index = len(search_list) - 1
    medium_index = (left_index + right_index) // 2

    if elem < search_list[medium_index]:
        right_index = medium_index
        search_list = search_list[:right_index]
        binary_search_recoursive(search_list, elem)
    elif elem > search_list[medium_index]:
        left_index = medium_index + 1
        search_list = search_list[left_index:]
        binary_search_recoursive(search_list, elem)
    else:
        print(search_list[medium_index])

# start_time = time.time()
# binary_search_recoursive(search_list, elem)
# print(time.time() - start_time, "seconds")

def binary_search_iterative(array, element):
    mid = 0
    start = 0
    end = len(array)
    step = 0

    while (start <= end):
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# Sort
sort_list = [2, 35, 4, 23, 3, 1]


def buble_sort(sort_list):
    # print(range(len(sort_list) - 1))
    for i in range(len(sort_list) - 1):
        for j in range(len(sort_list) - i - 1):
            if sort_list[j] > sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list

# print(buble_sort(sort_list))
# buble_sort(sort_list)


def choose_sort(sort_list):
    new_list = []

    iterations = len(sort_list)-1
    for i in range(iterations):
        least_value = find_least_value(sort_list)
        new_list.append(least_value)
        sort_list.remove(least_value)
    print(new_list)


def find_least_value(sort_list):
    least_value = sort_list[0]
    for i in sort_list:
        if i < least_value:
            least_value = i
    return least_value

# choose_sort(sort_list)


# MERGE SORT

def merge_sort(sort_list):
    if len(sort_list) < 2:
        return sort_list

    medium_index = len(sort_list) // 2
    left = merge_sort(sort_list[:medium_index])
    right = merge_sort(sort_list[medium_index:])
    return merge(left, right)


def merge(left_list, right_list):
    result = []
    i, j = 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        elif left_list[i] > right_list[j]:
            result.append(right_list[j])
            j += 1

    if i < len(left_list):
        result.append(left_list[i])

    elif j < len(right_list):
        result.append(right_list[j])

    return result


print(merge_sort(sort_list))



# ГРАФЫ
