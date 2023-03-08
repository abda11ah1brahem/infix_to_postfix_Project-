class Stack:
    def __init__(self):
        self.item=[]
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def isEmpty(self):
        return (self.item==[])
    def peek(self):
        return self.item[-1]
    def __str__(self):
        return str(self.item)
    def infixToPostfix(infixexprt):
        prec={}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        opStack=Stack()
        postfixList=[]
        tokenList=infixexprt.split()
        for token in tokenList:
            if token in "A,B,C,D,E,F,G,H "and token in "0,1,2,3,4,5,6,7,8,9":
                postfixList.append(token)
            elif token =="(":
                opStack.push(token)
            elif token ==")":
                topToken=opStack.pop()
                while topToken != "(":
                    postfixList.append(topToken)
                    topToken=opStack.pop()
            else:
                while (not opStack.isEmpty()) and (prec[opStack.peek()]>= prec[token]):
                    postfixList.append(opStack.pop())
                opStack.push(token)
        while not opStack.isEmpty():
            postfixList.append(opStack.pop())
        return "".join(postfixList)
    print(infixToPostfix(" A * B + C • D"))