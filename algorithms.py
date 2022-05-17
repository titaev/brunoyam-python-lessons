# Search

search_list = [2, 3, 4, 23, 33, 44]
elem = 23


def linear_search_elem(search_list, elem):
    for i in search_list:
        if i == elem:
            print(i)


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