#gameResultFunction

def result(li, plr):
    # li = [[" "," "," "],[" "," "," "],[" "," "," "]]
    for i in range(0, 3, 1):
        rf = 1
        for j in range(0, 3, 1):
            if li[i][j] != plr.smb:
                rf = 0
                break
        if rf == 1:
            break
            
    for p in range(0, 3, 1):
        cf = 1
        for q in range(0, 3, 1):
            if li[q][p] != plr.smb:
                cf = 0
                break
        if cf == 1:
            break
    df = 0
    if (li[0][0] == li[1][1] == li[2][2] == plr.smb):
        df = 1
    elif (li[0][2] == li[1][1] == li[2][0] == plr.smb):
        df = 1
    if (rf == 1 or cf == 1 or df == 1):
        res = True
    else:
        res = False
    return res
#===================================================================
#playerClass

class player:
    def __init__(self, name, symbol):
        self.nm = name
        self.smb = symbol
#===================================================================
#ticTacToeClass

class ttt:
    def __init__(self, p1, p2):
        self.s1 = p1.smb
        self.s2 = p2.smb
        self.li = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.di = {"A":(0, 0),"B":(0, 1),"C":(0, 2),
                   "D":(1, 0),"E":(1, 1),"F":(1, 2),
                   "G":(2, 0),"H":(2, 1),"I":(2, 2)}
        self.t_count = 0
        print(f"{p1.nm}'s turn -->", end = " ")
        loc = input()
        self.p1(loc)

    def p1(self, loc):
        row = self.di[loc][0]
        col = self.di[loc][1]
        
        self.li[row][col] = self.s1
        for i in range(0, 3, 1):
            print(self.li[i])
        print("===============")
        self.t_count += 1
        
        if result(self.li, p1) == True:
            print(f"{p1.nm} has won the game.")
        elif result(self.li, p2) == True:
            print(f"{p2.nm} has won the game.")
        elif self.t_count == 9:
            print("This is a draw.")
        else:
            print(f"{p2.nm}'s turn -->", end = " ")
            loc = input()
            self.p2(loc)
    def p2(self, loc):
        row = self.di[loc][0]
        col = self.di[loc][1]
        
        self.li[row][col] = self.s2
        for i in range(0, 3, 1):
            print(self.li[i])
        print("===============")
        self.t_count += 1
        
        if result(self.li, p1) == True:
            print(f"{p1.nm} has won the game.")
        elif result(self.li, p2) == True:
            print(f"{p2.nm} has won the game.")
        elif self.t_count == 9:
            print("This is a draw.")
        else:
            print(f"{p1.nm}'s turn -->", end = " ")
            loc = input()
            self.p1(loc)
#===============================================================
# [ A , B , C ]
# [ D , E , F ]
# [ G , H , I]
p1 = player("Jetu", "O")
p2 = player("Turja", "X")
g1 = ttt(p1, p2)