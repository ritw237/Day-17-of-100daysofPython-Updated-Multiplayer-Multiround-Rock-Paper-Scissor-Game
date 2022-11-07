print("Epic Rock Paper Scissors game for 2 Players")
print()
print("Enter your response as R,P or S for Rock, Paper and Scissor")

from getpass import getpass as input

p1_score = 0
p2_score = 0


p1 = input("Player 1 > ")
p2 = input("Player 2 > ")

if p1=="R" and p2=="S":
  print("p1's Rock beats p2's Scissor ")
  or if p2 =="P":
      print("p2's Paper beats p1's Rock")
  elif p2 =="R":
    print("Draw! Both players have Rock")
  else:
      print("Please select only from R,P or S")

else:
  print("Done")