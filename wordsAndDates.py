import pandas as pd






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
        # todo: check for all months or include user input to decide what month we are looking for, have
        # todo: the program scrape for words and place them in a list for the month they were in
        # seems useful ->(https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-12.php)
        # todo: also use the other databases that are not BTCP1


        # Note: dates are not all in order, best to continue interating loop after the month that is being looked for and find another way to end look
        # also, running this also returns dtype error, doesnt seem to affect output right now
        # this will add the words in post to a list in the future
        if "May" in dataFrame.at[row, date_column]:
            print("test")
        else:
            completed = 1
        row += 1


findMonth()