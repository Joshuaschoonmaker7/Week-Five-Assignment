# Joshua Schoonmaker
# Intro Computer Sciences
# GameOfWar.1.py
# This program plays version 1 of the card game WAR


import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter = gameCounter + 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
		if gameCounter == 1000:
			break
	
	# End of game
	
	print("There were ", gameCounter, " rounds played:")
	print()
	print("Player A had ",len(PlayerAHand), "cards, and player B had ",len(PlayerBHand), "cards")
	
def playRound(PlayerAHand, PlayerBHand):
	
	PlayerACard = PlayerAHand.pop()
	PlayerBCard = PlayerBHand.pop()
	
	if getRank(PlayerACard) == getRank(PlayerBCard):
	
		PlayerAHand.append(PlayerACard)
		PlayerBHand.append(PlayerBCard)
		WAR(PlayerAHand, PlayerBHand)
	
	else:
		
		if getRank(PlayerACard) > getRank(PlayerBCard):
			PlayerAHand.insert(0,PlayerACard)

		else:
			PlayerBHand.insert(0,PlayerBCard)
	
	return PlayerAHand, PlayerBHand


def WAR(PlayerAHand, PlayerBHand):
	
	if len(PlayerAHand) and len(PlayerBHand) > 10:
		
		ExtraCardA = []
		ExtraCardB = []
		
		for x in range(5):
			
			ExtraCardA.append(PlayerAHand.pop())
			ExtraCardB.append(PlayerBHand.pop())
		
		if getRank(ExtraCardA[4]) == getRank(ExtraCardB[4]):
			
			return 
			
		else:
			
			if getRank(ExtraCardA[4]) > getRank(ExtraCardB[4]):
				
				PlayerAHand = ExtraCardA + ExtraCardB + PlayerAHand
				
			else:
				
				PlayerBHand = ExtraCardA + ExtraCardB +  PlayerBHand
	
		return PlayerAHand, PlayerBHand
		
	else:
		
		return

	# getRank Function
	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()