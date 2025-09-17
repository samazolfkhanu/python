class Employee:
    def __init__(self,name,age,position):
        self.name=name
        self.age=age
        self.position=position
    def __repr__(self):
        return f"Name: {self.name}\tAge:{str(self.age)}\tPosition:{self.position}"