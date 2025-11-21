def bubble_sort(arr):
    """
    Performs bubble sort on the input list 'arr' in-place.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already in the correct place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

if __name__ == "__main__":
    # Test bubble_sort with example lists
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [],
        [1],
        [2, 2, 2, 2],
        [10, 9, 8, 7, 6, 5],
    ]
    for idx, arr in enumerate(test_cases):
        print(f"Original List {idx+1}: {arr}")
        bubble_sort(arr)
        print(f"Sorted List {idx+1}:   {arr}")
        print()
