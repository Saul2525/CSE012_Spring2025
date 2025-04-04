"""
    Saul Toribio
    4/3/25
    CSE012 Spring 2025: Week 10 Coding Assignment
    IDE: VSCode; Python: 3.12.7
"""

def linear_search(search_list: list, target_value: any) -> int | None:
    """
    Performs a linear search to find the index of target_value in search_list.

    Args:
        search_list (list): A list of items to search through.
        target_value: The value to search for.

    Returns:
        int: The index of the first occurrence of target_value in search_list.
             Returns None if target_value is not found.

    Efficiency: O(n) - Checks each item in the worst case.
    """
    for index, item in enumerate(search_list):
        if item == target_value:
            return index
    return None

def binary_search(sorted_list: list, target_value: any) -> int | None:
    """
    Performs a binary search to find the index of target_value in sorted_list.

    IMPORTANT: This function assumes sorted_list is already sorted in ascending order.

    Args:
        sorted_list (list): A list of items sorted in ascending order.
        target_value: The value to search for.

    Returns:
        int: The index of target_value in sorted_list.
             Returns None if target_value is not found.

    Efficiency: O(log n) - Halves the search space with each comparison.
    """
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target_value:
            return mid

        if sorted_list[mid] < target_value:
            low = mid + 1
        else:
            high = mid - 1
    return None

def selection_sort(value_list: list) -> list:
    """
    Sorts a list of comparable items in ascending order using Selection Sort.

    Args:
        value_list (list): A list of items to be sorted.

    Returns:
        list: A new list containing the items from value_list sorted in
              ascending order. Does not modify the original list.

    Efficiency: O(n^2) - Uses nested loops to find the minimum and swap.
    """
    sorted_list = value_list[:]
    for i in range(len(sorted_list) - 1):
        min_index = i
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j

        sorted_list[i], sorted_list[min_index] = sorted_list[min_index], sorted_list[i]
    return sorted_list

def main():
    """
    Simulates the adventurer's exploration using the search and sort functions.
    """
    artifacts = ["Golden Idol", "Crystal Skull", "Sunstone", "Ancient Vase", "Jeweled Dagger"]
    target_artifact = "Sunstone"
    print(f"Searching for {target_artifact} in artifacts: {artifacts}")
    artifact_index = linear_search(artifacts, target_artifact)
    if artifact_index is not None:
        print(f"Found {target_artifact} at index {artifact_index}!")
    else:
        print(f"{target_artifact} not found.")

    print("-" * 20)

    scroll_ids = [101, 153, 244, 512, 842, 1024, 1500]
    target_scroll_id = 842
    print(f"Searching for scroll ID {target_scroll_id} in sorted IDs: {scroll_ids}")
    scroll_index = binary_search(scroll_ids, target_scroll_id)
    if scroll_index is not None:
        print(f"Found scroll ID {target_scroll_id} at index {scroll_index}!")
    else:
        print(f"Scroll ID {target_scroll_id} not found.")

    target_scroll_id_missing = 600
    print(f"Searching for scroll ID {target_scroll_id_missing} in sorted IDs: {scroll_ids}")
    scroll_index_missing = binary_search(scroll_ids, target_scroll_id_missing)
    if scroll_index_missing is not None:
        print(f"Found scroll ID {target_scroll_id_missing} at index {scroll_index_missing}!")
    else:
        print(f"Scroll ID {target_scroll_id_missing} not found. (Correct!)")

    print("-" * 20)

    treasure_values = [150, 20, 80, 500, 10, 95, 300]
    print(f"Original treasure values: {treasure_values}")
    sorted_treasures = selection_sort(treasure_values)
    print(f"Sorted treasure values: {sorted_treasures}")
    print(f"Original list after sorting (should be unchanged): {treasure_values}")

    print("-" * 20)
    print("Adventure simulation complete!")

if __name__ == "__main__":
    main()
