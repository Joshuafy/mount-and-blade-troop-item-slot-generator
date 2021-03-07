def getName(line):
	item_entry = line.split(',')
	return '"itm_' + item_entry[0][4:]
	
def getType(line):	
	if 'itp_type_horse' in line:
		return 'horse'
	elif ('itp_type_body_armor' in line or 'itp_type_hand_armor' in line or
	     'itp_type_head_armor' in line or 'itp_type_foot_armor' in line):
		return 'armor'
	elif ('itp_type_bow' in line or 'itp_type_musket' in line or 
	      'itp_type_crossbow' in line or 'itp_type_thrown' in line or 'itp_type_pistol' in line):
		return 'ranged'
	elif 'itp_type_arrows' in line or 'itp_type_bolts' in line or 'itp_type_bullets' in line:
		return 'ammo'
	elif 'itp_type_one_handed_wpn' in line or 'itp_type_two_handed_wpn' in line or 'itp_type_polearm' in line:
		return 'weapon'
	elif 'itp_type_shield' in line:
		return 'shield'
		
def getAbundance(line):
	i = line.find('abundance')
	
	abundance = ''
	for c in range(i + 10, len(line)):
		if line[c] == ')':
			break
		else:
			abundance += line[c]
	
	return abundance
	
def getValue(line):
	item_entry = line.split(',')
	# Get index of flags
	for i in range(len(item_entry)):
		if item_entry[i].find('weight(') != -1:
			break
	# Go one back to get value
	return item_entry[i - 1]
			
def getHorseCharge(line):
	if getType(line) == 'horse':
		i = line.find('horse_charge')
	
		horse_charge = ''
		for c in range(i + 13, len(line)):
			if line[c] == ')':
				break
			else:
				horse_charge += line[c]
	
		return horse_charge
	
def getHorseSpeed(line):
	if getType(line) == 'horse':
		i = line.find('horse_speed')
	
		horse_speed = ''
		for c in range(i + 12, len(line)):
			if line[c] == ')':
				break
			else:
				horse_speed += line[c]
	
		return horse_speed
		
def getHorseManeuver(line):
	if getType(line) == 'horse':
		i = line.find('horse_maneuver')
	
		horse_maneuver = ''
		for c in range(i + 15, len(line)):
			if line[c] == ')':
				break
			else:
				horse_maneuver += line[c]
	
		return horse_maneuver
		
def getBodyArmor(line):
	i = line.find('body_armor(')
	if getType(line) not in ['ranged', 'ammo', 'thrown', 'weapon']:
		if i == -1:
			return '0'
		else:
			body_armor = ''
			for c in range(i + 11, len(line)):
				if line[c] == ')':
					break
				else:
					body_armor += line[c]
			return body_armor
	
def getHeadArmor(line):
	i = line.find('head_armor(')
	if getType(line) not in ['ranged', 'ammo', 'thrown', 'weapon', 'horse', 'shield']:
		if i == -1:
			return '0'
		else:
			head_armor = ''
			for c in range(i + 11, len(line)):
				if line[c] == ')':
					break
				else:
					head_armor += line[c]
			return head_armor
			
def getLegArmor(line):
	i = line.find('leg_armor(')
	if getType(line) not in ['ranged', 'ammo', 'thrown', 'weapon', 'horse', 'shield']:
		if i == -1:
			return '0'
		else:
			leg_armor = ''
			for c in range(i + 10, len(line)):
				if line[c] == ')':
					break
				else:
					leg_armor += line[c]
			return leg_armor
			
def getHitPoints(line):
	i = line.find('hit_points(')
	if i == -1:
		return '100'
	else:
		if getType(line) in ['horse', 'shield']:
			hit_points = ''
			for c in range(i + 11, len(line)):
				if line[c] == ')':
					break
				else:
					hit_points += line[c]
			return hit_points
		
def getDifficulty(line):
	if getType(line) != 'ammo':
		i = line.find('difficulty(')
		if i == -1:
			return '0'
		else:
			difficulty = ''
			for c in range(i + 11, len(line)):
				if line[c] == ')':
					break
				else:
					difficulty += line[c]
			return difficulty
			
def getWeight(line):
	i = line.find('weight(')
	weight = ''
	for c in range(i + 7, len(line)):
		if line[c] == ')':
			break
		else:
			weight += line[c]
	
	return str(int(float(weight) // 1))
	
def getRangedDamage(line):
	if getType(line) in ['ranged', 'thrown', 'ammo']:
		i = line.find('_damage(')
		if i == -1:
			return '0'
		else:
			ranged_damage = ''
			for c in range(i + 8, len(line)):
				if line[c] == ',':
					break
				else:
					ranged_damage += line[c]
			return ranged_damage
			
def getSpeedRating(line):
	i = line.find('spd_rtng(')
	if i != -1:
		spd_rating = ''
		for c in range(i + 9, len(line)):
			if line[c] == ')':
				break
			else:
				spd_rating += line[c]
		return spd_rating
		
def getShotSpeed(line):
	i = line.find('shoot_speed(')
	if i != -1:
		shot_speed = ''
		for c in range(i + 12, len(line)):
			if line[c] == ')':
				break
			else:
				shot_speed += line[c]
		return shot_speed
		
def getHorseUsable(line):
	if line.find('itp_cant_use_on_horseback') != -1:
		return '1'
	else:
		return '0'
		
def getLength(line):
	if getType(line) != 'thrown':
		i = line.find('weapon_length(')
		if i != -1:
			weapon_length = ''
			for c in range(i + 14, len(line)):
				if line[c] == ')':
					break
				else:
					weapon_length += line[c]
			return weapon_length
			
def getMaxAmmo(line):
	if getType(line) == 'ammo':
		i = line.find('max_ammo(')
		if i != -1:
			max_ammo = ''
			for c in range(i + 9, len(line)):
				if line[c] == ')':
					break
				else:
					max_ammo += line[c]
			return max_ammo
			
def getSwingDamage(line):
	if getType(line) == 'weapon':
		i = line.find('swing_damage(')
		swing_damage = '0'
		if i != -1:
			swing_damage = ''
			damage_type = ''
			reached_type = False
			for c in range(i + 13, len(line)):
				if line[c] == ')':
					break
				elif line[c] == ',':
					reached_type = True
				elif not reached_type:
					swing_damage += line[c]
				else:
					damage_type += line[c]
			if damage_type == ' pierce':
				swing_damage = str(int((float(swing_damage) * 1.2) // 1))
			elif damage_type == ' blunt':
				swing_damage = str(int((float(swing_damage) * 1.25) // 1))
		return swing_damage
				
def getThrustDamage(line):
	if getType(line) == 'weapon':
		i = line.find('thrust_damage(')
		thrust_damage = '0'
		if i != -1:
			thrust_damage = ''
			damage_type = ''
			reached_type = False
			for c in range(i + 14, len(line)):
				if line[c] == ')':
					break
				elif line[c] == ',':
					reached_type = True
				elif not reached_type:
					thrust_damage += line[c]
				else:
					damage_type += line[c]
			if damage_type == ' pierce':
				thrust_damage = str(int((float(thrust_damage) * 1.2) // 1))
			elif damage_type == ' blunt':
				thrust_damage = str(int((float(thrust_damage) * 1.25) // 1))
		return thrust_damage
		
def getShieldWidth(line):
	if getType(line) == 'shield':
		i = line.find('shield_width(')
		if i == -1:
			return '25'
		else:
			shield_width = ''
			for c in range(i + 13, len(line)):
				if line[c] == ')':
					break
				else:
					shield_width += line[c]
			return shield_width
		
def parseHorse(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getHorseCharge(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getHorseSpeed(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getHorseManeuver(line) + '),')
	print('    (item_set_slot, ' + name + ', 17, ' + getBodyArmor(line) + '),')
	print('    (item_set_slot, ' + name + ', 18, ' + getHitPoints(line) + '),')
	print('    (item_set_slot, ' + name + ', 8, ' + getDifficulty(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
def parseArmor(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getBodyArmor(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getLegArmor(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getHeadArmor(line) + '),')
	print('    (item_set_slot, ' + name + ', 17, ' + getWeight(line) + '),')
	print('    (item_set_slot, ' + name + ', 8, ' + getDifficulty(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
def parseRangedWeapon(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getRangedDamage(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getSpeedRating(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getShotSpeed(line) + '),')
	print('    (item_set_slot, ' + name + ', 8, ' + getDifficulty(line) + '),')
	print('    (item_set_slot, ' + name + ', 19, ' + getHorseUsable(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
def parseAmmo(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getLength(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getMaxAmmo(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getRangedDamage(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
def parseWeapon(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getSwingDamage(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getThrustDamage(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getSpeedRating(line) + '),')
	print('    (item_set_slot, ' + name + ', 17, ' + getLength(line) + '),')
	print('    (item_set_slot, ' + name + ', 8, ' + getDifficulty(line) + '),')
	print('    (item_set_slot, ' + name + ', 19, ' + getHorseUsable(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
def parseShield(line):
	name = getName(line)
	print('    (item_set_slot, ' + name + ', 9, ' + getBodyArmor(line) + '),')
	print('    (item_set_slot, ' + name + ', 10, ' + getSpeedRating(line) + '),')
	print('    (item_set_slot, ' + name + ', 16, ' + getHitPoints(line) + '),')
	print('    (item_set_slot, ' + name + ', 17, ' + getShieldWidth(line) + '),')
	print('    (item_set_slot, ' + name + ', 8, ' + getDifficulty(line) + '),')
	print('    (item_set_slot, ' + name + ', 19, ' + getHorseUsable(line) + '),')
	print('    (item_set_slot, ' + name + ', 65, 0),')
	print('    (item_set_slot, ' + name + ', 66, ' + getAbundance(line) + '),')
	print('    (item_set_slot, ' + name + ', 67, ' + getValue(line) + '),')
	
with open('itemsource.txt') as file:
	for line in file:
		type = getType(line)
		if type == 'horse':
			parseHorse(line)
		elif type == 'armor':
			parseArmor(line)
		elif type == 'ranged':
			parseRangedWeapon(line)
		elif type == 'ammo':
			parseAmmo(line)
		elif type == 'weapon':
			parseWeapon(line)
		elif type == 'shield':
			parseShield(line)
		else:
			print('ERROR: Unrecognized Item Type')
				