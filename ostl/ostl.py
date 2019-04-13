CODE = {' ': '_', 
	"'": '.----.', 
	'(': '-.--.-', 
	')': '-.--.-', 
	',': '--..--', 
	'-': '-....-', 
	'.': '.-.-.-', 
	'/': '-..-.', 
	'0': '-----', 
	'1': '.----', 
	'2': '..---', 
	'3': '...--', 
	'4': '....-', 
	'5': '.....', 
	'6': '-....', 
	'7': '--...', 
	'8': '---..', 
	'9': '----.', 
	':': '---...', 
	';': '-.-.-.', 
	'?': '..--..', 
	'A': '.-', 
	'B': '-...', 
	'C': '-.-.', 
	'D': '-..', 
	'E': '.', 
	'F': '..-.', 
	'G': '--.', 
	'H': '....', 
	'I': '..', 
	'J': '.---', 
	'K': '-.-', 
	'L': '.-..', 
	'M': '--', 
	'N': '-.', 
	'O': '---', 
	'P': '.--.', 
	'Q': '--.-', 
	'R': '.-.', 
	'S': '...', 
	'T': '-', 
	'U': '..-', 
	'V': '...-', 
	'W': '.--', 
	'X': '-..-', 
	'Y': '-.--', 
	'Z': '--..', 
	'_': '..--.-'}

def convertToMorseCode(sentence):
    sentence = sentence.upper()
    encodedSentence = ""
    for character in sentence:
        encodedSentence += CODE[character] + " " 
    return encodedSentence



def encodeToWords(sentence):
    encodedSentence = convertToMorseCode(sentence)
    for character in encodedSentence:
        if character == '-':
            print("Dash")
        elif character == '.':
            print("Dot")
        elif character == ' ':
            print('.')
        elif character == '_':
            print("Space")




def s2b (s):
    a=[]


    for i in s :
        val=ord(i)
        binary_val = bin(val)
        a.append(binary_val[2:])
       
    print a


while True:
	
    print " Menu:"
    print " 1. Morse code"
    print " 2. Morse code (Dash-Dot)"
    print " 3. Text to Binary"
    print " 4. Exit."
    ch = input(" Select : ")
    
 
    if ch == 1:
        sentence = raw_input("Enter sentence: ")
		#encodedSentence=convertToMorseCode(sentence)
		print (encodedSentence)
		
    if ch == 2:
        sentence = raw_input("Enter sentence: ")
		encodeToWords(sentence)
    if ch == 3:
        s=raw_input("enter the string")
		s2b(s)
 
    if ch == 4:
        break
