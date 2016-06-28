for i in range(1,100):
    if i==1:
        print("{} is not a prime".format(i));
    else:
        j = 2;
        isPrime = True;
        while i >= j*j:
            if i%j == 0:
                isPrime = False;
                break;
            else:
                j += 1;
        if isPrime == True:
            print("{} is prime".format(i));
        else:
            print("{} is not a prime".format(i));