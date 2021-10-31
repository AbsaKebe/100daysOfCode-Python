def division(nbr,max):
    for i in range(max):
        if i%2==0:
            print("{}/{} = {}".format(i,nbr,i/nbr))
division(4,20)