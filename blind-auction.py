from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.

print(art.logo)
print('Welcome to the secret auction program.')

continuation = True
bid_dictionary = {}

while continuation:
  bidder_name = input('What is your name?: ')
  bid_amount = int(input('What is your bid?: $'))
  
  bid_dictionary.update({bidder_name : bid_amount})
  
  print(bid_dictionary)

  add_bidder = input('Are there any other bidders? Type "yes" or "no".\n').lower()

  if add_bidder == 'no':
    continuation = False
  elif add_bidder == 'yes':
    clear()

highest_bid = 0
max_bidder = ''

for bidder in bid_dictionary:
  bid_amount = bid_dictionary[bidder]

  if bid_amount > highest_bid:
    highest_bid = bid_amount
    max_bidder = bidder


print(f'The winner is {max_bidder} with a bid of ${highest_bid}')
