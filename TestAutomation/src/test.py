
class Employee:
    name = ''

    def __init__(self, n):
        self.name = n

    def __len__(self):
        return len(self.name)


e = Employee('Pankaj')
print(e.__len__());
print('employee object length =', len(e))

input = "Hello World"
a = input.split(' ')
for x in a:
    print(x[::-1])
