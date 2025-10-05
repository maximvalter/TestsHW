# Задание «Голосование»

from collections import Counter

def vote(votes):
    """
    Возвращает самый частый элемент в списке, строке или числе.
    """
    if isinstance(votes, (str, int)):
        votes = [int(ch) for ch in str(votes)]
    return Counter(votes).most_common(1)[0][0]
