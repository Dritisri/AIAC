def linear_search(lst, value):
    """
    Performs a linear search for 'value' in 'lst'.
    Returns the index if found, otherwise returns -1.
    """
    for idx, item in enumerate(lst):
        if item == value:
            return idx
    return -1              
                           # Test cases to demonstrate the function
if __name__ == "__main__":
    # Test case 1: Element found
    test_list1 = [1, 3, 5, 7, 9, 11, 13, 15]
    search_value1 = 7
    result1 = linear_search(test_list1, search_value1)
    print(f"Searching for {search_value1} in {test_list1}")
    print(f"Result: {result1}")
    print()
    # Test case 2: Element not found
    test_list2 = [2, 4, 6, 8, 10]
    search_value2 = 5
    result2 = linear_search(test_list2, search_value2)
    print(f"Searching for {search_value2} in {test_list2}")
    print(f"Result: {result2}")
    print()
    # Test case 3: Empty list
    test_list3 = []
    search_value3 = 1
    result3 = linear_search(test_list3, search_value3)
    print(f"Searching for {search_value3} in {test_list3}")
    print(f"Result: {result3}")
    print()
    # Test case 4: First element
    test_list4 = [10, 20, 30, 40, 50]
    search_value4 = 10
    result4 = linear_search(test_list4, search_value4)
    print(f"Searching for {search_value4} in {test_list4}")
    print(f"Result: {result4}")
    print()
     # Test case 5: Last element
    test_list5 = [100, 200, 300, 400, 500]
    search_value5 = 500
    result5 = linear_search(test_list5, search_value5)
    print(f"Searching for {search_value5} in {test_list5}")
    print(f"Result: {result5}")