
class prime:
    def integer(self, number):
        flag = 0
        for i in range(2, number//2+1):
            if number % 2 == 0:
                flag = 1
                break
        return flag

Prime = prime()
print("gooooooooood")
