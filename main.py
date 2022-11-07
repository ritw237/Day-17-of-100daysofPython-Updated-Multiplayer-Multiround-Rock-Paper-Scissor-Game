print("Epic Rock Paper Scissors game for 2 Players")
print()
print("Enter your response as R,P or S for Rock, Paper and Scissor")

from getpass import getpass as input

p1_score = 0
p2_score = 0

round= 1
while True:
  print("Round ",round, "begins!!!")
  p1 = input("Player 1 > ")
  p2 = input("Player 2 > ")
  
  if p1== "R" and p2 =="S":
    print("p1 has Rock which beats Scissors of p2")
    p1_score+=1
  elif p1 =="P" and p2 =="R":
    print("p1 beats p2 because p1 has: Paper and p2 has: Rock")
    p1_score+=1
  elif p1 =="S" and p2=="P":
    print("p1 beats p2 because p1 has: Scissors and p2 has: Paper")
    p1_score+=1
  
  elif p2== "R" and p1 =="S":
    print("p2 has Rock which Scissors of p1")
    p2_score+=1
  elif p2 =="P" and p1 =="R":
    print("p2 beats p1 because p2 has: Paper and p1 has: Rock")
    p2_score+=1
  elif p2 =="S" and p1=="P":
    print("p2 beats p1 because p2 has: Scissors and p1 has: Paper")
    p2_score+=1
  
  elif p1 =="P" and p2 =="P":
      print("p1 and p2 both have Paper, it's a draw")
  elif p1 =="R" and p2 =="R":
      print("p1 and p2 both have Rock, it's a draw")
  elif p1 =="S" and p2 =="S":
      print("p1 and p2 both have Scissors, it's a draw")
  
  else:
    print("Please type valid responses as inputs")
  round = round+1
  print("Player 1 score:",p1_score)
  print("Player 2 score:",p2_score)
  
  if p1_score==3 or p2_score==3:
    break

if p1_score>p2_score:
  print("Player 1 wins!")
else:
  print("Player 2 wins!")