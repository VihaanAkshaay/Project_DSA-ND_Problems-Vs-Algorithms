def rotated_array_search(input_list, number, mid=0):
    """
    Find the index by searching in a rotated sorted array
    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    l = len(input_list)
    begin = 0
    end = l

    if begin == end:
        return -1

    while begin <= end:
        pivot = (begin+end) // 2
        #print('p', pivot)
        if input_list[0] < input_list[l-1] or pivot == l-1:
            pivot = 0
            break
        if input_list[pivot-1] > input_list[pivot]:
            break
        elif input_list[0] < input_list[pivot]:
            begin = pivot
        elif input_list[0] > input_list[pivot]:
            end = pivot
        #By the end of this, we can make sure
        # that the begin and end signify the start
        # and end of the larger continuous part of the rotated array

    if input_list[pivot] <= number and input_list[l-1] >= number:
        begin = pivot
        end = l
    else:
        begin = 0
        end = pivot

    while begin <= end:
        pivot = (begin+end) // 2
        if input_list[pivot] == number:
            return pivot
        elif input_list[pivot] < number:
            begin = pivot+1
        else:
            end = pivot-1
    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")
        #print(rotated_array_search(input_list, number))


#%% Testing - Official
# Normal cases
print('Normal Cases:')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('\n')


# Edge cases
print('Edge Cases:')
test_function([[], -1])
test_function([[1], 0])
