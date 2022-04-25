# 2. ZJE human resources database
# create a class called staff
class staff (object):
    def __init__(self,x,y,z): # use x to represent name, location and role
        self.x = x
        self.y = y
        self.z = z
        print("Name : "+x+"\n"+"Location : "+y+"\n"+"Role : "+z)
#given an example
a = staff('Hu, Maizhi', 'International Campus', 'student')
print(a)
