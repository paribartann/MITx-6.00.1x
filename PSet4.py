# © Paribartan Dhakal
# July 6, 2018 

#PROBLEM 1

def getWordScore(word, n):
    value=0
    for letter in word:
        value+=SCRABBLE_LETTER_VALUES[letter]
    if len(word)==n:
        value=len(word)*value+50
    else:
        value=len(word)*value
    
    return value


#problem 2

def updateHand(hand, word):
    hand1=hand.copy()
    for letter in word:
        if letter in hand.keys():
            hand1[letter]-=1
    return hand1

#problem 3

def isValidWord(word, hand, wordList):
    value=False
    hand1=hand.copy()
    for letter in word:
        if letter in hand1.keys() and hand1[letter]>0 and word in wordList:
            hand1[letter]-=1
            value=True
        else:
            value=False
            break
            
    return value
            
            
#problem 4
def calculateHandlen(hand):
    sum=0
    for num in hand.values():
        sum+=num
    return sum

#problem 5

def playHand(hand, wordList, n):
    score=0
    # As long as there are still letters left in the hand:
    while int(sum(hand.values()))>0:
        print("Current Hand: ", end="")
        displayHand(hand)
        # Display the hand
        userInput=input("Enter word, or a '.' to indicate that you are finished: ")
        # Ask user for input
        
        # If the input is a single period:
        if userInput=='.':
            # End the game (break out of the loop)
            break

            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord(userInput, hand, wordList):
                
                # Reject invalid word (print a message followed by a blank line)
                print("Invalid word, please try again.\n")
            # Otherwise (the word is valid):
            else:
                score+=getWordScore(userInput, n)
                print('"{}" earned {} points. Total: {} points \n'.format(userInput, getWordScore(userInput, n), score))
                
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                hand=updateHand(hand, userInput)
                # Update the hand 
                
    if userInput==".":
        print("GoodBye! Total Score: {} points".format(score))
        
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    else:
        print("Run out of letters. Total score: {} points.".format(score))



#Problem 6 
def playGame(wordList):
    gameCount=0
    
    while True:
        
        userInput=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if userInput!='n' and userInput!='r' and userInput!='e':
            print('Your input was invalid')
        else:
            if userInput=='n':
                gameCount+=1
                hand=dealHand(HAND_SIZE)
                playHand(hand.copy(), wordList, HAND_SIZE)
            elif userInput=='r':
                if gameCount==0:
                    print('You have not played a hand yet. Please play a new hand first!')
                else:
                    playHand(hand.copy(), wordList, HAND_SIZE)
            else:
                break
            
            print()


 #Problem 7 (18.00/20.00)

 def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO...
    gameCount=0
    while True:
    
        userInput=input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if userInput!='n' and userInput!='r' and userInput!='e':
            print('Invalid command.')
        elif userInput=='e':
            break
        elif userInput=='r' and gameCount==0:
            print('You have not played a hand yet. Please play a new hand first!')
        else:
            #while True:
                nextInput=input('Enter u to have yourself play, c to have the computer play: ')
                if nextInput!='u' and nextInput!='c':
                    print('Invalid command.')
                elif nextInput=='u':
                    if userInput=='n':
                        gameCount+=1
                        hand=dealHand(HAND_SIZE)
                        playHand(hand.copy(), wordList, HAND_SIZE)
                    elif userInput=='r':
                        if gameCount==0:
                           print('You have not played a hand yet. Please play a new hand first!')
                        else:
                            playHand(hand.copy(), wordList, HAND_SIZE)
                elif nextInput=='c':
                    if userInput=='n':
                        gameCount+=1
                        hand=dealHand(HAND_SIZE)
                        compPlayHand(hand.copy(), wordList, HAND_SIZE)
                    elif userInput=='r':
                        if gameCount==0:
                            print('You have not played a hand yet. Please play a new hand first!')
                        else:
                            compPlayHand(hand.copy(), wordList, HAND_SIZE)        
                #else:
                    #break
                print()











