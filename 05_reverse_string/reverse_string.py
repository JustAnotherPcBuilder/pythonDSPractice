def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    newstr = ''
    for index in reversed(range(len(phrase))):
        newstr += phrase[index]
    return newstr