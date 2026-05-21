
def map_task_3_2(words):
    """
    Convert all words to uppercase.
    Args:
        words: list of strings ["cat", "dog", "fish"]
    Returns:
        list of uppercase words
    """
    return words.upper()
words=["cat", "dog", "fish"]
print(list(map(map_task_3_2,words)))