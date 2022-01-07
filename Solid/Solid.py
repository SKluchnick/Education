class StringWriter:

    def generateMessage(self):
        pass


class InputData:

    def getParameters(self):
        pass


class InputDataFromConsole(InputData):

    def getParameters(self):
        enter = input().lower().strip()
        return enter


class Bob(StringWriter):
    def generateMessage(self):
        super().generateMessage()
        return print("Hello Bob")


class TemplateHandler:
    dct = {}

    def templateHandler(self):
        self.dct.update({'bob': Bob()})
        return self.dct

    def getMap(self, name):
        i = self.templateHandler()
        i.get(name)
        return i


t = TemplateHandler()
res = t.getMap('bob')
print(res)


class MessageImplement:
    inputDataFromConsole = InputDataFromConsole()
    templateHandler = TemplateHandler()

    def getString(self):
        outPut = ''
        while True:
            print('Would you like to write name? (y/n)')
            enter = input().lower().strip()
            if not self.isContinue(enter):
                break
            lst = self.splitEnteredParameters()
            numOne = self.checkInputSecond(lst[0])
            if numOne.strip().lower() == 'bob':
                outPut = self.templateHandler.getMap(numOne)
                break
        return outPut

    def splitEnteredParameters(self):
        num = 1
        while True:
            print('Please write 1 name <name> only string')
            lst = self.inputDataFromConsole.getParameters().strip().lower().split(" ")
            if len(lst) != num:
                self.inputDataFromConsole.getParameters()
            else:
                break
        return lst

    def checkInputSecond(self, value):
        while True:
            for i in range(len(value)):
                while not value[i].isalpha():
                    print('1Must be only one word')
                    break
            if len(value) == 0:
                print('2Must be only one word')
                break
            if value.strip().lower() != 'bob':
                print('Name does not exist')
                break
            else:
                break
        return value

    def isContinue(self, value):
        return value.lower() == 'y' or value.lower() == 'yes'


messageImplement = MessageImplement()
messageImplement.getString()
