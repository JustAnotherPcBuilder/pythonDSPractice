def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = list('aeiou')
    front = 0
    end = len(s)
    lst = list(s)
    for i in range(len(s)):
        if i == end: break
        if lst[i].lower() in vowels:
            for j in reversed(range(end)):
                if j == i :
                    break
                if lst[j].lower() in vowels:
                    temp = lst[i]
                    lst[i] = lst[j]
                    lst[j] = temp
                    end = j
                    break
    return ''.join(lst)