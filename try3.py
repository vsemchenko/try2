from onemore import Employee


class ITEmployee(Employee):
    def __init__(self, *args, **kwargs):
        Employee.__init__(self,*args,**kwargs)
        self.skils = []


    def add_skill(self,new_skill):
        self.skils.append(new_skill)





