from spellchecker import SpellChecker

# sucessfully generated frequency for cipher

eng_freq = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 
					'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

input_string = "lgdtmodtl o ytts miam o ligwsr stm bgw ass qfgc miam mitkt ol a dgflmtk cioei iortl ztiofr mit zsaeqzgakr of esall zwm mitf om sggql rtth ofmg db tbtl citf o eafm ktdtdztk ciam dami o ad lwhhgltr mg zt masqofu azgwm afr o qfgc miam o ad fgm alltkmoxt tfgwui mg mtss bgw aslg om cgwsr zt uggr mg mtss bgw miam ciost ct al a mtaeiofu lmayy eakt azgwm bgw gwk lmwrtfml a uktam rtas ct aslg hkogkomont gwk laytmb yaoksb iouisb lg oy miol dgflmtk txtk rgtl zktaq gwm ykgd ztiofr mit zsaeqzgakr o coss zt kwffofu al yalm al o eaf gwm gy mit rggk maqofu arxafmaut gy mit yaem miam om coss utm gft gy bgw afr mitf zt mgg zwlb mg eialt dt"

# analyze the ciphertext to break the substitution cipher
# return (plaintext, ciphertext alphabet)
# where ciphertext alphabet(CA) is of the form [c1, c2, c3, c4, _, c6, _, ...]
# replace c3 with whatever character in the CA corresponds to c in the PA
# _ is used to denote any letter for which you are uncertain about
def decode(ciphertext):

	# gets a list of letters in cipher text by frequency (most frequent...least frequent)
	ciph_dic = {i : ciphertext.count(i) for i in set(ciphertext)}
	del ciph_dic[' ']
	temp = []
	for key in ciph_dic:
		temp.append((key, ciph_dic[key]))
	temp.sort(key=lambda tup: tup[1])
	temp.reverse()
	ciph_freq = [x[0] for x in temp]


	# gets one letter words frequency in one_letter_freq
	one_letter = []
	one_letter_options = ['a', 'i']
	for x, y in enumerate(ciphertext):
			if ciphertext[x-1] == ' ' and ciphertext[x+1] == ' ':
				one_letter.append(ciphertext[x])
	one_dic = {i : one_letter.count(i) for i in one_letter}
	one_temp = []
	for key in one_dic:
		one_temp.append((key, one_dic[key]))
	one_temp.sort(key=lambda tup: tup[1])
	one_temp.reverse()
	one_letter_freq = [x[0] for x in one_temp]


	# gets two letter words frequency in two_letter_freq
	two_letter = []
	two_letter_options = ["of", "to", "in", "it", "is", "be", "as", "at", "so", "we", "he", "by", "or", "on", "do", "if", "me", "my", "up", "an", "go", "no", "us", "am"]
	for x, y in enumerate(ciphertext):
			if ciphertext[x] == ' ' and x+3 < len(ciphertext) and ciphertext[x+3] == ' ':
				two_letter.append(ciphertext[x+1: x+3])
	two_dic = {i : two_letter.count(i) for i in two_letter}
	two_temp = []
	for key in two_dic:
		two_temp.append((key, two_dic[key]))
	two_temp.sort(key=lambda tup: tup[1])
	two_temp.reverse()
	two_letter_freq = [x[0] for x in two_temp]

	# gets 3 letter words frequency in three_letter_freq
	three_letter = []
	three_letter_options = ["the", "and", "for", "are", "but", "not", "you", "all", "any", "can", "had", "her", "was", "one", "our", "out", "day", "get", "has", "him", "his", "how", "man", "new", "now", "old", "see", "two", "way", "who", "boy", "did", "its", "let", "put", "say", "she", "too", "use"]
	for x, y in enumerate(ciphertext):
			if ciphertext[x] == ' ' and x+4 < len(ciphertext) and ciphertext[x+4] == ' ':
				three_letter.append(ciphertext[x+1: x+4])
	three_dic = {i : three_letter.count(i) for i in three_letter}
	three_temp = []
	for key in three_dic:
		three_temp.append((key, three_dic[key]))
	three_temp.sort(key=lambda tup: tup[1])
	three_temp.reverse()
	three_letter_freq = [x[0] for x in three_temp]


	# gets double characters frequency in double_letter_freq
	double_letter = []
	double_letter_options = ["ss", "ee", "tt", "ff", "ll", "mm", "oo",]
	for x, y in enumerate(ciphertext):
			if ciphertext[x-1] == ciphertext[x]:
				double_letter.append(ciphertext[x-1: x+1])
	double_dic = {i : double_letter.count(i) for i in double_letter}
	double_temp = []
	for key in double_dic:
		double_temp.append((key, double_dic[key]))
	double_temp.sort(key=lambda tup: tup[1])
	double_temp.reverse()
	double_letter_freq = [x[0] for x in double_temp]

	guess(input_string, ciph_freq, eng_freq)
	
def guess(ciphertext, ciph_freq, alphabet):
	ciph_temp = ciphertext
	for x in ciphertext:
		if(x != " "):
			
	print(ciphertext)
		

decode(input_string)



