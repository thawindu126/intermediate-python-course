import random

DICE_ROLLS = 2


def main():
	"""
	Game's main function
	"""
	
	dice_sum = 0
	
	for _ in range(0, DICE_ROLLS):
		roll = random.randint(1, 6)
		dice_sum += roll
		print(f'You rolled a {roll}')

	print(f'You have rolled a total of {dice_sum}')


if __name__ == "__main__":
	main()
