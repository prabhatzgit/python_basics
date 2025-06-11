def merge_sort(arr):
    # Base case: If the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = []
    left_idx = right_idx = 0

    # Compare elements from both halves and merge them in sorted order
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_list.append(left[left_idx])
            left_idx += 1
        else:
            sorted_list.append(right[right_idx])
            right_idx += 1

    # Add any remaining elements from the left or right list
    sorted_list.extend(left[left_idx:])
    sorted_list.extend(right[right_idx:])

    return sorted_list


# Example usage:
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sorted List:", sorted_list)