from random import randint
from random import seed
seed(123)
from random import choices
import dice
import functions
import item
import monster
import encounter
import json

class Dungeon:
	def __init__(self, name='unnamed dungeon', x=0, y=0, size=6):
		self.name = name
		self.x = x
		self.y = y
		self.floor = []
		self.floor_size = size
	
	def add_floor(self, depth):
		self.floor.append(Floor(depth, self.floor_size))
		
	def __repr__(self):
		ostr = self.name + ' at position: ' + str(self.x) + ' / ' + str(self.y)
		ostr += '\nwith ' + str(len(self.floor)) + ' floors'
		return(ostr)
	
	def __str__(self):
		ostr = self.name + ' at position: ' + str(self.x) + ' / ' + str(self.y)
		ostr += '\nwith ' + str(len(self.floor)) + ' floors'
		for f in self.floor:
			ostr += str(f)
		return(ostr)
	
	def to_json(self):
		return json.dumps(self._attr)


class Floor:
	def __init__(self, depth, size):
		self.depth = depth
		self.size = size
		self.room = []
		self.draw_hallways()
		self.draw_rooms()

	def __repr__(self):
		ostr = '\n################################################\n'
		ostr += 'Floor depth: ' +str(self.depth)+ '\n'
		ostr += '\n################################################\n'
		ostr += self.print_layout()
		return(ostr)
	
	def __str__(self):
		ostr = '\n################################################\n'
		ostr += 'Floor depth: ' +str(self.depth)+ '\n'
		ostr += '\n################################################\n'
		ostr += self.print_layout()
		for r in self.room:
			ostr += str(r)
		return(ostr)
		
	def get_room(self,x,y):
		for r in self.room:
			if r.x == x and r.y == y:
				return(r)
			
	def draw_hallways(self):
		size = self.size
		# Hallways entering the dungeon start at every side
		x1 = randint(1,size)
		y1 = randint(1,size)
		x2 = randint(1,size)
		y2 = randint(1,size)
		
		#first draw a horizontal hallway through the structure then clockwise until it hits another hallway
		for x in range(1,size+1):
#			print('drawing:',x,y1)
			self.room.append(Room(x,y1,self.depth,is_hallway=True))
		if self.size >3:
			for y in range(1,size+1):
				if self.get_room(x1,y) != None:
					break
				else:
#					print('drawing:',x1,y)
					self.room.append(Room(x1,y,self.depth,is_hallway=True))
		elif self.size >4:
			for x in range(size,0,-1):
				if self.get_room(x,y2) != None:
					break
				else:
#					print('drawing:',x,y2)
					self.room.append(Room(x,y2,self.depth,is_hallway=True))
		elif self.size >5:
			for y in range(size,0,-1):
				if self.get_room(x2,y) != None:
					break
				else:
#					print('drawing:',x2,y)
					self.room.append(Room(x2,y,self.depth,is_hallway=True))

	def draw_rooms(self):
		size = 0	# CHANGE FLOORSIZE IN FUNCTION draw_hallways
		for r in self.room:
			if r.x >= size:
				size = r.x
			elif r.y >= size:
				size = r.y
		for x in range(1,size+1):
			for y in range(1,size+1):
				if self.get_room(x,y) == None:
					self.room.append(Room(x,y,self.depth))
#					print('drawing room at: ',x,y)
				else:
					pass
#					print('passing over: ',x,y)

	def print_layout(self):
		size = 0	# CHANGE FLOORSIZE IN FUNCTION draw_hallways
		for r in self.room:
			if r.x >= size:
				size = r.x
			elif r.y >= size:
				size = r.y
		buff = ''
		for y in range(1,size+1):
			for x in range(1,size+1):
				if self.get_room(x,y) != None:
					if self.get_room(x,y).type == 'hallway':
						buff += '#'
					else:
						#buff += '0'
						buff += self.get_room(x,y).type[0]
				else:
					buff += '.'
			buff += '\n'
		return(buff)


class Room:
	def __init__(self,x,y,depth,is_hallway=False):
		self.x = x
		self.y = y
		self.depth = depth
		self.type = ''
		self.feature = '' 
		self.encounter = []
		if is_hallway == False:
			self.gen_room(r = randint(1,20), s = randint(1,12))
			self.gen_feature(depth = 'auto', roll = randint(1,10))
		else:
			self.type = 'hallway'

	def __repr__(self):
		ostr = 'Room x: '+str(self.x)+' y: '+str(self.y)+' depth: '+str(self.depth)
		ostr += '\n'+self.type[0:10]
		return(ostr)
	
	def __str__(self):
		ostr = '\n++++++++++++++++++++++++++++\n'
		ostr = (ostr + 'Position: X: '+str(self.x)
							  +' Y: '+str(self.y)
							  +' depth: '+str(self.depth)
					+'\n'+self.type
					+'\nFeature:\n'+self.feature
					+'\nEncounters:\n'+str(self.encounter)
				)
		return(ostr)


	def gen_room(self, r = randint(1,20), s = randint(1,12)):
		ostr = ''
# 1 PLAZA
		if r == 1:
			ostr = ('Plaza - A wide expanse of tiled floor stretches '
					+'out into the dark. If there is a ceiling above it '
					+'is too high to be seen. Occasionally populated with '
					+'strange “sculptures” these open spaces also tend to '
					+'be ambush spots for more conniving individuals.'
				   )
			if s <= 4:
	# 1-1 STATUE GARDEN
				ostr = ostr + ('\nStatue Garden - Odd geometric stones '
							   +'crowd this area, making direct travel '
							   +'difficult and unnerving.'
							  )
				if (randint(1,6)>=5):
					self.encounter.append(encounter.Bandits())
			elif s <= 8:
	# 1-2 OBELISK
				ostr = ostr + ('\nObelisk - towering and foreboding, '
							   +'a single obelisk rests in the center '
							   +'of the plaza. Seen as an object of worship, '
							   +'some have left offerings behind. '
							   + str(randint(1,10)+randint(1,10))
							   +' coins and ' + str(randint(1,6))
							   +' random tools'
							  )
			else:
	# 1-3 EERILY EMPTY
				ostr = ostr + ('\nEerily Empty - It is uncannily barren. Voices travel far and echoes return as whispers.'
							  )
# 2 GRAVEYARD
		elif r == 2:
			ostr = ('Graveyard - Countless '
					+'identical plinths sit arranged in '
					+'dozens of ordered rows. A'
					+'solemn atmosphere permeates'
					+'this area.'
					+'Those with more macabre '
					+'sensibilities see the grave-like '
					+'similarities right away. Some '
					+'go so far as to turn the place '
					+'into a makeshift cemetery.'
				   )
			if s <= 4:
				ostr = ostr + ('\nHollow Coffers - The plinths '
							   +'are hollow and crack open with '
							   +'a blow from a sledge. Doing so '
							   +'draws attention, roll on the '
							   +'encounter table. Inside each '
							   +'coffer is a single silver “coin.”'
							  )
			elif s <= 8:
				ostr = ostr + ('\nCharnel House - Skulls and '
							   +'remains have been carefully '
							   +'stacked on the plinths, names '
							   +'and epitaphs scratched into '
							   +'them. Some are ancient... '
							  )
			else:
				ostr = ostr + ('\nQuiet - The air is still here and '
							   +'demands reverence of some form.'
							  )
# 3 ARCHIVE
		elif r == 3:
			ostr = ('Archive - Row after row of '
					+'towering structures are '
					+'arranged like the shelves of '
					+'some massive library. They '
					+'stand dozens of feet tall and '
					+'stretch thrice that in length. '
					+'The structures here appear '
					+'imposing, but time has taken '
					+'their toll and some are close to '
					+'collapse.'
				   )
			if s <= 6:
				ostr = ostr + ('\nCarved - The sides of these '
							   +'shelves are patterned with '
							   +'geometric forms like some '
							   +'alien mural, they are quite easy '
							   +'to climb.'
							  )
			else:
				ostr = ostr + ('\nTeetering - the shelves stand '
							   +'precariously and could be '
							   +'toppled with a strong push or '
							   +'two. Doing so causes them to '
							   +'domino in catastrophic fashion, '
							   +'dealing 10d6 to anyone caught '
							   +'underneath and alerting all in '
							   +'earshot, roll on the encounter '
							   +'table.'
							  )
# 4 KENNELS
		elif r == 4:
			ostr = ('Kennel - Small claustrophobic '
					+'rooms are arranged like '
					+'cabinets along a massive '
					+'shear wall. Skittering can be '
					+'heard far above.'
					+'The kennels tend to attract life, '
					+'both mortal and not.\n'
					+'Climbing up to the rooms reveals '
					+'remains of refuges and '
					+'hideouts, along with more dangerous life...\n'
					+'You Find...\n'
				   )
			if s <= 6:
				ostr = ostr + ('nothing')
			elif s <= 8:
				ostr = ostr + ('a random tool: '+str(item.choose_random_miscellania()))
			elif s <= 10:
				ostr = ostr + ('a terrified traveler')
			else:
				ostr = ostr + ('one of the crawl')
# 5 OUBLIETTE
		elif r == 5:
			ostr = ('Oubliette - The floor of this '
					+'room is a steep and sleek '
					+'funnel that leads to a single '
					+'hole just large enough for a '
					+'mortal to slip into. '
					+'Walking across this room is '
					+'difficult, save versus Breath or '
					+'slide into the hole and drop '
					+'1d6x10 feet. The pit is never '
					+'empty...'
				   )
			if s <= 3:
				amt = randint(1,10)
				ostr = ostr + ('\nCorpse Pile - The crumbling '
							   +'remains of previous victims. '
							   +'There are 1d10 random tools if '
							   +'you dig them out.'
							  )
				for i in range(0,randint(1,10)):
					ostr = ostr +'\n'+str(item.choose_random_miscellania())

			elif s <= 6:
				ostr = ostr + ('\nHidden Treasure - Buried '
							   +'among the pile of dust and '
							   +'dried bone at the bottom is '
							   +'something of value. (roll on the '
							   +'treasure table pg. 21)'
							   +'\n'+str(item.choose_random_artifact(depth=self.depth))
							  )
			elif s <= 9:
				ostr = ostr + ('\nSomeone Trapped - They cry '
							   +'out weakly to be rescued from '
							   +'the pit. Close to death, they will '
							   +'perish without immediate '
							   +'assistance. They will be a '
							   +'helpful companion if saved.'
							  )
			else:
				ostr = ostr + ('\nSome Creature - '
							   +'it is either trapped down here or '
							   +"has made it it's lair. "
							   +'The creature may be hostile or passive.'
							  )

# 6 TEMPLE
		elif r == 6:
			ostr = ('Temple - A gateway leads into a lengthy room with a vaulted '
					+'ceiling and terminates into a sanctum. The sanctum ceiling '
					+'spirals up into the dark, defying your eyes.'
					+'\nThis place has an odd effect on '
					+'the minds of pious travelers. '
					+'Drawn like moths to the flame to worship this space.'
				   +'')
#Subtype					
			if s <= 4:
				ostr = ostr + ('\nAltar - An enormous geometric '
							   +'sculpture of strange and '
							   +'wicked shape sits as some '
							   +'grim centerpiece. It is '
							   +'engraved with veins of '
							   +'precious metal worth '
							   +str(randint(1,6)*50)
							   +'coins if stripped.'
							  )
			elif s <= 8:
				ostr = ostr + ('\nThrone - A singular pedestal '
							   +'sits upon a wide and regal '
							   +'base. Akin to some seat for a '
							   +'massive being, an object of '
							   +'importance has been left upon '
							   +'it. (Roll on the treasure table) '
							   +'\n'+str(item.choose_random_artifact(depth=self.depth))
							  )
			else:
				ostr = ostr + ('\nWorshipers - 1d20 penitent '
							   +'and troubled souls gather here '
							   +'in the dark. They feverishly '
							   +'worship with desperate '
							   +'whispers. Attack if disturbed. '
							  )
				self.encounter.append(encounter.FeverishFaithful())
# 7 PIT
		elif r == 7:
			ostr = ('Pit - The floor gives way, in its '
					+'place lies a cavernous pit that '
					+'drops into the dizzying dark. '
					+'There is no bottom in sight. '
					+'A vertical descent that leads '
					+'deeper into the ruins.')
#Subtype					
			if s <= 4:
				ostr = ostr + ('\nTiered - Series of stair-like tiers '
							   +'descend into to dark. Descent '
							   +'and ascent is easy. Depth +1.'
							  )
			elif s <= 8:
				ostr = ostr + ('\nDistressed - It appears as a '
							   +'collapsed sinkhole at first, yet '
							   +'the walls of the pit are strange '
							   +'geometric patterns. It can be '
							   +'climbed, albeit with some '
							   +'difficulty. Depth +1.'
							  )
			else:
				ostr = ostr + ('\nShear - A smooth square pit '
							   +'descends down into the dark. It '
							   +'will require climbing gear to '
							   +'rappel... Depth +'+str(randint(1,6))
							  )
# 8 VAULT
		elif r == 8:
			ostr = ('Vault - A short room terminates '
					+'with an enormous gate of '
					+'some kind. A wall of rusted iron '
					+'acts as a featureless and '
					+'imposing door. A gentle hum '
					+'can be heard on the other side. '
					+'There is treasure here, for '
					+'those forceful or cunning '
					+'enough to pilfer it. '
					+'The “door” of rusted iron is as '
					+'thick as a fist and will be '
					+'difficult to break into. Those '
					+'who find a way in will be '
					+'rewarded with blocks of '
					+'identical lodestone worth '
					+str(randint(100,1000))
					+'coins and 1d3 '
					+'treasures.'
				   )
			for i in range(0, randint(1,3)):
				ostr = ostr + '\n' + str(item.choose_random_artifact(depth=self.depth))
# 9 ATRIUM
		elif r == 9:
			ostr = ('Atrium - A massive open '
				   +'space lies below an imposing '
				   +'ceiling of crumbling structural '
				   +'supports. Ahead is a grand '
				   +'entryway further into the ruins, '
				   +'as if this is some transitional '
				   +'area. '
				   +'Travelers gather at this '
				   +'precipice. Perhaps a '
				   +'subconscious will of the ruins '
				   +'or some long forgotten '
				   +'tradition. '
				   +'A makeshift camp with 1d6 '
				   +'Travelers, willing to trade '
				   +'goods and information.'
				   )
# 10 TOWER
		elif r == 10:
			ostr = ('Tower - A vertical chimney '
				   +'travels up to frightful heights, '
				   +'the ceiling of which is beyond '
				   +'sight. Echoes seem to linger in '
				   +'the dark space far above. '
				   +'This room leads to the surface '
				   +'if it appears at a Depth greater '
				   +'than 1, otherwise it leads to '
				   +'nowhere except a ceiling '
				   +'hundreds of feet up.'
				   +'There is a 2-in-6 chance the '
				   +'tower has something akin to '
				   +'stairs, otherwise it must be '
				   +'scaled with some difficulty.'
				   )
#Subtype					
			if s <= 4:
				ostr = ostr + ('\nThe tower has stairslike protrusions '
							   +'making for an easy ascend.'
							  )
			else:
				ostr = ostr + ('\nThe once smooth surface of the tower '
							   +'has been eroded by time. '
							   +'Enabeling explorers to climb it '
							   +'with some difficulty.'
							  )
# 11 OSSUARY
		elif r == 11:
			ostr = ('Ossuary - A long and winding '
				   +'tunnel with smooth cracked '
				   +'walls is peppered with small '
				   +'hand-sized holes. The holes '
				   +'burrow deep and seem to go '
				   +'on forever. '
				   +'The holes here are not empty. '
				   +'Filled with curious trinkets as '
				   +'well as curious dangers. Roll '
				   +'1d6 anytime a Traveler '
				   +'searches a hole.'
				   +'\nYou Find...'
				   )
#Subtype					
			if s <= 2:
				ostr = ostr + '\nBone - Broken bits or teeth.'
			elif s <= 4:
				ostr = ostr + '\nOil - Flammable, burns 1 hour.'
			elif s <= 6:
				ostr = ostr + '\nCoin - A flat silver disk.'
			elif s <= 8:
				ostr = ostr + '\nLodestone - A perfect sphere.'
			elif s <= 10:
				ostr = ostr + '\nBite - Suffer 1d6 damage.'
			else:
				ostr = ostr + '\nKeepsake - Something small from home...'
# 12 GREAT HALL
		elif r == 12:
			ostr = ('Great Hall - Identical sequoia- '
					+'sized pillars stand in perfect '
					+'rows, holding up the ceiling of '
					+'this titanic room. Rumbling can '
					+'be heard above as the pillars '
					+'creak with the impossible '
					+'weight they bear. '
					+'Noise travels quickly here, '
					+'sometimes alerting unwanted '
					+'attention...'
				   )
			# add an extra encounter roll for this one
			self.encounter.append(encounter.choose_random_encounter(depth=self.depth))
# 13 MAZE
		elif r == 13:
			ostr = ('Maze - The walls close tightly '
					+'here, twisting and turning in '
					+'uncomfortable directions both '
					+'vertical and horizontal. The '
					+'path splits in places, a hellish '
					+'fractal maze. '
					+'With no pattern or sensible '
					+'layout, it is far too easy to get '
					+'lost in this maze...\n'
					+'Travelers must roll 3 '
					+'successful Intelligence checks '
					+'in a row to make it through this '
					+'area\n.'
					+'Failure: 1d6 hours of '
					+'time have been lost and roll an '
					+'encounter.'
				   )
# 14 BATHHOUSE
		elif r == 14:
			ostr = ('Bathhouse - Deep circular'
					+'basins are carved into the floor'
					+'of this room. Each is filled with'
					+'water and sediment including'
					+'chunks of stone from the'
					+'fractured ceiling.\n'
					+'The filthy water replenishes'
					+'here from the countless cracks'
					+'and fractures after a day. It is'
					+'drinkable but only after being'
					+'distilled or sanitized. There is a'
					+'1-in-20 chance of treasure'
					+'hidden in the detritus at the'
					+'bottom of one of the basins.'
				   )
			if randint(1,20) == 20:
				ostr = ostr + '\n' + str(item.choose_random_artifact(depth=self.depth))
# 15 AMPHITHEATER
		elif r == 15:
			ostr = ('Amphitheater - A massive '
					+'semicircular room, the floor is '
					+'nothing but rows of concentric '
					+'steps that lead to a singular '
					+'small stage against a flat '
					+'decaying wall.'
				   )
#Subtype					
			if s <= 4:
				ostr = ostr + ('\nFalse whispers - The acoustics '
							   +'are strange here. Whispers are '
							   +'heard from all angles...'
							  )
			elif s <= 8:
				ostr = ostr + ('\nObservers - There are 2d6 '
							   +'mortals diligently watching the '
							   +'“stage.” They are enthralled by '
							   +'“the show” and demand '
							   +'silence, growing violent if the '
							   +'Travelers cause a scene.'
							  )
			else:
				ostr = ostr + ('\nThe Thespian - A tall jet-black'
							   +'figure stands silently in the '
							   +'center of the “stage.” They '
							   +'speak only when spoken to '
							   +'and answers with elegant, '
							   +'theatrical flourishes of their '
							   +'body.\n'
							   +'They know more about the '
							   +'Vast than anyone else, and '
							   +'are more dangerous than the '
							   +'oldest of the Crawl...'
							   )
# 16 CELLAR
		elif r == 16:
			ostr = ('Cellar - Angled channels lead '
				   +'into tight, claustrophobic '
				   +'rooms. They are cold, like a '
				   +'graveyard in winter.\n'
				   +'The cold is unbearable after '
				   +'several hours, yet the rooms '
				   +'have an odd quirk: Nothing '
				   +'rots, decays or ages so long as '
				   +'they stay in one of the rooms.'
				   )
# 17 PLANETARIUM
		elif r == 17:
			ostr = ('Planetarium - A titanic domed '
				   +'room, large enough to house a '
				   +'castle, echos with every step. '
				   +'Strange coiling cosmic designs '
				   +'cover the ceiling, the detail '
				   +'impossibly intricate. '
				   +'This room has odd effects on '
				   +'the psyche of mortals. Those '
				   +'who dare to meditate or to '
				   +'dream within this room are '
				   +'visited by its power...\n'
				   +'Roll 1d20+WIS, INT, or CHA\n'
				   +'1: You dream of the Crawl, '
				   +'their pain, their anguish, their '
				   +'hate.\n'
				   +'  Lose a Memory (pg. 22).\n'
				   +'2-10: Senseless visions, dream-mazes '
				   +'of impossible geometry.\n'
				   +'  Gain a level of exhaustion\n'
				   +'11-15: A vision of things yet to '
				   +'pass.\n'
				   +'  You may make one roll at '
				   +'advantage the next day.\n'
				   +'16-18: The fractal geometry '
				   +'spreads before you.\n'
				   +'  You know '
				   +'what the next 1d6 rooms will '
				   +'contain.\n'
				   +'19-20: You dream of home, of the '
				   +'life before the Vast.\n'
				   +'  You regain one memory (pg. 22).\n'
				   +'21+: You dream of the Schema.\n'
				   +'  The Wyrm will arrive shortly, '
				   +'defeat it and you will be '
				   +'rewarded with a great treasure.'
)
# 18 DORMITORY
		elif r == 18:
			ostr = ('Dormitory - Slabs of oblong '
					+'stone lie in perfect rows like '
					+'mortuary tables. The air is still, '
					+'breathing seems difficult.\n'
					+'This place has not earned its '
					+'name for just looks. Travelers '
					+'who rest upon the slabs fall '
					+'into a deep, unbreakable '
					+'sleep. They remain unchanged '
					+'in a form of stasis until they are '
					+'awoken by an outside source.'
				   )
			if randint(1,6) == 6:
				ostr = ostr + ('\nSomeone is asleep upon one of '
							   +'the slabs. Their age is '
							   +'uncertain as are their motives.'
							  )
# 19 DUMP
		elif r == 19:
			ostr = ('Dump - Channels from the '
					+'walls and ceiling rhythmically '
					+'dump mounds of detritus into '
					+'the recessed floor of this room. '
					+'Broken architecture, soiled '
					+'water, graveled sand, it all '
					+'ends in the floor of this room.\n'
					+'Many things find their way into '
					+'this great dump, some are '
					+'even useful.\n'
					+'For every hour spent searching '
					+'the mounds of garbage in this '
					+'room there is a 3-in-6 chance '
					+'of finding something useful:\n'
					+'1-3: nothing\n'
					+'4: A random tool\n'
					+'5: 1d6x10 lodestone.\n'
					+'6: 1d3 unspoiled rations.\n'
					+'However, there is also a 3-in-6\n'
					+'chance of suffering harm:\n'
					+'1-3: nothing\n'
					+'4: Cuts and bruises, 1d6 damage.\n'
					+'5: A serious injury, 1 exhaustion.\n'
					+'6: A hidden enemy, roll encounter.'
				   )
		elif r == 20:
			ostr = ('Pyramid - Gargantuan and '
					+'imposing, a massive multi- '
					+'faceted pyramid sits like some '
					+'terrible beast. Closer '
					+'inspection reveals it is crafted '
					+'from a singular piece of '
					+'stone...'
				   )
#Subtype					
			if s <= 4:
				ostr = ostr + ('\nGlimmering Capstone - Made '
							   +'of lodestone and engraved with '
							   +'fractal veins of gold. Weighing '
							   +'500 lbs. it is worth 1d6x200 ('
							   +str(randint(200,1200))
							   +') coins if safely transported.'
							  )
			elif s <= 8:
				ostr = ostr + ('\nMaddening hum - Every hour '
							   +'spent here requires a Save '
							   +'versus Charm or gain a level of '
							   +'exhaustion.'
							  )
			else:
				ostr = ostr + ('\nCrumbling - The sides if the '
							   +'pyramid are unstable, like a '
							   +'mountain before an avalanche. '
							   +'Disturbing the pyramid causes '
							   +'a landslide of rubble to come '
							   +'rolling down, dealing 5d6 to all '
							   +'caught in its path.'
							  )
#write the description to memory
		self.type = ostr
#add an encounter
		self.encounter.append(encounter.choose_random_encounter(depth=self.depth))

	def gen_feature(self, depth = 'auto', roll = randint(1,10)):
		if depth == 'auto':
			depth = self.depth
		r = roll+depth
		if r == 1:
			self.feature = ('Dead Traveler - Petrified and desiccated, '
							+'a mournful look on their face. There is a 2-in-6 '
							+'chance they have a random tool:\n'
							+str(item.choose_random_miscellania())
						   )
		elif r == 2:
			self.feature = ('Map - Scratched and carved with ragged haste. '
							+'You can see what the next '
							+str(randint(1,6))
							+' rooms will be.'
						   )
		elif r == 3:
			self.feature = ('Shaft - A small vertical descent into the dark.'
							+'\n+1 Depth'
						   )
		elif r == 4:
			self.feature = ('Stairs Down - Unsteady geometric protrusions lead down.'
							+'\n+1 Depth'
						   )
		elif r == 5:
			strbuff = 'Crevasse - A cracked scar runs the length of the room.'
			if randint(1,2) == 2:
				strbuff = strbuff + '+' + str(randint(1,3)) + ' Depth'
			self.feature = strbuff
		elif r == 6:
			self.feature = ('Devastation - Broken, collapsed and crumbling. '
							+'This room takes twice as long to cross.'
						   )
		elif r == 7:
			strbuff = 'Excavation - Someone or something has been digging:\n'
			s = randint(1,3)
			if s == 1:
				strbuff = strbuff + 'A hollow cavern.'
			elif s == 2:
				strbuff = strbuff + 'A lodestone deposit.'
			else:
				strbuff = strbuff + 'Deep down below. +1 Depth.'
			self.feature = strbuff
		elif r == 8:
			self.feature = 'Spoiled Pool - Deep puddles of foul-smelling water.'
		elif r == 9:
			self.feature = "Stagnant Pool - A basin of clear, tasteless water. One week's worth."
		elif r == 10:
			strbuff = ('Stash of Loot - Tucked away by someone for later use. '
							+ str(randint(1,6)) + ' rations.'
					  )
			for i in range(randint(1,6)):
				r = randint(1,20)
				if r <= 17:
					strbuff = strbuff +'\n'+str(item.choose_random_miscellania())
				elif r <= 19:
					strbuff = strbuff +'\n'+str(item.choose_random_light())
				else:
					strbuff = strbuff +'\n'+str(item.choose_random_weapon())
			self.feature = strbuff
		elif r == 11:
			self.feature = 'Warning - Cryptic and foreboding, scratched hastily into a surface.'
		elif r == 12:
			self.feature = 'Bone pile - Like gravel across a tail, the floor is littered with countless broken bones.'
		elif r == 13:
			self.feature = ('Bug Nest - Buzzing diminutive life gathers in the dark. '
						   +'Can be harvested for '+str(randint(1,3)*randint(1,3))+' rations.'
						   )
		elif r == 14:
			self.feature = ('Vein of Metal - Vast sections of rusted iron or '
							+'corroded copper. It can be mined '
							+'and sold as raw lodesone.'
						   )
		elif r == 15:
			self.feature = ('Vein of Precious Metal - Streaks and accents '
							+'of shimmering metal. Can be mined and sold as '
							+'raw lodestone but twice the value.'
						   )
		elif r == 16:
			strbuff = ('Abandoned Camp - Scattered remains and supplies.'
							+ str(randint(1,6)) + ' rations.'
					  )
			for i in range(randint(1,3)):
				r = randint(1,20)
				if r <= 14:
					strbuff = strbuff +'\n'+str(item.choose_random_miscellania())
				elif r <= 17:
					strbuff = strbuff +'\n'+str(item.choose_random_light())
				elif r <= 19:
					strbuff = strbuff +'\n'+str(item.choose_random_weapon())
				else:
					strbuff = strbuff +'\n'+str(item.choose_random_armour())
			self.feature = strbuff
		elif r == 17:
			self.feature = ('Ration Stockpile - Enormous, neatly stacked '
							+'blocks of pemmican, enough to feed '
							+str(randint(1,20)) + ' persons for '
							+str(randint(1,6)) + ' months.'
						   )
		elif r == 18:
			self.feature = ('Treasure - Hidden among the corners '
							+'and recesses is something of value. '
							+'\n'+str(item.choose_random_artifact(depth=self.depth))
						   )
		elif r == 19:
			self.feature = ('Cave-in - A collapse has rendered this room '
							+'impassable. There is no way forward, remove '
							+'additional entryways and exits.'
						   )
		else:
			self.feature = ('A familiar Room - This place is calm and '
							+'strangely familiar. Do you know what it is?'
						   )


seed(123)
#d = Dungeon()
#for depth in range(1,11):
#	d.add_floor(depth)
#print(d)
#print(str(d)[-1000:])


		
#	r.gen_room(i)
#	print(r.x)
#	print(r.y)
#	print(r.depth)
#	print(r.type)
#	print(r.feature)
#	print(r.encounter)

d = Dungeon(size=3)
for depth in range(1,20):
	d.add_floor(depth)
print(d)