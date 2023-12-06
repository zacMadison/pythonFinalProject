import pandas as pd, json, nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# pandas library documentation : https://pandas.pydata.org/docs/user_guide/index.html#user-guide

programRunning = 1
# This loads the list of exclusions so you can sto running the program but keep the list, if it is not present it creates one
try:
    with open('exclusions.txt', 'r') as fp:
        excludedWords = json.load(fp)
except json.decoder.JSONDecodeError:
        excludedWords = ['the', 'bitcoin', 'a', 'and', 'btc', 'to', 'of', 'is', 'in', 'for', 'on', '-', 'i', 'with', 'it', 'that', 'at', '|', 'be', 'will', 'this', 'are', 'as', 'my', 'via', 'by', 'your', 'not', 'have', 'or', 'from', 'has', 'but', 'we', 'an', 'was', 'you', 'crypto', 'blockchain']
except FileNotFoundError:
    excludedWords = ['the', 'bitcoin', 'a', 'and', 'btc', 'to', 'of', 'is', 'in', 'for', 'on', '-', 'i', 'with', 'it',
                     'that', 'at', '|', 'be', 'will', 'this', 'are', 'as', 'my', 'via', 'by', 'your', 'not', 'have',
                     'or', 'from', 'has', 'but', 'we', 'an', 'was', 'you', 'crypto', 'blockchain']

# program starts by asking if user would like to use sentiment analysis
SentAnalysis = input("Would you like to use sentiment analysis? y/n: ")

# This is the program starts, allows the user to change the exclusions list
def menu():

    inMenu = 1
    while inMenu == 1:
        userChoice = input(
            "Welcome to the database word scraper\nIf you want to see or change the list of excluded words, type 'E'"
            "\nIf you want to continue to the program press 'c'\nTo exit the program press Enter\n")
        # allows user to view and change exclusion list
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
            with open('exclusions.txt', 'w') as fp:
                json.dump(excludedWords, fp)
            exit()



# recieve input from user for which month to use
# if the database is zero program should stop running
def recieveMonth():
    # Lists that contain the corresponding databases for faster processing
    may = [3,0]
    jun = [3, 4, 0]
    jul = [4, 5, 0]
    aug = [5, 6, 0]
    sep = [6, 7, 0]
    oct = [7, 8, 0]
    nov = [8, 0]
    receivingInput = 1
    # allows the user to enter a month
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
        elif targetMonth.lower() == "exit":
            with open("exclusions.txt", 'w') as fp:
                json.dump(excludedWords, fp)
            exit()
        else:
            print("Invalid input, please try again.")
    wordAmount = int(input("How many words do you want: "))
    return targetMonth, databases, wordAmount

# This finds what the most repeated words are and prints them out
# This will use a loop to find what the most repeated word is, and at the end it pops the item, lowers the amount of
# remaining words and does it again until all the words have been printed
def sortWords(words, wordNum):
    sortedDict = {}
    # prevents the program from returning an empty word
    words.pop("")
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



# finds the target month in the database and then read the tweet to find how often each word is repeated
def findMonth(database, targetMonth):
    global num_of_words, SentAnalysis
    print("processing, please wait...")
    # set up for variables
    # sets up for sentiment analysis
    sia = SentimentIntensityAnalyzer()
    count = 0
    # used to remove punctuation
    punc = '''!()-[]{};:'"\,<>./?@#%^&*_~'''
    # tracks how many databases have been searched
    currentDatabase = 0
    filePath = 'BTCP' + str(database[currentDatabase]) + '.csv'

    # This program uses pandas to read file, as it is the best way I found to search the files
    dataFrame = pd.read_csv(filePath, dtype={"created_at": str}, low_memory=False)

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
        # checks to see if the current row is in the current row
        if targetMonth in dataFrame.at[row, date_column]:
            # sentiment analysis
            tweet = dataFrame.at[row, tweet_column]
            if SentAnalysis.lower() == "y":
                currentSent = sia.polarity_scores(tweet)
                if count == 0:
                    totalSent = currentSent
                else:
                    totalSent['neg'] += currentSent['neg']
                    totalSent['pos'] += currentSent['pos']
                    totalSent['neu'] += currentSent['neu']
                count += 1
            # following code processes the individual tweets
            tweet = tweet.split()
            # this cycles through all words in the tweet
            for word in tweet:
                # Replaces punctuation that may be connected to a word we want
                for letter in word:
                    if letter in punc:
                        word = word.replace(letter, "")
                # if word is already been found it increments the connected value, otherwise create a new entry
                if word.lower() not in excludedWords:
                    if word in wordsRepeated:
                        wordsRepeated[word] += 1
                    else:
                        wordsRepeated[word] = 1
        # this  will change the file, or end the program if it is already on teh last database (database = 0)
        if row == len(dataFrame) - 1:
            row = 0
            currentDatabase += 1

            if database[currentDatabase] == 0:

                completed = 0
                sortWords(wordsRepeated, num_of_words)
                # prints sentiment analysis
                if SentAnalysis.lower() == "y":
                    print("Tweets in this months were:\n" + str(
                        round(totalSent['pos'] * 100 / count, 2)) + "% positive\n" + str(
                        round(totalSent['neg'] * 100 / count, 2)) + "% negative\n" + str(
                        round(totalSent['neu'] * 100 / count, 2)) + "% neutral")
            else:
                filePath = "BTCP" + str(database[currentDatabase]) + ".csv"
                dataFrame = pd.read_csv(filePath, dtype={"created_at": str}, low_memory=False)


menu()
