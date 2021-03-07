line_num = 0
with open('troopsource.txt') as file:
	for line in file:
		if line_num % 3 == 0:
			name = '"trp_'
			started = False
			ended = False
			for c in line:
				if ended:
					break
				if started:
					name += c
				if c == '"' and started:
					ended = True
				if c == '"' and not started:
					started = True
			print('    (troop_set_slot, ' + name + ', 169, 0),')
			print('    (troop_set_slot, ' + name + ', 170, 0),')
			print('    (troop_set_slot, ' + name + ', 171, 0),')
			print('    (troop_set_slot, ' + name + ', 172, 0),')
		line_num += 1