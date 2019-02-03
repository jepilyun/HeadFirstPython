def search4vowels(phrase:str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(phrase))
    return found


def search4letters(phrase:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(phrase))
    
