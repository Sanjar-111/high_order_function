def min_task_1_3(words):
    """
    Find the string with the smallest number of vowels.
    Args:
        words: list of strings ["book", "sky", "quiet", "data"]
    Returns:
        string with fewest vowels
    """
    return
def vovels_of_words(words):
    a="AIUEOaiueo"
    count=1
    for i in words:
        count+=i in a
    return count
words=["book", "sky", "quiet", "data"]
print(min(words,key=vovels_of_words))