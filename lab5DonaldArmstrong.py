

def main():
	# encodedWord = "UUHO"
	# encodedWord = "WBLARF8TTS"
	# encodedWord = "L8KAOUL"
	# encodedWord = "E8N8N8" 
	# encodedWord = "8TRA8DY T8LA"
	encodedWord = "8TT LHA TILLTA LIMAS"	
	# encodedWord = "LHA GRAAN FIATD GTA8MS IN LHA W8RM SUNEABMS"
	# encodedWord = "TONG T8E T8CKS L8SLY L8CO LIMA 8L TA8SL T8LATY"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
	
	print(DecodeWord(encodedWord))





#Your code goes here.
def DecodeWord(word):
    newword = ""# inizilizzed new word into an empty string
    for i in range(0,len(word)): #len = the length of the string.len("----") == 4. YOU HAVE TO START AT ZERO because python starts things at 0 instead of 1. 
        oldletter = word[i] #takes the i(i = letter in sequence that will be decoded) character from our encoded word

       
        newletter = DecodeCharacter(oldletter) #actually decode the letter(i)
        # print(oldletter,newletter,newword)
        newword = newword + newletter # cancatinate newword with the new letter. Build the new word with new letters
        
    return newword



def DecodeCharacter(character): #this function is decoding the letters within the word into what they should output to
    if character == "L": #input L 
        return "T"#output to T and so forth
    elif character == "T": 
        return "L"
    elif character == "8":
        return "A"
    elif character == "B":
        return "A"
    elif character == "A":
        return "E"
    elif character == "E":
        return "B"
   
    else:
        return character


	
def DecodeWordBonus(word):
    newword = ""# inizilizzed new word into an empty string
    for i in range(0,len(word)): #len = the length of the string.len("----") == 4. YOU HAVE TO START AT ZERO because python starts things at 0 instead of 1. 
        oldletter = word[i] #takes the i(i = letter in sequence that will be decoded) character from our encoded word
        print(i,len(word),i+1)
        if i + 1 < len(word):
            nextletter = word[i+1]
        else:
            nextletter = ""
        newletter = DecodeCharacter(oldletter,nextletter) #actually decode the letter(i)
        print(oldletter,newletter,newword)
        newword = newword + newletter # cancatinate newword with the new letter. Build the new word with new letters
        
    return newword










#This code triggers the main to run
#we'll talk about this more in chapters 6,7, & 8.	
if __name__ == "__main__":
	main()
