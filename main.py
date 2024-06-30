def main():

    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """

    for number in range(N+1):
        result.append(2 ** number)
        
    print(result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
    