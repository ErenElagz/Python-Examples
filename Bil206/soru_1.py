def Func():
    x=1
    y=4
    if x ==1:
        print( ( " " * y ) +(x * " * " ) )
        x = x + 2 
    
    while x <= 9:
        y= y-2
        print( " " * (y-2) +  " " * x)
        x = x+2

        Func()

Func()