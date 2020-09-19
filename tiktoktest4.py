import re

class test4():
    def inputdata(self):
        self.data = []
        data = input()
        n = 1
        while data != '':
            data = re.split(r'\s', data)
            if n > 10 or len(data) > 10:
                print("out of size")
                return
            n += 1
            for i in data:
                if not re.match(r'[0-2]', i):
                    print("data is error", i)
                    return
            data = [int(x) for x in data]
            self.data.append(data)
            data = input()
        m = 0
        c = self.change()
        while c is True:
            m += 1
            c = self.change()

        if m == 0:
            return -1
        else:
            return m

    def change(self):
        self.cdata = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == 2:
                    self.find(self.data, i, j, len(self.data)-1, len(self.data[i])-1)

        if self.cdata != []:
            for x, y in self.cdata:
                self.data[x][y] = 2
            return True
        else:
            return False

    def find(self, data, x, y, lx, ly):
        if x-1>=0 and data[x-1][y] == 1:
            self.cdata.append((x-1,y))
        if x+1<=lx and data[x+1][y] == 1:
            self.cdata.append((x+1, y))
        if y-1>=0 and data[x][y-1] == 1:
            self.cdata.append((x, y-1))
        if y+1<=ly and data[x][y+1] == 1:
            self.cdata.append((x, y+1))

if __name__ == '__main__':
    t = test4()
    test = t.inputdata()
    print(test)

