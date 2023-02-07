class List_1:
    pass 

class Prime:
    def mass(self):
        self.list_1 = []
        self.p1 = List_1()
        self.size = int(input())
        self.first = self.p1 
        for i in range(self.size):
            self.p1.num = int(input())
            self.p1.next = List_1()
            self.p1 = self.p1.next 

        self.p1.next = "stop"
        self.p1 = self.first 

    def checker(self, num):
        flag = True
        if num == 1:
            return False 
        for i in range(2, num):
            if num % i == 0:
                return False 
        return flag 

    def prime(self):
        for i in range(self.size):
            if self.checker(self.p1.num):
                self.list_1.append(self.p1.num)
                self.p1 = self.p1.next
            else:
                self.p1 = self.p1.next 
                
                
        print(*self.list_1)


p2 = Prime()
p2.mass()
p2.prime()

