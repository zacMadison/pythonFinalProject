import pandas as pd
# pandas library documentation : https://pandas.pydata.org/docs/user_guide/index.html#user-guide

programRunning = 1
excludedWords = ['the', 'bitcoin', 'a', 'and', 'btc', 'to', 'of', 'is', 'in', 'for', 'on', '-', 'i', 'with', 'it', 'that', 'at', '|', 'be', 'will', 'this', 'are', 'as', 'my', 'via', 'by', 'your', 'not', 'have', 'or', 'from', 'has', 'but', 'we', 'an', 'was', 'you', 'crypto', 'blockchain']


# todo: let users choose between links and words

def menu():

    inMenu = 1
    while inMenu == 1:
        userChoice = input(
            "Welcome to the database word scraper\nIf you want to see or change the list of excluded words, type 'E'"
            "\nIf you want to continue to the program press 'c'\nTo exit the program press Enter\n")
        if userChoice.upper() == "E":
            userChoice = input("This is the current list of excluded words \nIf you would like to add a word type 'A'\nIf you would like to remove a word type 'R'\nIf you would like to go back press Enter \n"
                               "______________________________________________\n" + str(excludedWords) + '\n')
            if userChoice.upper() == "A":
                excludedWords.append(input("What would you like to add to the list: "))
            elif userChoice.upper() == "R":
                excludedWords.remove(input("What would you like to remove from the list: "))
        elif userChoice.upper() == "C":

            global targetMonth, databases, num_of_words
            while programRunning == 1:
                targetMonth, databases, num_of_words = recieveMonth()
                findMonth(databases, targetMonth)
        elif userChoice == "":
            exit()



# recieve input from user for which month to use
# if the database is zero program should stop running
def recieveMonth():
    # Lists that contain the corresponding databases for faster processing, the user will input what month they want
    # and it will use the list to read the corresponding databases, only use may - Nov 2019
    may = [3,0]
    jun = [3, 4, 0]
    jul = [4, 5, 0]
    aug = [5, 6, 0]
    sep = [6, 7, 0]
    oct = [7, 8, 0]
    nov = [8, 0]
    receivingInput = 1
    months = [may, jun, jul, aug, sep, oct, nov]
    while receivingInput == 1:
        targetMonth = input("\nIf you want to go back press 'B', if you want to exit the program type 'exit' Enter\n\nPlease input a month between May and Nov by typing the first 3 letter of the month: ")
        if targetMonth.lower() in "may":
            targetMonth = "May"
            databases = may
            receivingInput = 0
        elif targetMonth.lower() in "jun":
            targetMonth = "Jun"
            databases = jun
            receivingInput = 0
        elif targetMonth.lower() in "jul":
            targetMonth = "Jul"
            databases = jul
            receivingInput = 0
        elif targetMonth.lower() in "aug":
            targetMonth = "Aug"
            databases = aug
            receivingInput = 0
        elif targetMonth.lower() in "sep":
            targetMonth = "Sep"
            databases = sep
            receivingInput = 0
        elif targetMonth.lower() in "oct":
            targetMonth = "Oct"
            databases = oct
            receivingInput = 0
        elif targetMonth.lower() in "nov":
            targetMonth = "Nov"
            databases = nov
            receivingInput = 0
        elif targetMonth.lower() == "b":
            menu()
        elif targetMonth == "exit":
            exit()
        else:
            print("Invalid input, please try again.")
    wordAmount = int(input("How many words do you want: "))
    return targetMonth, databases, wordAmount


def sortWords(words, wordNum):
    sortedDict = {}

    print("Word | Occurrences"
          "\n---------------")
    while wordNum != 0:
        keys = list(words.keys())
        Highest = keys[0]
        for word in words:
            if words[word] > words[Highest]:
                Highest = word
        print(Highest + "    " + str(words.pop(Highest)))

        wordNum -= 1
    return sortedDict



def findMonth(database, targetMonth):
    global num_of_words
    print("processing, please wait...")
    # set up variable to read the csvs
    currentDatabase = 0
    filePath = 'BTCP' + str(database[currentDatabase]) + '.csv'

    # dataFrames are used by the module pandas, the reason I chose this module over csv is that it has more functionality
    # attempted to solve dtype error: unsuccessful https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options
    dataFrame = pd.read_csv(filePath)

    # used for loop
    completed = 1

    # dictionary used to count repeated words
    wordsRepeated = {}
    # row will be incremented through each loop
    row = 0
    date_column = 'created_at'
    tweet_column = 'text'
    while completed == 1:
        row += 1
        # running this also returns dtype error, doesn't seem to affect output right now
        # This checks if the current row is for the target month
        if targetMonth in dataFrame.at[row, date_column]:
            tweet = dataFrame.at[row, tweet_column]
            tweet = tweet.split()
            # this cycles through all words in the tweet
            for word in tweet:
                # removes hashtags to prevent the same word popping up twice and for readability
                if '#' in word:

                    word = word.replace('#', '')

                if word.lower() not in excludedWords:
                    if word in wordsRepeated:
                        wordsRepeated[word] += 1
                    else:
                        wordsRepeated[word] = 1

        # This is for testing will be used to change files later

        if row == len(dataFrame) - 1:
            row = 0
            currentDatabase += 1

            if database[currentDatabase] == 0:
                completed = 0
                wordsRepeated = sortWords(wordsRepeated, num_of_words)




            else:
                filePath = "BTCP" + str(database[currentDatabase]) + ".csv"
                dataFrame = pd.read_csv(filePath)


menu()
