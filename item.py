#item.py
from random import randint
from random import choices

class Item:
	# those are the default keys, those items will appear in this order by printing
	keys = ['name', 'description', 'equipment_slots',
			'attack_bonus', 'damage', 'range',
			'defense_bonus', 'armour']
	
	def __init__(self, **kwargs):
		self._attr = {}
		for k, v in kwargs.items():
			self._attr[k] = v
	
# the properties are not necessary i'll leve them here for my own reference
#	@property
#	def attr(self):
#		return(self._attr)
#	
#	@attr.setter
#	def attr(self, value):
#		self._attr = value
#	
#	@attr.deleter
#	def attr(self):
#		del self._attr
#
# here's the magic happening this means i can just use instance['name'] to directly acces
# elements of the _attr dictionary without having to write instance.attr['name']
	def __getitem__(self, key):
		return(self._attr[str(key)])
	
	def __setitem__(self, key, value):
		self._attr[str(key)] = value
	
	def __iter__(self):
		return(ItemIterator(self))
	
	def __contains__(self, key):
		if key in self._attr:
			return(True)
		else:
			return(False)
	
	def __len__(self):
		return(len(self._attr))
	
	def __repr__(self):
		return(self.__str__())
	
	def __str__(self):
		ostr = ''
		# at first we add all the items in the default list
		for k in Item.keys:
			try:
				if k == 'name' or k == 'description':
					ostr += str(self._attr[k]+'\n')
				else:
					ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
			except:
				pass
		# then we again iterate over the content but omit everything we already have
		for k,v in self._attr.items():
			if k not in Item.keys:
				ostr += str(k).replace('_',' ')+': '+str(self._attr[k])+'\n'
		return(ostr)


class ItemIterator():
	def __init__(self, item):
		self._item = item
		self._index = 0
	
	def __next__(self):
		if self._index < len(self._item._attr):
			k = list(self._item._attr.keys())[self._index]
			result=(k,self._item._attr[k])
		else:
			raise StopIteration
		self._index += 1
		return(result)

########################################
# WEAPONS AND ARMOURS (implementes as classes)
########################################

# WEAPONS
class Sword(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'sword',
					   'description': 'An elegant bladed weapon',
					   'equipment_slots': 2,
					   'damage': '1d6'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Dagger(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'dagger',
					   'description': 'a small blade usually carried as a sidearm',
					   'equipment_slots': 1,
					   'damage': '1d6-1'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Greatsword(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'greatsword',
					   'description': 'An elegant bladed weapon',
					   'equipment_slots': 3,
					   'damage': '1d6+1'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


# RANGED WEAPONS
class Bow(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bow',
					   'description': 'A ranged weapon usually crafted from wood',
					   'equipment_slots': 2,
					   'damage': '1d6',
					   'range': 20
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Arrow(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'arrows',
					   'description': 'Ammunition for bows. Weight per 10.',
					   'equipment_slots': 1,
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class CrossBow(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'crossbow',
					   'description': 'An advanced ranged weapon.\n'
					   				  +'Requires an extra action to reload.',
					   'equipment_slots': 2,
					   'damage': '1d6+1',
					   'range': 20
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Bolts(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bolts',
					   'description': 'Ammunition for crossbbows. Weight per 10.',
					   'equipment_slots': 1,
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Sling(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'sling',
					   'description': 'A ranged weapon made from leather or fiber that is used to '
					   					+'hurl stones or lead ammunition at your enemies.\n'
					   					+'Can use gathered stones as ammunition at -2 penalty.',
					   'equipment_slots': 1,
					   'damage': '1d6-1',
					   'range': 10
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class SlingBullet(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'sling bullet',
					   'description': 'Ammunition for slings. Weight per 20.',
					   'equipment_slots': 1,
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class ThrowingKnife(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'throwing knife',
					   'description': 'A small ranged weapon. Size per 3',
					   'equipment_slots': 1,
					   'damage': '1d6-1',
					   'range': 10
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class ThrowingAxe(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'throwing axe',
					   'description': 'A massive throwing weapon. Usually thrown before engaging in melee.',
					   'equipment_slots': 1,
					   'damage': '1d6+1',
					   'attack_bonus': '-1',
					   'range': 10
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


# SHIELDS
class Shield(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'shield',
					   'description': 'shields come in various forms and makes, they are worn on the arm and offer some protection against melee and ranged attacks',
					   'equipment_slots': 2,
					   'defense_bonus': 2
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Buckler(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'buckler',
					   'description': 'a buckler is a small defensive weapon, it offers no protection against ranged attacks',
					   'equipment_slots': 1,
					   'defense_bonus': 2
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


# ARMOURS
class Hides(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'hides',
					   'description': 'thick protective clothing offering some resistance to attack',
					   'equipment_slots': 1,
					   'armour': '1d6|6+'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Gambeson(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'gambeson',
					   'description': 'padded armour made of linen or leather',
					   'equipment_slots': 2,
					   'armour': '2d6|6+'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class MailArmour(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'chain mail',
					   'description': 'a shirt made from chain mail, worn over padded armour for increased protection',
					   'equipment_slots': 3,
					   'armour': '2d6|5+'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class PlateArmour(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'plate',
					   'description': 'adding a breastplate, greaves and arm guards offers increased protection',
					   'equipment_slots': 4,
					   'armour': '3d6|5+'
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

		
class Helmet(Item):
	def __init_(self, **kwartgs):
		for (k, v) in {'name': 'helmet',
					   'description': 'a helmet is usually one of the first pieces of armour any warrior will add to their kit'+
					   '\ncritical hits now do normal damage instead of 2x',
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


########################################
# TREASURES
########################################
class Treasure(Item):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self._attr['type']='artifact'


class SeerStone(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Seer Stone',
					   'description': ('A beautiful orb of cut glass. '
									   +'Reveals fissures of light on '
									   +'the ceiling if looked through. '
									   +'Allows for navigation even when '
									   +'landmarks are invisible'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class SpellEater (Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Spell Eater',
					   'description': ('An octagonal plate of hardened '
									   +'green metal. Once per day, the '
									   +'plate may absorb one spell that '
									   +'targets you, growing painfully '
									   +'hot when it does so'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class DowsingCharm(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Dowsing Charm',
					   'description': ('A small tripointed star made of '
									   +'pearl-stone. Pointsto the nearest '
									   +'source of water.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Bleeder(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Bleeder',
					   'description': ('Jagged sharpened stone the color of '
									   +'coal. Can be wielded as a blade, '
									   +'wounds made with it do not heal '
									   +'quickly and weep black ooze ichor '
									   +'for 1d6 damage every day.'),
					   'damage': '1d6-1',
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class TorchStone(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Torch Stone',
					   'description': ('A luminescent cylinder that is warm '
									   +'to the touch. Glows like a lantern '
									   +'when fed blood, 1 HP for 1 hour of '
									   +'light.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class AlarmBand(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Alarm Band',
					   'description': ('A circlet that seems made of woven '
									   +'bone. Vibrates intesnely when '
									   +'Crawl are near. Worn as a helmet.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Dreamless(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Dreamless',
					   'description': ('A bead that seems to swirl with '
									   +'colour. You nolonger need to '
									   +'sleep, your appearance grows '
									   +'haggard with time.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class StoneDance(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'StoneDance',
					   'description': ('A leather bag filled with a '
									   +'grey powder that feels like needles '
									   +'to the touch. Anything coated in '
									   +'this powder passes throughstone '
									   +'like water. Enough powder to '
									   +'cover one person.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class WeighNoMore(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Weigh No More',
					   'description': ('A stone crescent, weightless and '
									   +'azure. As long as it is held in '
									   +'hand, the wielder is weightless.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Unmoved(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Unmoved',
					   'description': ('A cube of iron with tarnished gold '
									   +'lines. When held in place and '
									   +'struck with force the cube will be '
									   +'immovable until verbally released '
									   +'by the wielder. '
									   +'Approx 1m³.'),
					   'equipment_slots': 4
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class LyingCoin(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Lying Coin',
					   'description': ('An octagonal lead disk, '
									   +'painfully cold to the touch. '
									   +'The coin hums when lies are told.'),
					   'equipment_slots': 0
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Melder(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Melder',
					   'description': ('Fused and broken jade, '
									   +'sticky like scabs. Touching the '
									   +'fresh dead heals you for 1d6 HP '
									   +'a minute as they are absorbed.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Transference(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Transference',
					   'description': ('Two plates of tarnished gold '
									   +'Can bring back the dead, but only '
									   +'if another life is given in '
									   +'exchange and placed on the '
									   +'other plate.'
									   +'Size is 2 plates à 2.'),
					   'equipment_slots': 4
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Forgotten(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Forgotten',
					   'description': ('A tablet of soapstone and a stylus '
									   +'of iron. Thoughts and ideas carved '
									   +'into this tablet are forgotten, '
									   +'the effect spreading from '
									   +'mortal to mortal like wildfire.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Annihilation(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Annihilation',
					   'description': ('A heavy staff of chipped and broken '
									   +'obsidian. When somethin is slain '
									   +'by this staff, it is utterly '
									   +'annihilated, stricken from the '
									   +'memory of the world and mortals. '
									   +'Has a 1 in 36 chance of breaking '
									   +'every strike.'
									   +'This is a two-handed weapon.'),
					   'equipment_slots': 2,
					   'damage': '1d6'
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Incineration(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Incineration',
					   'description': ('A single pale flame, utterly colourless'
									   +'roughly the size of an adults fist. '
									   +'It burns and spreads like any '
									   +'ordinary flame, but can never be '
									   +'extinguished. When all fuel is '
									   +'consumed a flame of the original '
									   +'size remains where the last '
									   +'fuel was consumed.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Transmutation(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Transmutation',
					   'description': ('A simple sphere of polished lead. '
									   +'Anythin this orb directly touches '
									   +'turns into lead. '
									   +'Living things take 1d6 damage '
									   +'a successful save halfs damage.'),
					   'equipment_slots': 2
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

class Command(Treasure):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Command',
					   'description': ('A tiara-sized ring of glittering '
									   +'bismuth. All who can hear and '
									   +'understand its wielder will '
									   +'follow their commands without '
									   +'question.'),
					   'equipment_slots': 1
				  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


########################################
# MISCELLANEOUS ITEMS
########################################
class Bearings(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bearings',
					   'description': ('Two cirles wit balls or zylinders '
									   +'in between to minimize friction.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class BearTrap(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bear trap',
					   'description': ('a massive pair of jaws used to catch animal '
									   +'- or human - prey. '
									   +'Immobilized until successful Str save. '
									   +'If concealed save against Int to reveal.'),
					   'damage': '2d6',
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Bottle(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'glass bottle',
					   'description': 'A bottle of glass. Typical volume of approx. 1 l.',
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class HobnailedBoots(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'hobnailed boots',
					   'description': ('high quality boots with added hobnails '
									   +'provides great traction on soft and rocky '
									   +'terrain also provides great slippage on '
									   +'hard polished ground.'
									   +'One slot when carried in inventory.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Bucket(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'bucket',
					   'description': ('A bucket made from wood, metal or leather. '
									   +'Typical volume of approx. 10 l.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Caltrops(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Caltrops',
					   'description': ('Tetragonal shaped pieces of metal designed '
									   +'to bury into the foot of persons stepping into '
									   +'them. Enough to cover 4 m². '
									   +'Quarter movement speed for 1d3 days. '
									   +'Con save for half penalty. '
									   +'Save dex to avoid when passing area.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Chain(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'chain',
					   'description': ('A sturdy chain of iron. 3 m long.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Chest(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Chest',
					   'description': ('A small chest. Usually made from wood. '
									   +'Sadly it has no legs and is not animated. '
									   +"So you'll have to carry it around."),
					   'equipment_slots': 2
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Chisel(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Chisel',
					   'description': ('A tool for carving stone. '
									   +'Can be abused as a somewhat less shitty '
									   +'improvised weapon.'),
					   'damage': '1d6-1',
					   'attack_bonus': -1,
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Crowbar(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'crowbar',
					   'description': ('A tool used for prying things open. '
									   +'It is also a passable improvised weapon.'),
					   'damage': '1d6-1',
					   'attack_bonus': -1,
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Drill(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'drill',
					   'description': ('A tool used to drill holes.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class GrapplingHook(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'grappling hook',
					   'description': ('A three or four pronged hook to which a '
									   +'rope can be affixed.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Hammer(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'hammer',
					   'description': ('a tool used for putting nails in things '
									   +'or smashing things, like for example thumbs.'),
					   'damage': '1d6-1',
					   'attack_bonus': -1,
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class IronTongs(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'iron tongs',
					   'description': ('A pair of long iron tongs, '
									   +'there are different makes for different '
									   +'specialised purposes.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Kettle(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'kettle',
					   'description': ('A small kettle used for boiling water. '
									   +'Typical volume of 1/2 to 2 litres'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Ladder(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'ladder',
					   'description': ('A tool for climbing up smooth surfaces. '
									   +'Typical length of 2-3 metres.'),
					   'equipment_slots': 2
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Lockpicks(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'lockpicks',
					   'description': ('Tools used to open up locks.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Magnet(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'magnet',
					   'description': ('A piece of magnetised matter.'
									   +'Usually either magnetised iron or '
									   +'in this place lodestone.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Manacles(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'manacles',
					   'description': ('bindings used to restrict the movement of '
									   +'a persons arms and or legs. '
									   +'Often combined with prisoners to impede escape.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class MetalFile(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'metal file',
					   'description': ('A piece of hardened roughed metal used to '
									   +'work away at other metals.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Mirror(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'mirror',
					   'description': ('A reflective surface, '
									   +'simple variants are made from polished copper '
									   +'sheets. More expensive ones are polished silver '
									   +'covered by glass.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Nails(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'nails',
					   'description': ('Nails are put into things to hold them together. '
									   +'There are various different makes for different '
									   +'purposes.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Net(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'net',
					   'description': ('Used to entangle animals or people. '
									   +'Save dex to avoid being immobilized. '
									   +'Can save dex every round to get free.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Pick(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Pick',
					   'description': ('A tool used for prospecting and mining.'
									  +' Enables to harvest Lodestone from Desposits.'),
					   'equipment_slots': 2,
					   'damage': '1d6',
					   'attack_bonus': -1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Pole(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'pole',
					   'description': ('Typically made from wood, sometimes from metal. '
									   +'Why are poles so expensive and ladders so cheap? '
									   +'Guild regulations baby!'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Rope(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'rope',
					   'description': ('Plant or animal fibers wrought into a rope. '
									   +'Typically up to 15 metres.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Sack(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'sack',
					   'description': ('A sack. Can be impregnated with oil or beeswax '
									   +'to provide (some) protection from water.'
									   +''
									   +''
									   +''
									   +''),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Scrap(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'scrap',
					   'description': ('An assortment of scrap and junk '
									   +'it could serve you well. '
									   +'As long as you are looking for '
									   +'a doorstopper or paperweight'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Shovel(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'shovel',
					   'description': ('An all time favourite of peasants, '
									   +'builders, gravediggers, graverobbers and knights. '
									   +'Used to dig trenches and storm them. '
									   +'Can be used as a decent improvised '
									   +'two handed weapon.'),
					   'damage': '1d6',
					   'attack_bonus': 0,
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Soapstone(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'soapstone',
					   'description': ('A lump of soapstone. '
									   +'It is popular amongst artists and craftsmen '
									   +'due to the ease with which it can be carved.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class SurgeonsTools(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'surgeons tools',
					   'description': ('Needles for sewing cuts and lacerations, braces '
									   +'for setting bones, spoons to extract projectiles '
									   +'scalpels, pincers and saws for operating and '
									   +'amputating.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Spyglass(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'Spyglass',
					   'description': ('A tool for magnifying and observing '
									   +'things far away. Consists of lenses '
									   +'housed within a cylinder usually made from metal.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Tent(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'tent',
					   'description': ('A small tent for one person.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Waterskin(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'waterskin',
					   'description': ('A bag made usually from animal hides and/or '
									   +'bladders. It is often waterproofed by using '
									   +'pitch or resins.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


########################################
# Lighting
########################################
class Candle(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'candle',
					   'description': ('Provides dim illumination in a '
									   +'radius of approx. 2 m. '
									   +'Burns for 4 hours.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class DirectionalLantern(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'directional lantern',
					   'description': ('This lantern is fitted with a reflector '
									   +'usually made from polished metal and a '
									   +'collector lens. Made somewhat less useful by '
									   +'the fact that the collector and lens require '
									   +'frequent cleaning from accumulated soot. '
									   +'Illuminates in a 45° angle. Casts bright light '
									   +'20 m and dim light 40 meters away.'
									   +'Burns for 6 hours on one flask of oil.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Lantern(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'lantern',
					   'description': ('Provides bright illumination in a 10 m '
									   +'radius and dim illumination in a 20 m '
									   +'radius. '
									   +'Burns for 6 hours on one flask of oil.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Oil(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'oil',
					   'description': ('A burnable liquid. Useful for fuelling lamps.'
									   +'Usually comes with a clay pot.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Torch(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'torch',
					   'description': ('Provides bright illumination in a 10 m radius '
									   +'and dim illumination in a 20 m radius. '
									   +'Burns for 1 hour.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


class Tinderbox(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'tinderbox',
					   'description': ('Contains flint and steel and tinder. '
									   +'Has a 1 in 6 chance per round to start a fire.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)

		
########################################
# Alchemicals
########################################
class FirePot(Item):
	def __init__(self, **kwargs):
		for (k, v) in {'name': 'firepot',
					   'description': ('A clay pot containing an alchemical mixture that ignites when coming in contact with air.\n'
									   +'Save Dexterity or suffer 1d6 damage.  When hit target suffers 1d3 and moves around randomly, '
									   +'panicking until it saves Wisdom.'),
					   'equipment_slots': 1
					  }.items():
			if k not in kwargs.keys():
				kwargs[k] = v
		super().__init__(**kwargs)


########################################
# Helper functions
########################################
def choose_random_miscellania():
	pool = [Bearings(), BearTrap(), Bottle(), HobnailedBoots(), Bucket(),
			Caltrops(), Chain(), Chest(), Chisel(), Crowbar(),
			Drill(), GrapplingHook(),Hammer(), IronTongs(), Kettle(),
			Ladder(), Lockpicks(), Magnet(), Manacles(), MetalFile(),
			Mirror(), Nails(), Net(), Pick(), Pole(),
			Rope(), Sack(), Scrap(), Shovel(), Soapstone(),
			SurgeonsTools(), Spyglass(), Tent(), Waterskin(), FirePot()]
	return(choices(pool)[0])

def choose_random_light():
	pool = [Candle(), DirectionalLantern(), Lantern(), Oil(), Torch(), Tinderbox()]
	return(choices(pool, weights = [3, 1, 5, 6, 8, 3])[0])

def choose_random_weapon():
	pool = [Sword(), Dagger(), Greatsword(), Bow(), ThrowingKnife(), ThrowingAxe(), CrossBow(), Sling()]
	return(choices(pool, weights = [7,4,3,3,2,1,2,1]))[0]

def choose_random_melee_weapon():
	pool = [Sword(), Dagger(), Greatsword()]
	return(choices(pool, weights = [3,2,1]))[0]

def choose_random_ranged_weapon():
	pool = [Bow(), ThrowingKnife(), ThrowingAxe(), Crossbow(), Sling()]
	return(choices(pool, weights = [3,2,1,2,1]))[0]

def choose_random_sidearm():
	pool = [Dagger(), Sword()]
	return(choices(pool, weights = [3,1]))[0]
	
def choose_random_offhand():
	pool = [Dagger(), Shield(), Buckler()]
	return(choices(pool, weights = [1,3,2]))[0]

def choose_random_armour():
	pool = [Hides(), Gambeson(), MailArmour(), PlateArmour()]
	return(choices(pool, weights = [8,4,2,1]))[0]

def choose_random_light_armour():
	pool = [Hides(), Gambeson()]
	return(choices(pool, weights = [2,1]))[0]

def choose_random_heavy_armour():
	pool = [MailArmour(), PlateArmour()]
	return(choices(pool, weights = [2,1]))[0]

def choose_random_artifact(depth=0):
	r = randint(1,20)+depth
	if r <=10:
		pool = [SeerStone(), SpellEater(), DowsingCharm(),
				Bleeder(), TorchStone(), AlarmBand()]
		return(choices(pool)[0])
	elif r <= 19:
		pool = [Dreamless(), StoneDance(), WeighNoMore(),
				Unmoved(), LyingCoin(), Melder()]
		return(choices(pool)[0])
	else:
		pool = [Transference(), Forgotten(), Annihilation(),
				Incineration(), Transmutation(), Command()]
		return(choices(pool)[0])