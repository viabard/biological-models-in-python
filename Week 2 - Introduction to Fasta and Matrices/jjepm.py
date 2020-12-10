def inputCC(thingToAsk, tipe, errorMessage='Input not castable...'):
    """
    input cast check.

    thingToAsk is a String that uses input() to ask the user.
    tipe is a type used for casting, checking to see if the input is correct.
    errorMessage is a customisable string that is printed if the casting results in an error.
    """
    y = True 
    while(y is True):
        x = input(thingToAsk)
        try:
            x = tipe(x) 
            y = False
        except:
            print(errorMessage)
    return x