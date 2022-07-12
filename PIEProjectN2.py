from termcolor import colored, cprint
from random import choice, randint

def chooseGameMode():
    """
    The function asks player(s) about the game mode.
    Returns int(1) if the player(s) chose 1-player mode and int(2) otherwise.
    Returns False if the player(s) chose exit the game ('q')
    """
    # Question about the number of players
    questionForMode = colored('You can choose the game mode:', on_color='on_cyan') + '\n' + \
        colored('1) 1-player mode', on_color='on_cyan') + '\n' + \
        colored('2) 2-player mode', on_color='on_cyan') + '\n' + \
        colored('Enter "exit" to exit the game', on_color='on_cyan') + '\n' + '\n' + \
        colored('What is your choice?', 'white', 'on_blue', attrs=['bold']) + ' '
    
    answer = input(questionForMode)

    while True:
        if answer == '1':
            return 1
        elif answer == '2':
            return 2
        elif answer == 'exit':
            return False
        else:
            answer = input(colored('Enter "1","2" or "exit" only:', 'white', \
                on_color='on_red', attrs=['bold']) + ' ')


def isAlphabetWord(word):
    """
    This function checks the word for the absence of digits and symbols
    """
    for char in word:
        if char.isalpha():
            continue
        else:
            return False
    return True


def isCharInWord(char, word):
    return [index for index, letter in enumerate(word) if letter == char]


def start1PlayerMode():
    numberOfStrings = 0
    with open('words.txt', 'r') as wordsFile:
        for line in wordsFile.readlines():
            numberOfStrings += 1
            line = line

    stringNumber = randint(1, numberOfStrings)
    with open('words.txt', 'r') as wordsFile:
        for i in range(stringNumber):
            string = wordsFile.readline()
            i = i

    secretWord = string.split()[1]
    print(secretWord)

    return secretWord.upper()


def start2PlayerMode():
    """
    This function starts a game in 2-player mode
    """

    # Message
    print('\n' + colored('Let\'s start ', on_color='on_cyan') + \
        colored('2-player', 'white',on_color='on_blue', attrs=['bold']) + \
        colored(' mode game', on_color='on_cyan') + '\n')

    # Ask the first player to choose a word
    secretWord = input(colored('Player #1 please type your word (except "exit"):', on_color='on_cyan') + ' ')
    while not secretWord or not isAlphabetWord(secretWord) or secretWord.upper() == 'EXIT':
        secretWord = input(colored('You must to type the word without digits and symbols (and not "exit" word):', 'white', on_color='on_red') + ' ')
    return secretWord.upper()


def drawLettersFromList(charsList):
    """
    This function prints letters from the lists like ['a', 'b', ...]
    in a pretty way
    """
    for i in range(len(charsList)):
        if (i + 1) % 7 == 0:
            print('| ' + charsList[i] + ' |')
            print('-----------------------------')
        else:
            print('| ' + charsList[i] + ' ', end='')
    print('|\n')


def drawGameStatus(word, used, unused, lives):
    """
    This function draws the gallows with a man, status of the secret word,
    already used and yet unused letters
    """

    # Clear the screen
    # print(chr(27) + "[2J")
    
    # Draw the gallows
    if lives == 6:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |        ?\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 5:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (^,^)\n' + \
            '  |       (-)\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 4:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (o,o)\n' + \
            '  |       (-)\n' + \
            '  |       -#-\n' + \
            '  |      (   )\n' + \
            '  |       \\ /\n' + \
            '  |        |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 3:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (o,o)\n' + \
            '  |       (^)\n' + \
            '  |       -#-\n' + \
            '  |     /(   )\n' + \
            '  |    /  \\ /\n' + \
            '  |        |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 2:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (O,O)\n' + \
            '  |       (^)\n' + \
            '  |       -#-\n' + \
            '  |     /(   )\\\n' + \
            '  |    /  \\ /  \\\n' + \
            '  |        |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 1:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (O,O)\n' + \
            '  |       (O)\n' + \
            '  |       -#-\n' + \
            '  |     /(   )\\\n' + \
            '  |    /  \\ /  \\\n' + \
            '  |        |\n' + \
            '  |       /\n' + \
            '  |      /\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )
    elif lives == 0:
        print(
            '  __________\n' + \
            '  |        |\n' + \
            '  |        |\n' + \
            '  |       _?_\n' + \
            '  |      (x,x)\n' + \
            '  |       (x)\n' + \
            '  |       -#-\n' + \
            '  |     /(   )\\\n' + \
            '  |    /  \\ /  \\\n' + \
            '  |        |\n' + \
            '  |       / \\\n' + \
            '  |      /   \\\n' + \
            '  |\n' + \
            '  |\n' + \
            '__|__'
        )

    # Draw the status of the secret word
    print('\n')
    for char in word:
        if char != '_':
            print(colored(char, attrs=['bold']) + ' ', end='')
        else:
            print(char + ' ', end='')
    print('\n')
    
    # Draw unused letters
    print('UNUSED LETTERS')
    drawLettersFromList(unused)

    # Draw used letters
    print('USED LETTERS')
    drawLettersFromList(used)


def game(secretWord):
    """
    The game itself
    """
    
    # Options of guessing message
    guessMessages = [
        'Try to guess a letter: ',
        'Letter or whole word maybe? ',
        'What the letter will we check? ',
        'Make your move: ',
        'Let\'s try: '
    ]

    # Options of good message
    goodChoice = [
        'Yeah! You are right!',
        'Good job!',
        'Very good!',
        'Nice!',
        'Soon we\'ll win!'
    ]

    # List of already used letters
    usedChars = []
    for char in range(26):
        usedChars.append(' ')
        char = char # For avoiding IDE warning
    
    # List of unused letters
    unusedChars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', \
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    # Initial status of the secret word
    dashedWord = []
    for char in secretWord:
        dashedWord.append('_')

    # Number of lives of the guessing Player
    lives = 6

    initialMessage = ''

    # Cycle of the game
    while True:

        # Draw current status of the game
        print(chr(27) + "[2J")
        print(initialMessage)
        drawGameStatus(dashedWord, usedChars, unusedChars, lives)

        # Loss of the player
        if lives == 0:
            print(colored('GAME OVER', 'white', 'on_red') + f' The word {secretWord} was hidden.')
            break

        # The player win
        elif '_' not in dashedWord:
            print(colored('! YOU WIN !', on_color='on_green'))
            break

        # The player try to guess
        else:
            guessMessage = choice(guessMessages)
            guessLetter = input(guessMessage)

            # Processing received inputs from the player
            while True:
                if not guessLetter:
                    guessLetter = input(colored('Enter a single letter or the whole word:', 'white', 'on_red') + ' ')
                if len(guessLetter) == 1:
                    if guessLetter.upper() in usedChars:
                        guessLetter = input(colored(f'You already used {guessLetter.upper()} letter,', 'white', 'on_red') + '\n' + \
                            colored('try another one:', 'white', 'on_red') + ' ')
                        continue
                    elif guessLetter.isalpha():
                        break
                    else:
                        guessLetter = input(colored(f'{guessLetter} is not a letter, be smarter:', 'white', 'on_red') + ' ')
                        continue
                elif len(guessLetter) > 1:
                    if not isAlphabetWord(guessLetter):
                        guessLetter = input(colored(f'{guessLetter} can not be a winnig word,', 'white', 'on_red') + '\n' + \
                            colored('there are prohibited symbols here. Be smarter: ', 'white', 'on_red') + ' ')
                        continue
                    elif len(guessLetter) != len(secretWord) and guessLetter.upper() != 'EXIT':
                        guessLetter = input(colored(f'{guessLetter} can not be a winnig word,', 'white', 'on_red') + '\n' + \
                            colored('it doesn\'t match the number of letters. Be smarter: ', 'white', 'on_red') + ' ')
                        continue
                    else:
                        break
            
            # If 'exit' entered
            workingValue = guessLetter.upper()
            if workingValue == 'EXIT':
                print(colored('Good Bye!', on_color='on_green'))
                break

            # If entered single letter
            elif len(workingValue) == 1:
                indexOfLetter = unusedChars.index(workingValue)
                unusedChars[indexOfLetter] = ' '
                usedChars[indexOfLetter] = workingValue
                if workingValue not in secretWord:
                    initialMessage = colored('Guessed wrong', 'red', attrs=['bold'])
                    lives -= 1
                    continue
                else:
                    indexesOfWorkingValueInSecretWord = isCharInWord(workingValue, secretWord)
                    for index in indexesOfWorkingValueInSecretWord:
                        dashedWord[index] = workingValue
                    initialMessage = colored(choice(goodChoice), 'green', attrs=['bold'])
                    continue
            
            # If word entered
            else:
                if workingValue == secretWord:
                    for index in range(len(secretWord)):
                        dashedWord[index] = secretWord[index]
                else:
                    initialMessage = colored('That\'s not the right word', 'red', attrs=['bold'])
                    lives -= 1


def main():

    # Greetings to player(s)
    greetings = colored('Welcome to the Hangman Game!', 'white', on_color='on_blue', attrs=['bold'])
    print(f'\n{greetings}\n')
    
    # Start chosen game mode
    gameMode = chooseGameMode()
    if gameMode == 1:
        secretWord = start1PlayerMode()
    elif gameMode == 2:
        secretWord = start2PlayerMode()

    # Start the game
    game(secretWord)
    
    
main()
