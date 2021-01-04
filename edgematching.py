unicorn_cardset = [[["P","T"], ["G","T"], ["R","H"],["Y","H"]],
[["P","H"], ["G","H"], ["R","T"],["Y","T"]],
[["R","T"], ["Y","H"], ["G","H"],["P","T"]],
[["R","H"], ["Y","H"], ["P","T"],["Y","T"]],
[["R","T"], ["G","T"], ["P","H"],["Y","H"]],
[["R","T"], ["P","T"], ["R","H"],["G","H"]],
[["P","H"], ["G","H"], ["R","T"],["G","T"]],
[["Y","T"], ["P","T"], ["Y","H"],["G","H"]],
[["P","T"], ["G","H"], ["Y","H"],["Y","T"]]]

ultimate_cardset  = [[["C","O"], ["C","O"], ["A","I"],["C","I"]],	
	[["C","O"], ["A","O"], ["P","I"],["C","I"]],
	[["C","O"], ["A","O"], ["A","I"],["C","I"]],
	[["A","O"], ["B","O"], ["C","I"],["A","I"]],
	[["A","O"], ["P","O"], ["C","I"],["A","I"]],
	[["A","O"], ["A","O"], ["B","I"],["C","I"]],
	[["A","O"], ["P","O"], ["B","I"],["P","I"]],
	[["B","O"], ["C","O"], ["P","I"],["C","I"]],
	[["B","O"], ["C","O"], ["A","I"],["B","I"]],
	[["B","O"], ["C","O"], ["B","I"],["P","I"]],
	[["B","O"], ["B","O"], ["P","I"],["C","I"]],
	[["B","O"], ["B","O"], ["P","I"],["A","I"]],
	[["P","O"], ["C","O"], ["C","I"],["B","I"]],
	[["P","O"], ["C","O"], ["C","I"],["P","I"]],
	[["P","O"], ["C","O"], ["A","I"],["A","I"]],
	[["P","O"], ["B","O"], ["B","I"],["A","I"]]]
	

def return_card(a_cardset, a_card):
	"""send a cardset and a card ID, get return top, right, bottom, left"""
	num_cards = len(a_cardset)
	if a_card < num_cards:
		return a_cardset[a_card]
	else:
		return [[" "," "],[" "," "],[" "," "],[" "," "]]


def return_printable_side(side):
	return side[0] + side[1]
	
def print_card(a_card):
	print("----------")
	print("|   " + return_printable_side(a_card[0]) + "   |")
	print("| " + return_printable_side(a_card[3]) + "  " + return_printable_side(a_card[1]) + " |")
	print("|   " + return_printable_side(a_card[2]) + "   |")
	print("----------")

def print_header(a_puzzle_width):
	for c in range(1,a_puzzle_width):
		print("-------------",end='')
	print('')
	
def print_placement(a_placement, a_puzzle_width):
	"""print a placement nicely"""
	#print("width " +str(a_puzzle_width))
	for row in range(0,a_puzzle_width):
		print_header(a_puzzle_width)
		print("|",end='')
		for column in range(0,a_puzzle_width):
			card=return_card(a_placement,row*a_puzzle_width+column)
			print("   " + return_printable_side(card[0])+ "   |",end='')
		print()
		print("|",end='')
		for column in range(0,a_puzzle_width):
			card=return_card(a_placement,row*a_puzzle_width+column)
			print(" " + return_printable_side(card[3]) + "  " + return_printable_side(card[1]) + " |",end='')
		print()
		print("|",end='')
		for column in range(0,a_puzzle_width):
			card=return_card(a_placement,row*a_puzzle_width+column)
			print("   " + return_printable_side(card[2])+ "   |",end='')
		print()
	print_header(a_puzzle_width)
	
def rotate_card(a_card):
	top = a_card[3]
	right = a_card[0]
	bottom = a_card[1]
	left = a_card[2]
	return [top,right,bottom,left]

def flip_card(a_card):
	top = a_card[0]
	right = a_card[3]
	bottom = a_card[2]
	left = a_card[1]
	return [top,right,bottom,left]	
	
def check_left(a_placement, a_card, a_num_cards_placed):
	reference_card = a_placement[a_num_cards_placed-1]
	if reference_card[1][0] == a_card[3][0] and reference_card[1][1] != a_card[3][1]:
		return True
	else:
		return False
		
def check_up(a_placement, a_card, a_num_cards_placed, a_puzzle_width):
	reference_card = a_placement[a_num_cards_placed-a_puzzle_width]
	
	if reference_card[2][0] == a_card[0][0] and reference_card[2][1] != a_card[0][1]:
		return True
	else:
		return False

def check_left_up(a_placement, a_card, a_num_cards_placed, a_puzzle_width):
	return check_left(a_placement, a_card, a_num_cards_placed) and check_up(a_placement, a_card, a_num_cards_placed, a_puzzle_width)


def matches (a_placement, a_card, a_puzzle_width):
	### define specific checks for each possible length of a valid placement
	num_cards_placed = len(a_placement)
	#print(num_cards_placed, a_puzzle_width)
	if num_cards_placed == 0: #placing top left always true
		return True
	elif num_cards_placed < a_puzzle_width : #placing top middle or top right, check the left of this card to the right of the previous
		return check_left(a_placement, a_card, num_cards_placed)
	
	elif num_cards_placed % a_puzzle_width == 0: #middle left or bottom left, check the top of this card to the bottom of the one above
		return check_up(a_placement, a_card, num_cards_placed, a_puzzle_width)
		
	else: #middle middle, check the top of this card to the bottom of tm and left of this card = right of ML (etc)
		return check_left_up(a_placement, a_card, num_cards_placed, a_puzzle_width)
		
def try_card(a_placement, a_card, an_untried_cards, a_puzzle_width, a_flippable):		
	### if the card can be placed, return the new valid placement and a boolean True.  If the card cannot be placed, return the old placement and a boolean False.
	if matches(a_placement, a_card, a_puzzle_width): #default orientation
		a_placement.append(a_card)
		solve1(a_placement[:], an_untried_cards[:], a_puzzle_width,a_flippable)
		
def solve1(a_placement, an_untried_cards, a_puzzle_width, a_flippable):
	#print("Placement Length: " +str(len(a_placement)))
	#print_placement(a_placement,a_puzzle_width)
	if len(a_placement) == a_puzzle_width**2: #if we have a completed placement, we're done

		print_placement(a_placement, a_puzzle_width)
	else:
		
		#print("Untried cards:"+ str(len(an_untried_cards)))
		
		for card in an_untried_cards:
		
			remaining_cards = an_untried_cards.copy()
			remaining_cards.remove(card)  #requires unique cards
			
			#print("Trying card:" + str(card) + " with " + str(len(remaining_cards)) + " cards passed along")
			#print_card(card)
			#print_placement(a_placement, a_puzzle_width)
			
			try_card(a_placement[:], card, remaining_cards, a_puzzle_width,a_flippable)
			try_card(a_placement[:], rotate_card(card), remaining_cards, a_puzzle_width,a_flippable)
			try_card(a_placement[:], rotate_card(rotate_card(card)), remaining_cards, a_puzzle_width,a_flippable)
			try_card(a_placement[:], rotate_card(rotate_card(rotate_card(card))), remaining_cards, a_puzzle_width,a_flippable)
			
			if a_flippable:
				try_card(a_placement[:], flip_card(card), remaining_cards, a_puzzle_width, a_flippable)
				try_card(a_placement[:], rotate_card(flip_card(card)), remaining_cards, a_puzzle_width, a_flippable)
				try_card(a_placement[:], rotate_card(rotate_card(flip_card(card))), remaining_cards, a_puzzle_width, a_flippable)
				try_card(a_placement[:], rotate_card(rotate_card(rotate_card(flip_card(card)))), remaining_cards, a_puzzle_width, a_flippable)

def solve(a_cardset, a_flippable):
	placement = []
	puzzle_width = int(len(a_cardset)**0.5)

	solve1(placement, a_cardset, puzzle_width, a_flippable)


solve(ultimate_cardset, False)
