import re

class clock():
    def inputdata(self):
        self.data = []
        line = input()
        while line is not '':
            line = re.split(r'\s', line)
            line = [int(e) for e in line]
            self.data.append(line)
            line = input()
        self.inputnum()

    def inputnum(self):
        N = self.data[0][0]
        if N >= 100 or N <= 0:
            print("闹钟数量有误!")
        else:
            self.StartTime = []
            for i in range(N):
                self.cstarttime(i+1)
            self.outputtime()

    def cstarttime(self, n):
        stime = self.data[n]
        self.stcheck(len(stime), int(stime[0]), int(stime[1]))

    def stcheck(self, n, h, m):
        if h < 0 or h > 24:
            print("时间格式有误!")
        elif m < 0 or m > 60:
            print("时间格式有误!")
        elif n > 2:
            print("时间格式有误!")
        else:
            self.StartTime.append((h, m))

    def needtime(self):
        ntime = self.data[-2][0]
        if ntime < 0 or ntime > 100:
            print("输入时间有误请重新输入！")
        else:
            return ntime

    def lstarttime(self):
        lstime = self.data[-1]
        h, m = self.lstcheck(len(lstime), int(lstime[0]), int(lstime[1]))
        return h, m

    def lstcheck(self, n, h, m):
        if h <= 0 or h > 24:
            print("时间格式有误!")
        elif m <= 0 or m > 60:
            print("时间格式有误!")
        elif n > 2:
            print("时间格式有误!")
        else:
            return h, m

    def checktime(self):
        ntime = self.needtime()
        A, B = self.lstarttime()
        self.otime = []
        for Hi, Mi in self.StartTime:
            if (A * 60 + B) - (Hi * 60 + Mi) >= ntime:
                self.otime.append((Hi * 60 + Mi))
        if len(self.otime) > 0:
            return True
        else:
            print("没有闹钟符合规定时间。")
            return False

    def outputtime(self):
        if self.checktime():
            otime = sorted(self.otime)
            output = otime[-1]
            outputh = int(output / 60)
            outputm = output % 60
            print(outputh, outputm)


if __name__ == "__main__":
    c = clock()
    c.inputdata()