def merge_sort(arr, depth=0):
    """Perform merge sort with debug output showing recursion depth."""
    indent = "   " * depth  # indentation for readability
    print(f"{indent}merge_sort({arr})")

    # Base case
    if len(arr) <= 1:
        return arr

    # Split array
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    print(f"{indent}Split into {left} and {right}")

    # Recursive sorting
    left_sorted = merge_sort(left, depth + 1)
    right_sorted = merge_sort(right, depth + 1)

    # Merge step
    merged = merge(left_sorted, right_sorted, depth)
    print(f"{indent}Merged {left_sorted} and {right_sorted} into {merged}")
    return merged


def merge(left, right, depth=0):
    """Merge two sorted lists into one sorted list."""
    indent = "   " * depth
    result = []
    i = j = 0

    print(f"{indent}Merging {left} and {right}")

    # Compare elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    print(f"{indent}Result after merge: {result}")
    return result


# Example usage
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", arr)
    sorted_arr = merge_sort(arr)
    print("\nFinal Sorted array:", sorted_arr)
