
def anagrams(word):
    """
    Use the file WORD.LST and returns anagrams
    of the word given in parameter word
    """
    words = [
        w.rstrip() for w in open('WORD.lst')
        if len(w.rstrip()) == len(word) and w.rstrip() != word
    ]

    anagram_list = []

    for w in words:
        tmp_word = list(word)
        is_anagram = True
        for letter in w:
            if letter not in tmp_word:
                is_anagram = False
                break
            else:
                tmp_word.remove(letter)

        if is_anagram:
            anagram_list.append(w)

    return anagram_list


if __name__ == "__main__":
    print(anagrams("train"))
    print('--')
    print(anagrams("drive"))
    print('--')
    print(anagrams("python"))
