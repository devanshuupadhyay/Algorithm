# backend/algorithms/sorting.py
def simple_sort(numbers: list[int | float]) -> list[int | float]:
    """
    A simple function that takes a list of numbers
    and returns a sorted list.
    """
    # For demonstration, we use Python's built-in sorted().
    # You can replace this with your own sorting algorithm later!
    print(f"Received numbers to sort: {numbers}")
    sorted_list = sorted(numbers)
    print(f"Returning sorted list: {sorted_list}")
    return sorted_list