def main():
    celcius = input('What is the temperature in Celcius?')
    fahrenheit = (( 9 * int(celcius) / 5 ) + 32)
    print ('Fahrenheit:', format(fahrenheit, '.2f'))
    """
    ##################################################
    # Complete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
