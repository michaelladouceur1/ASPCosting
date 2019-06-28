import ezdxf
import math

dwg = ezdxf.readfile('WAR72SRS.40.dxf')
msp = dwg.modelspace()

# def print_entity(e):
#     print("LINE on layer: %s\n" % e.dxf.layer)
#     start = [e.dxf.start[0], e.dxf.start[1]]
#     end = [e.dxf.end[0], e.dxf.end[1]]
#     length = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
#     print(length)
#     print(e.dxf.start)
#     print(e.dxf.end)
#     # print("start point: %s\n" % e.dxf.start)
#     # print("end point: %s\n" % e.dxf.end)

def print_att(e):
	if e.dxf.layer != 'OBJ':
		return 0
	else:
		if e.dxftype() == 'LINE':
			start = [e.dxf.start[0], e.dxf.start[1]]
			end = [e.dxf.end[0], e.dxf.end[1]]
			length = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
			print(f'LINE ({e}): {length}')
		elif e.dxftype() == 'CIRCLE':
			radius = e.dxf.radius
			length = 2*3.14169*radius
			print(f'CIRCLE ({e}): {length}')
		elif e.dxftype() == 'ARC':
			radius = e.dxf.radius
			start = e.dxf.start_angle
			end = e.dxf.end_angle
			length = radius*((end-start)*(3.14159/180))
			if length < 0:
				end = 360
				length = radius*((end-start)*(3.14159/180))
			print(length)
		return length

def blank(msp):
	index = 0
	for e in msp:
		if index < 1:
			x = {'max': e.dxf.start[0], 'min': e.dxf.end[0]}
			y = {'max': e.dxf.start[1], 'min': e.dxf.end[1]}
		else:
			break
	for e in msp:
		if e.dxftype() == 'LINE':
			if e.dxf.start[0] > x['max']:
				print(e.dxf.start[0])
				x['max'] = e.dxf.start[0]
			else:
				x['max'] = x['max']
			if e.dxf.end[0] < x['min']:
				print(e.dxf.end[0])
				x['min'] = e.dxf.end[0]
			else:
				x['min'] = x['min']
			if e.dxf.start[1] > y['max']:
				print(e.dxf.start[1])
				y['max'] = e.dxf.start[1]
			else:
				y['max'] = y['max']
			if e.dxf.end[1] < y['min']:
				print(e.dxf.end[1])
				y['min'] = e.dxf.end[1]
			else:
				y['min'] = y['min']
	blankx = x['max'] - x['min']
	blanky = y['max'] - y['min']
	print(f'BLANK WIDTH: {blankx}')
	print(f'BLANK HEIGHT: {blanky}')

sum = 0
for e in msp:
	sum += print_att(e)

blank(msp)

print(f'TOTAL LENGTH: {sum}')

