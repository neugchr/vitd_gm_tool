import monster
import item
from random import choices
from random import randint

class Cyclops(monster.Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'cyclops (crawl)',
					   'description': ('Bodies twisted as if grappling, '
									   +'a single caved headthat thrums with hollow notes. '
									   +'They are never alone ...'),
					   'hit_dice': '1d8',
					   'strength': '1d3-1',
					   'dexterity': '1d2',
					   'constitution': '1d3-1',
					   'intelligence': '1d6-5',
					   'wisdom': '2d2-2',
					   'charisma': '1d4-5',
					   'damage': '1d4-1; 1d4-1 (-2 on attack)',
					   'natural_armour': '1d6|6+',
					   'ability': ('Call in the Dark: They cry for each '
								   +'other in the dark. Every round they are '
								   +'aware of the Travelers, there is a 1-in-6 '
								   +'chance another Cyclops will appear.'
								   +'(Or other Monsters from the floor are '
								   +'attracted at the GMs discretion)')
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 1 in 8 chance to have a random piece of equipment
		if randint(1,8) == 1:
			tmp = [item.Scrap(), item.choose_random_miscellania(), item.choose_random_light(),
				   item.choose_random_weapon(), item.choose_random_armour]
			self._attr['loot'] = choices(tmp, weights = [20,20,20,5,1])[0]


class Medusa(monster.Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'cyclops (crawl)',
					   'description': ('Appears as a trio of screaming '
									   +'lovers, its head both terrible to '
									   +'behold and pulsing with frightening '
									   +'harmonic power...'),
					   'hit_dice': '2d8',
					   'strength': '1d3-1',
					   'dexterity': '1d2',
					   'constitution': '1d3-1',
					   'intelligence': '1d6-5',
					   'wisdom': '2d2-2',
					   'charisma': '1d4-5',
					   'damage': '1d8',
					   'natural_armour': '1d6|6+',
					   'ability': ('Petrifying Scream: Their shrieks '
								   +'tense muscle and freeze the mind. '
								   +'As Attack, all within sight must '
								   +'save with wisdom.\n'
								   +'Success: No '
								   +'effect, advantage on subsequent '
								   +'saves.\n'
								   +'Fail: stunned for 1d6-Constitution rounds.')
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 1 in 8 chance to have a random piece of equipment
		if randint(1,8) == 1:
			tmp = [item.Scrap(), item.choose_random_miscellania(), item.choose_random_light(),
				   item.choose_random_weapon(), item.choose_random_armour]
			self._attr['loot'] = choices(tmp, weights = [20,20,20,5,1])[0]


class Griffon(monster.Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'cyclops (crawl)',
					   'description': ('Dozens of hands writhe in the '
									   +'guise of wings and a face. Fingers'
									   +'twitch hungrily around drooling'
									   +'jaws...'),
					   'hit_dice': '3d8*2',
					   'strength': '2d2',
					   'dexterity': '1d2+1',
					   'constitution': '1d3',
					   'intelligence': '1d6-5',
					   'wisdom': '2d2-2',
					   'charisma': '1d4-5',
					   'damage': '1d8; Devour',
					   'natural_armour': '2d6|6+',
					   'ability': ('Fly: can fly\n'
								   +'Devour: The fingers snare and '
								   +'drag victims to its maw. Save '
								   +'with Dexterity or become trapped in '
								   +'its mouth and suffer 1d4 damage '
								   +'every turn (armour protects normally).\n'
								   +'Save with Strength every round '
								   +'to break free.\n'
								   +'When a player suffers '
								   +'8 damage in this fashion, Save '
								   +'versus Hold again or be swallowed '
								   +'whole (treat same as bleading out).')
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 1 in 8 chance to have a random piece of equipment
		if randint(1,8) == 1:
			tmp = [item.Scrap(), item.choose_random_miscellania(), item.choose_random_light(),
				   item.choose_random_weapon(), item.choose_random_armour]
			self._attr['loot'] = choices(tmp, weights = [20,20,20,5,1])[0]


	
class Wyrm(monster.Character):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'cyclops (crawl)',
					   'description': ('Bodies twisted as if grappling, '
									   +'a single caved headthat thrums with hollow notes. '
									   +'They are never alone ...'),
					   'hit_dice': '(5d8)*3',
					   'strength': '1d2+4',
					   'dexterity': '1d3+2',
					   'constitution': '1d2+3',
					   'intelligence': '4d3-8',
					   'wisdom': '4d3-8',
					   'charisma': '2d4-6',
					   'damage': '1d6+1; 1d6+1',
					   'natural_armour': '2d6|5+',
					   'ability': ('Mimicry: It prefers to ambush, '
								   +'luring with its many tongues. The '
								   +'Wyrm can perfectly imitate the '
								   +'voice of any mortal it has heard.\n'
								   +'Breath of decay: Every one of its mouth '
								   +'bellows in a scream.'
								   +'\nAs Attack, all within sight must '
								   +'Save versus Breath.\n'
								   +'Success: Half damage\n'
								   +'Fail: 1d6 decaying damage ignores armour. '
								   +'Every carried item has a 1/20 chance '
								   +'to become scrap.')
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)
		# give it a 1 in 8 chance to have a random piece of equipment
		if randint(1,8) == 1:
			tmp = [item.Scrap(), item.choose_random_miscellania(), item.choose_random_light(),
				   item.choose_random_weapon(), item.choose_random_armour]
			self._attr['loot'] = choices(tmp, weights = [20,20,20,5,1])[0]
	
