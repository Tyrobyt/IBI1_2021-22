# 3. Chocolate bar affordability calculator
# write a function contains 2 paramenters
# 3.1 the total money that the user has (total_money)
# 3.2 the price of one chocolate bar (price)
# the function should return (1) the number of bars that can be bought and (2) the change that will be left over.
def calculator(x,y):
    """

    :param x: the price of chocolate
    :param y: the total money
    :return: 1.the number of bars that can be brought 2. the change that will be left over

    """
    x=int(x)
    y=int(y)
    print('the number of chocolate bars we can brought:'+str(y//x))
    print('the charge will be left over:'+str(y%x))
    return (x,y)
# here is an example
y=200
x=21
calculator(x,y)
# input your data here
y=input("Total money = ")
x=input("Price=")
calculator(x,y)


