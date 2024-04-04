import json
class Base():
    def __init__(self, name:str, stolbci:list[str]) -> None:
        self.name = name
        self.kluchi = stolbci
        self.inf = {}
        self.glavni_kluch = stolbci[0]
        try:
            self.__old_file()
        except FileNotFoundError:
            self.__new_file()

    def __old_file(self):
        file = open(self.name, 'r', encoding='UTF-8')
        self.inf = json.load(file)
        file.close()

    def __new_file(self):
        file = open(self.name, 'w', encoding='UTF-8')
        json.dump({}, file)
        file.close()


    def sozdanie(self, new_zapis:dict):
        if self.proverka(new_zapis[self.glavni_kluch]) is False:
            self.inf[len(self.inf)] = new_zapis
        else:
            raise ValueError

    def obnovlenie(self, zapis:dict):
        if self.proverka(zapis[self.glavni_kluch]) is False:
            raise ValueError
        else:
            for i in (self.inf):
                if self.inf[i][self.glavni_kluch] == zapis[self.glavni_kluch]:
                    self.inf[i] = zapis

    def schitivanie(self,glavn_znach):
        if self.proverka(glavn_znach) is False:
            raise ValueError
        else:
            for i in self.inf:
                if self.inf[i][self.glavni_kluch] == glavn_znach:
                    return self.inf[i]
            

    def save(self):
        file = open(self.name, 'w')
        json.dump(self.inf, file)
        file.close()

    def proverka(self, param_poisk):
        for i in self.inf:
            if self.inf[i][self.glavni_kluch] == param_poisk:
                return True
        return False

x = Base('wert', ['Name', 'money'])
# y = Base('cars', ['number', 'color', 'marka'])

# x.sozdanie({'Name':'Oleg', 'money':'123'})
# x.sozdanie({'Name':'Masha', 'money':'12'})
print(x.schitivanie('Oleg'))
# y.sozdanie({'number':'q1215rt', 'color':'blue', 'marka':'lexus'})
x.save()
# y.save()
# z = Base('pfpkf', ['class', 'life'])
# z.save()
