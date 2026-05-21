def map_task_3_3(words):
    """
    Get the lengths of each word.
    Args:
        words: list of strings ["hi", "hello", "bye"]
    Returns:
        list of word lengths
    """
    return len(words)
words=["hi", "hello", "bye"]
print(list(map(map_task_3_3,words)))