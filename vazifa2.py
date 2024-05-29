'''Homework 3'''


class Datas:




    objects = []
    counter = 0





    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.objects.append(self)


    
    def __iter__(self, **args ):
        return self
    


    def __next__(self, *args ):
        try:
            object = self.objects[self.counter]
            self.counter += 1
            return object.first_name and object.last_name
        except IndexError:
            self.counter = 0
            raise StopIteration()
        

Datas('Abdulaziz')
Datas('Asror')
Datas('Raxmonjon')
Datas('Farhod')
Datas('Ayubxon')
Datas('Muhammaddillo')
Datas('Sardor')
Datas('Shoxobbos')    



bro = list(filter(lambda x:x,   Datas('')))

print(bro)