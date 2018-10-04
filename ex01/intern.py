class Intern():

    def __init__(self, name = None):
        if name == None:
            name = "My name? I’m nobody, an intern, I have no name."

        self.name = name

    def __str__(self):
        return self.name

    class Coffee():
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee()


if __name__ == '__main__':

    nobody = Intern()
    mark = Intern('Mark')

    print(mark)
    print(nobody)

    print(mark.make_coffee())

    nobody.work()
