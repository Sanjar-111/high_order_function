def max_task_2_4(words):
    """
    Find the word with the most vowels.
    Args:
        words: list of strings ["tree", "education", "sky", "road"]
    Returns:
        word with most vowels
    """
    return
def vovels_of_words(words):
    a="AIUEOaiueo"
    count=1
    for i in words:
        count+=i in a
    return count
words=["tree", "education", "sky", "road"]
# print(vovels_of_words(words))
print(max(words,key=vovels_of_words))
    