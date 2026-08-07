def bottle_verse ():
    s = input ('How long input is ?')
    s = int (s)
    for i in range (s, 0, -1 ):
        print( i, ' bottles of beer on the wall')
        print( i, ' bottles of beer' )
        print('Take one down, pass it around')
        print(i - 1, ' bottles of beer on the wall')

bottle_verse()