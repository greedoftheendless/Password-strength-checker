from utils import generate_leetspeak, append_years

def generate_wordlist(inputs):
    """
    Generate a custom wordlist from user inputs with leetspeak and years.
    """
    base = set(inputs)
    wordlist = set(base)

    for word in base:
        wordlist.update(generate_leetspeak(word))
        wordlist.update(append_years(word))

    return sorted(wordlist)

def save_wordlist(words, filename="wordlist.txt"):
    """
    Save wordlist to a text file.
    """
    with open(filename, "w") as f:
        for word in words:
            f.write(word + "\n")
