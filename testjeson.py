class Practice():
    def __init__(self):
        self.word = 'hello'


test = Practice()
print(test.word)

class newPractice(Practice):
    def __init__(self):
        super().__init__()
        self.number = 9


test = newPractice()
print(test.word,test.number)