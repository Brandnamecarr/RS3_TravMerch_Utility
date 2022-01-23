import merchInfo

# driver code
def main():
    url = "https://runescape.wiki/w/Travelling_Merchant%27s_Shop"
    mg = merchInfo.merchGetter(url)

    _unformattedStock = []
    
    # calling the getTableData() method from the merchGetter class. 
    _unformattedStock = mg.getTableData()
    
    # method calls to get the current runedate from the TM website (url).
    _precleaningData = mg.getRunedate()
    date_cleaned = mg.cleanData(_precleaningData)

    # creating a string out of the elements from the date_cleaned list.
    date_string = " ".join(date_cleaned)

    # formatting for the batchfile, indicating the date.
    print()
    print("Runedate: " + str(date_string))
    # header section for what the items available are.
    print("The items available are: ")
    print()

    # counter for formatting in the batch file. 
    counter = 1
    for item in _unformattedStock:
        print("%s: %s" % (counter, item))
        counter = counter + 1
    
    # newline for formatting in the batch file. 
    print()


# invoking main
if __name__ == '__main__': main()