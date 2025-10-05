# Задание «Палиндромы»

def solve(phrases: list):
    """
    Возвращает список палиндромов из переданных фраз (пробелы игнорируются).
    """
    result = []
    for phrase in phrases:
        x = phrase.replace(" ", "")
        if x[::-1] == x:
           result.append(phrase.lower())
    return result

