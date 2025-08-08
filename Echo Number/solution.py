class EchoNumber:
    def __init__(self, num=0):
        self.num = num

    def input(self):
        while True:
            try:
                self.num = int(input())
                break
            except ValueError:
                print("Enter an integer!")

    def output(self):
        return str(self.num) * self.num
    

n = EchoNumber()
n.input()
print(n.output())
        