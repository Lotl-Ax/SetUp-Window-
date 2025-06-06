'''
define a class called vegetable with following attributes and methods
* name
* colour
* weight

% set_colour
% get_colour
% set_weight
% get_weight

'''

# class definition

# main

# instantiate the class, call it my_veg and give it a name

# set colour and weight

'''
inheritance ?
'''

class vegetable():

    def __init__(self, name , colour, weight):
        self.name = name
        self.colour = colour
        self.weight = weight

    def set_colour(self, colour):
        self.colour = colour

    def get_colour(self):
        return self.colour
    
    def set_weight(self, weight):
        self.weight = weight

    def get_weight(self):
        return self.weight
    


class Potato(vegetable):
    def __init__(self, name, colour, weight, nobbles):
        # super(vegetable).__init__()
        super().__init__(name, colour, weight)

        self.nobbles = nobbles

    def set_nobbles(self, nobbles):
        self.nobbes = nobbles

    def get_nobbles(self):
        return self.nobbles


veg_name = 'Carrot'
veg_colour = 'Blue'
veg_weight = 40
my_veg = vegetable(veg_name, veg_colour, veg_weight)
print(f'{my_veg.get_colour()}, {my_veg.get_weight()}')



potato_name = 'Potato'
potato_colour = 'pink'
potato_weight = 500
potato_nobbles = 7
my_potato = Potato(potato_name, potato_colour, potato_weight, potato_nobbles)
# print(my_potato.nobbles)
print(f'{my_potato.get_colour()}, {my_potato.get_weight()}, {my_potato.get_nobbles()}')    