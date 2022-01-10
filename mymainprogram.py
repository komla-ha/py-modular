#mymainprogram.py


from mycalculator import \
    adder as new_add, \
    substracter as new_sub 
from myrandom import gen_random_1p,gen_random_2p

def maincall():

    x = gen_random_1p()
    y = gen_random_2p()

    added = new_add(x,y)
    substracted = new_sub(x,y)

    print("x: {}, y: {}".format(x,y))
    print("y: {}".format(y))

    print("Addition is {}".format(added))
    print("Substraction is {}".format(substracted))
    print(globals())
if __name__ == "__main__":
    maincall()

