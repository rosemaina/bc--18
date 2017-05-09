class Car(object):

    def __init__(self, name='General', model='GM' ,car_type='honda' ):

        self.car_type = car_type
        self.model = model
        self.name = name

        #Default speed of a car
        self.speed = 0

        #Unless otherwise,default name is general
        #Porshe and Koenigsegg have 2 doors while the default is 4
        if name== 'Porshe' or name== 'Koenigsegg':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

            #No of wheels in the trailer is 8 while in the saloon is 4
        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def doors(self, num_of_doors):
        pass

    def drive(self, moving_man):
        return moving_man

    def drive(self, speed):
        if self.car_type == 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed

        return self

    def wheels(self, num_of_wheels):
        return num_of_wheels


    def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
            return True

pass