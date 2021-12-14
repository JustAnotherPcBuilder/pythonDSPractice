def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return ' '.join([  (word[0].upper() + word[1:].lower()) if len(word) > 1 else word[0].upper() for word in phrase.split(' ')])