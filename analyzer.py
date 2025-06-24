from zxcvbn import zxcvbn

def analyze_password(password):
    """
    Analyze password strength using zxcvbn and return score and suggestions.
    Score is from 0 (weak) to 4 (strong).
    """
    result = zxcvbn(password)
    score = result['score']
    suggestions = result['feedback'].get('suggestions', [])
    return score, suggestions
