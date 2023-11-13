import pandas as pd


# todo: check for all months or include user input to decide what month we are looking for, have
# todo: the program scrape for words and place them in a list for the month they were in
# seems useful ->(https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php)
# todo: also use the other databases that are not BTCP1
# Next: Make work with more months
# Next Next: use all databases
# Next Next Next: fetch the words used in the tweets



def findMonth():
    # set up variable to read the csvs
    filePath = 'BTCP1.csv'

    # dataFrames are used by the module pandas, the reason I chose this module over csv is that it has more functionality
    dataFrame = pd.read_csv(filePath)

    #used for loop
    completed = 0

    # row will be incremented through each loop
    row = 1
    date_column = 'created_at'
    while completed == 0:
        # ISSUE: row starts at 7 then skips to 463568 and I have no clue why

        print(row)
        # Note: dates are not all in order, best to continue interating loop after the month that is being looked for and find another way to end look
        # also, running this also returns dtype error, doesnt seem to affect output right now
        # this will add the words in post to a list in the future
        if "Jan" in dataFrame.at[row, date_column]:
            print("Jan")
        elif "Feb" in dataFrame.at[row, date_column]:
            print("Feb")
        elif "Mar" in dataFrame.at[row, date_column]:
            print("Mar")
        elif "Apr" in dataFrame.at[row, date_column]:
            print("Apr")
        elif "May" in dataFrame.at[row, date_column]:
            print("May")
        elif "Jun" in dataFrame.at[row, date_column]:
            print("Jun")
        elif "Jul" in dataFrame.at[row, date_column]:
            print("Jul")
        elif "Aug" in dataFrame.at[row, date_column]:
            print("Aug")
        elif "Sep" in dataFrame.at[row, date_column]:
            print("Sep")
        elif "Oct" in dataFrame.at[row, date_column]:
            print("Oct")
        elif "Nov" in dataFrame.at[row, date_column]:
            print("Nov")
        elif "Dec" in dataFrame.at[row, date_column]:
            print("Dec")
        else:
            completed = 1

        # This is for testing will be used to change files later
        if row == len(dataFrame) - 1:
            print("reached end of file")
        row += 1


findMonth()