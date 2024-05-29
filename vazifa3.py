'''homework 4'''
class Datas:


    objects = []
    data_id = 0


    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = Datas.data_id(id)
        Datas.data_id(self.id) + 1
        self.objects.append(self)



    
    def __iter__(self, data_id):
        self.data_id = 0
        return data_id

    



    def __next__(self):
        if self.data_id <= len(self.__class__.objects):
            objects = self.__class__.objects[self.data_id]
            self.data_id += 1
            return objects
        else:
            raise StopIteration()
        

    @classmethod
    def datas_id(cls):
        for obj in cls.objects:
            return [obj.id ]
        
Datas('Abdulaziz')
Datas('Asror')
Datas('Raxmonjon')
Datas('Farhod')
Datas('Ayubxon')
Datas('Muhammaddillo')
Datas('Sardor')
Datas('Shoxobbos')
    
datas_id = Datas.data_id()

print("Data id:", datas_id)