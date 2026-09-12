class MyStack(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack2.append(x)

        while self.stack1:
            self.stack2.append(self.stack1.pop(0))
        self.stack1,self.stack2=self.stack2,self.stack1
    def pop(self):
        return self.stack1.pop(0)

    def top(self):
        return self.stack1[0]

    def empty(self):
        return not self.stack1