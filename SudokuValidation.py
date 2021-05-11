def valid_solution(board):
    return checkRows(board) and checkColumns(board) and not containsZero(board) and allNumeric(board) and gridsValid(board);
    

def gridsValid(board):
    blocks = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            blocks.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
            for k in range(len(blocks[0])):
                if blocks[0].count(blocks[0][k]) > 1:
                    return False;
    return True;


def allNumeric(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not str(board[i][j]).isdigit():
                return False;
    return True;


def containsZero(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return True;
    return False;
    

def checkRows(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i].count(board[i][j]) > 1:
                return False;
    return True;
    

def checkColumns(board):
    j = 0;
    tmp = [];
    while j < len(board[0]):
        for i in range(len(board)):
            tmp.append(board[i][j]);
            for k in range(len(tmp)):
                if tmp.count(tmp[k]) > 1:
                    return False;
        j += 1;
        tmp = []
    return True;
        
