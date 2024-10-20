class Element():
    def __init__(self, name, beating, beaten_by):
        self.name = name
        self.beating = beating
        self.beaten_by = beaten_by

    def isbeating(self, i):
        return self.beating == i

    def isequal(self, i):
        return self.name == i


rock = Element('Камень', "Ножницы", "Бумага")
paper = Element("Бумага", 'Камень', "Ножницы")
scissors = Element("Ножницы", "Бумага", 'Камень')
