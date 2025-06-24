def generate_leetspeak(word):
    """
    Return variations of the word using common leetspeak substitutions.
    """
    substitutions = {
        'a': ['@', '4'],
        'e': ['3'],
        'i': ['1', '!'],
        'o': ['0'],
        's': ['$', '5']
    }

    variants = set([word])
    for i, char in enumerate(word):
        if char.lower() in substitutions:
            for sub in substitutions[char.lower()]:
                new_word = word[:i] + sub + word[i+1:]
                variants.add(new_word)
    return variants

def append_years(word, start=1990, end=2026):
    """
    Return variations of the word with years appended to the end.
    """
    return [f"{word}{year}" for year in range(start, end + 1)]
