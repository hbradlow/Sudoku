import random

class SudokuBoard:
    def __init__(self):
        self.reset()
    def reset(self):
        self.board = [[0 for i in range(9)] for j in range(10)]
    def check_unique_set(self,s):
        l = []
        for i in s:
            if i in l and i != 0:
                return False
            l.append(i)
        return True
    def check_valid(self):
        for i in range(9):
            if not self.check_unique_set(self.board[i]):
                return False
        for j in range(9):
            if not self.check_unique_set([self.board[i][j] for i in range(9)]):
                return False
        for i in range(3):
            for j in range(3):
                s = []
                for k in range(3):
                    for l in range(3):
                        s.append(self.board[i*3+k][j*3+l])
                if not self.check_unique_set(s):
                    return False
        return True
    def place_cell(self,i,j):
        l = range(1,10)
        for val in range(9):
            self.board[i][j] = l.pop(random.choice(range(len(l))))
            if self.check_valid():
                return True
        return False
    def generate_board(self,num_attempts=1000):
        def create_board():
            for i in range(9):
                for j in range(9):
                    if not self.place_cell(i,j):
                        return False
            return True
        for i in range(num_attempts):
            if create_board():
                self.num_attempts_used = i
                return True
            self.reset()
        return False
    def __repr__(self):
        s = ""
        for i in range(9):
            if i%3==0 and i!=0:
                s += "---------" + "-------" + "-----\n"
            s += " ".join(str(j) for j in self.board[i][0:3]) + " | "
            s += " ".join(str(j) for j in self.board[i][3:6]) + " | "
            s += " ".join(str(j) for j in self.board[i][6:9]) + "\n"
        return s

if __name__=="__main__":
    sb = SudokuBoard()
    if sb.generate_board():
        print "Solution found in",sb.num_attempts_used,"tries"
        print sb
    else:
        print "No solution found"
