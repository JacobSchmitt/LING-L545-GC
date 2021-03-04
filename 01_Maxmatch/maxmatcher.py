import 	sys



#dictionary = [(len(line), line.strip()) for line in open("thaidict.dict").readlines()]
#dictionary.sort()
#dictionary.reverse()
dictionary = [line.strip() for line in open("thaidict.dict").readlines()]



def maxmatch(sentence, dictionary):
	if sentence == '':
		return []
	for i in range(0, len(sentence)):
		firstword = sentence[0:-i]
		remainder = sentence[-i:]
		if firstword in dictionary:
			return [firstword] + maxmatch(remainder, dictionary)

	firstword = sentence[0]
	remainder = sentence[1:]
	return [firstword] + maxmatch(remainder, dictionary)



line = sys.stdin.readline()
while line:
	print(' '.join(maxmatch(line.strip('\n'), dictionary)))
	line = sys.stdin.readline()
