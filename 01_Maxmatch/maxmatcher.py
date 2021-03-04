import 	sys


#below are no longer necessary as I used a different approach to read in the dictionary
#dictionary = [(len(line), line.strip()) for line in open("thaidict.dict").readlines()]
#dictionary.sort()
#dictionary.reverse()
dictionary = [line.strip() for line in open("thaidict.dict").readlines()]



def maxmatch(sentence, dictionary):
	#so if the txt is empty then just return empty
	if sentence == '':
		return []
	#for each character from the back of the sentence moving forward
	for i in range(0, len(sentence)):
		#firstword is our whole sentence up to where i is, remainder is the rest
		firstword = sentence[0:-i]
		remainder = sentence[-i:]
		#if firstword is in dictionary (if firstword is a word), return it
		if firstword in dictionary:
			return [firstword] + maxmatch(remainder, dictionary)
	#reset firstword and remainder
	firstword = sentence[0]
	remainder = sentence[1:]
	#recursive call to the function with the remainder 
	return [firstword] + maxmatch(remainder, dictionary)


#this is the part that actually does it
line = sys.stdin.readline()
while line:
	print(' '.join(maxmatch(line.strip('\n'), dictionary)))
	line = sys.stdin.readline()
