from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the blind aution")

blind_auction = {}
new_bidder = False

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid} ")
      
while not new_bidder:
  #Asking information of auction player
  name = input("What is your name?\n")
  bid = int(input("What is your bid? \n$"))
  blind_auction[name] = bid
  user_response = input("Is there another individual particapting in the auction? Type 'yes' or 'no' \n").lower()
  if user_response == "no":
    new_bidder = True
    highest_bidder(blind_auction)
    break
  else:
    clear()
          

