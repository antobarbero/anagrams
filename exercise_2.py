
def annograms(word):
	"""
	Use the file WORD.LST and returns annograms
	of the word given in parameter word
	"""
	words = [w.rstrip() for w in open('WORD.lst') if len(w.rstrip()) == len(word) and w.rstrip() != word]
	annogram_list = []

	for w in words:
		tmp_word = list(word)
		is_annogram = True
		for letter in w:
			if letter not in tmp_word:
				is_annogram = False
				break
			else:
				tmp_word.remove(letter)

		if is_annogram : annogram_list.append(w)	

	return annogram_list
	
	raise NotImplementedError


if __name__ == "__main__":
	print(annograms("train"))
	print('--')
	print(annograms("drive"))
	print('--')
	print(annograms("python"))
