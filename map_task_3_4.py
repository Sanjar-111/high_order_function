def map_task_3_4(numbers):
    """
    Square each number.
    Args:
        numbers: list of integers [1, 4, 5]
    Returns:
        list of squared numbers
    """
    return numbers**2
numbers=[1, 4, 5]
print(list(map(map_task_3_4,numbers)))
