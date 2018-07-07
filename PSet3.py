# © Paribartan Dhakal
# July 6, 2018 

#problem 1
def 
    found=False
    for letters in secretWord:
        if letters in lettersGuessed:
            found=True
        else:
            found=False
            break
    return found

#problem 2
def getGuessedWord(secretWord, lettersGuessed):
    
    s=''
    for letter in secretWord:
        if letter in lettersGuessed:
            s=s+letter
        else:
            s=s+'_'+' '
    return s


#problem 3

def getAvailableLetters(lettersGuessed):
    s=string.ascii_lowercase
    for letter in lettersGuessed:
            s=s.replace(letter,'')
    return s
    
 #problem4
 def hangman(secretWord):
   
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))
    print('--------------------------')
    numberOfGuessesLeft=8
    lettersGuessed=''
    allGuessed=''
    wrongGuessed=''
    while numberOfGuessesLeft>0 and secretWord!=getGuessedWord(secretWord, lettersGuessed):
        print('You have {} guesses left'.format(numberOfGuessesLeft))
        
        print('Available Letters: {}'.format(getAvailableLetters(allGuessed)))
        
        userGuess=input('Please guess a letter: ')
        allGuessed+=userGuess
      
        if userGuess in secretWord and userGuess not in lettersGuessed:
            lettersGuessed+=userGuess
            print('Good Guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')
            
        elif userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')
        elif userGuess in wrongGuessed:
            print("Oops! You've already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')
        else:
            wrongGuessed+=userGuess
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')
            numberOfGuessesLeft=numberOfGuessesLeft-1
            
       
    if secretWord==getGuessedWord(secretWord, lettersGuessed):
        print('Congratulations, you have won!')
    else:
        print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))