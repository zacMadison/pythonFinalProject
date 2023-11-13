import pandas as pd



# seems useful ->(https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php)
# todo: look for the year it was posted because this is the worst organized database I've ever seen
# Next: Make work with more months - done
# Next Next: use all databases - done?
# Next Next Next: fetch the words used in the tweets



def findMonth():
    # set up variable to read the csvs
    filePath = 'BTCP1.csv'
    currentFile = 1
    # dataFrames are used by the module pandas, the reason I chose this module over csv is that it has more functionality
    # attempted to solve dtype error: unsuccessful https://stackoverflow.com/questions/24251219/pandas-read-csv-low-memory-and-dtype-options
    dataFrame = pd.read_csv(filePath, sep=',', dtype={'created_at': str})

    #used for loop
    completed = 0

    # row will be incremented through each loop
    row = 0
    date_column = 'created_at'
    while completed == 0:
        row += 1


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
            row = 0
            print("reached end of file, changing to next file")
            filePath = "BTCP" + str(currentFile) + ".csv"
            dataFrame = pd.read_csv(filePath, sep=',', dtype={'created_at': str})





findMonth()