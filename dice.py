# dice.py
from random import randint
import re
from functions import solve

class Dice:
	def __init__(self, dice_formula):	# something like 1d6+2 (should support all algebra)
		self.formula = dice_formula
		rx = re.compile('([0-9\.\,]+)(?:d)([0-9\.\,]+)')
		self.number = 0
		self.size = []
		for m in rx.finditer(dice_formula):
			self.number += int(m.group(1))
			self.size.append(m.group(2))
		self.size = list(set(self.size)).sort(reverse=True)

	def roll(self):
		roll(self.formula)


# this function takes a string describing a dice roll (e.g. 2d10+d6+2) and replaces the
# random elements by a random number in the range e.g. 2d10+2 becomes [1;5]+2
def roll(dice_string):
	# replace [] with () since we need [] for a special syntax later
	dice_string = dice_string.replace('[', '(').replace(']', ')')
	added_rolls = dice_string		#one string to add the dice in one throw together
	# find dice occurences and replace them by random numbers in rage of the dice
	re_dc = re.compile('([0-9]*)(?:[dDwW]{1}(?!0))([0-9]+)')
	d = re_dc.search(added_rolls)
	while d:
		d_amt = int(d.group(1))
		d_sze = int(d.group(2))
		summed_dice = 0
		accum = '['
		for i in range(0, d_amt):
			if i > 0:
				accum += ';'
			roll = randint(1, d_sze)
			summed_dice += roll
			accum += str(roll)
		accum += ']'
		dice_string = re_dc.sub(str(accum), dice_string, count =1)
		added_rolls = re_dc.sub(str(summed_dice), added_rolls, count =1) 
		d = re_dc.search(added_rolls)
	return({'result': solve(added_rolls),
			'added rolls': added_rolls,
			'rolls': dice_string})

