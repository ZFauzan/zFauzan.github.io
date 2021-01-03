#Zunaira Fauzan

def crossword(L):
  # make a 20x20 matrix
  blank = ' '
  board = [[blank]*20 for i in range(20)] 


  # 1. place first word horizontally in the center 
  if not firstword(board, L[0]):
      print(L[0],"reaches outside grid")

  # 2. placing second word vertically 
  for k in range(1,len(L)):
      # if odd, add vertical
      if k % 2 == 1:
          addvertical(board,L[k])
          
      # if even, add horizontal
      else:
          addhorizontal(board,L[k])

  printmatrix(board)

def firstword(board, word) :
    D = len(board)
    n = len(word)
    # check first if the word is too long
    if n > D :
      return False
    # Put the word onto the board in the centre
    for k in range(n) :
      column = D // 2 - n // 2 + k
      board[D // 2] [column] = word[k]
    return True
  
# if you can add a word vertically at a particular spot board[row][col]
# (a) the word is not too long for the board at that spot
# (b) at least one letter of word must match, and
# (c) other letters of word must land on blanks
# The word must start at row, col and go downwards

def checkvertical(board, word, row, col) :
  D = len(board)
  n = len(word)
  blank = ' '
  # (a) the word is not too long for the board at that spot
  if n > 20 - row :
    return False

  matchesoneletter = False
  # go through the letters of the word
  for k in range(n) :
    wordletter = word[k]
    boardletter = board[row + k] [col ]
    # are these two letters the same?
    # check for validity
    if wordletter == boardletter and not vertical_touching(board,word,row,col,k):
      matchesoneletter = True
  return matchesoneletter

# add a word vertically using checkvertical() to verify landing sites


def addvertical(board, word) :
  # go across and down the whole board looking for a spot to add word
  for i in range(len(board)) :
    for j in range(len(board)) :
      # check if word can go at (i,j), then place it there
      if checkvertical(board, word, j, i):
        for k in range(len(word)):
          row = j
          board[j + k][i] = word[k]
        return True
  print(word,'does not have a matching letter or it reaches outside grid') 
  return False

def vertical_touching(board, word, row, col, index):
    blank = ' '
    for k in range(len(word)):
    # for the word,
    # a) for every char, horizontally left and right must be blank
    #    except for word[k]
        if k != index:
            #print(row, col, word, index)
            if board[row+k][col] != blank: 
                return True
            if board[row+k][col+1]!= blank:
                return True
            elif board[row+k][col-1] != blank:
                return True
    
    # b) for the first letter, vertically up must be blank
    if board[row-1][col] != blank:
        return True 
    # c) for the last letter, vertically down must be blank
    if board[row+len(word)][col] != blank:
        return True
    return False

def checkhorizontal(board, word, row, col) :
  D = len(board)
  n = len(word)
  blank = ' '
  # (a) the word is not too long for the board at that spot
  if n > 20 - col :
    print(word, 'reaches outside grid') 
    return False
  # Check now if it matches a letter on the board
  matchesoneletter = False
  # go through the letters of the word
  for k in range(n) :
    wordletter = word[k]
    boardletter = board[row] [col + k]
    if wordletter == boardletter and not horizontal_touching(board, word, row, col, k):
      matchesoneletter = True
  return matchesoneletter

def addhorizontal(board, word) :
  # go across and down the whole board looking for a spot to add word
  for i in range(len(board)) :
    for j in range(len(board)) :
      # check if word can go at (i,j)  and if it can, then place it there
      if checkhorizontal(board, word, j, i):
        for k in range(len(word)):
          row = j
          board[j][i + k] = word[k]
        return True
  print(word, 'does not have a matching letter') 
  return False

def horizontal_touching(board, word, row, col, index):
    blank = ' '
    for k in range(len(word)):
    # for the word,
    # a) for every char, vertically up and down must be blank except word[k]
        if k != index:
            #print(row, col, word, index)
            if board[row][col + k] != blank: 
                return True
            if board[row+1][col+k]!= blank: 
                return True
            elif board[row-1][col+k] != blank:
                return True
    
    # b) for the first letter, horizontally left must be blank
    if board[row][col-1] != blank:
        return True 
    # c) for the last letter, horizontally right must be blank
    if board[row][col+len(word)] != blank:
        return True
    return False

def printmatrix(matrix):
  for y in matrix:
    print(y)

def main():
  words = ["addle", "apple", "clowning", "incline", "plan","gift"] 
  #words = ["ryerson","computer", "science", "nice", "code", "algorithm", "motivation", "macroeconomics"]
  #words = ["averyveryverywaytoolongword"]
  crossword(words) 

main()
