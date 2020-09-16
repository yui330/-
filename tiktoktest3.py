import re

class money():
    def inputdata(self):
        N = input()
        N = int(N)
        if N < 1 or N > 1000:
            print("N is error")
            return
        line = input()
        line = re.split(r'\s', line)
        line = [int(e) for e in line]
        if len(line) != N:
            print("error")
            return
        c = self.cost(N, line)
        print(c)

    def cost(self, N, line):
        self.c = 100
        cost = [self.c]
        for i in range(N-1):
            cost.append(self.c)
            if line[i] > line[i+1]:
                if cost[i] < cost[i+1]:
                    cost[i] = cost[i] + self.c
                    self.costleft(line, cost, i)
            else:
                cost[i+1] = cost[i] + self.c
        print(cost)
        return self.costcount(cost)

    def costleft(self, line, cost, n):
        if line[n-1] > line[n]:
            cost[n-1] = cost[n-1] + self.c
            self.costleft(line, cost, n-1)

    def costcount(self, cost):
        c = sum(cost)
        return c

if __name__ == '__main__':
    m = money()
    m.inputdata()




