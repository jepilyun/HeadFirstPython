
def search4vowels(inza:str='aeiou', phrase:str) -> set:
    """Return any vowels found in a supplied phrase."""
    return set(inza).intersection(set(phrase))
