import ezdxf
import math

class DXF:
	def __init__(self, dwg):
		try:
			drawing = ezdxf.readfile(f'{dwg}.dxf')
		except FileNotFoundError:
			raise FileNotFoundError(f'{dwg} CANNOT BE FOUND') from None
		self.msp = drawing.modelspace()

	def length(self):
		def line(e):
			start = [e.dxf.start[0], e.dxf.start[1]]
			end = [e.dxf.end[0], e.dxf.end[1]]
			return math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)

		def circle(e):
			return 2*math.pi*e.dxf.radius

		def arc(e):
			radius = e.dxf.radius
			start = e.dxf.start_angle
			end = e.dxf.end_angle
			length = radius*((end-start)*(math.pi/180))
			if length < 0:
				end = 360
				length = radius*((end-start)*(math.pi/180))
			return length

		def polyline(e):
			points = []
			vertices = []
			length = 0
			for i in e.points():
				points.append(i)
			for i in range(len(points)-1):
				inf = math.sqrt((points[i][0]-points[i+1][0])**2 + (points[i][1]- 
				points[i+1][1])**2)
				length += inf
			return length

		sum = 0
		for e in self.msp:
			if e.dxf.layer != 'OBJ':
				return 0
			else:
				if e.dxftype() == 'LINE':
					length = line(e)
				elif e.dxftype() == 'CIRCLE':
					length = circle(e)
				elif e.dxftype() == 'ARC':
					length = arc(e)
				elif e.dxftype() == 'POLYLINE':
					length = polyline(e)
				else:
					print('SOMETHING I DONT KNOW')
					length = 0
			sum += length
		return sum

	def blank(self):
		index = 0
		for e in self.msp:
			if e.dxftype() == 'LINE':
				x = {'max': e.dxf.start[0], 'min': e.dxf.end[0]}
				y = {'max': e.dxf.start[1], 'min': e.dxf.end[1]}
				break
			else:
				continue
		for e in self.msp:
			if e.dxftype() == 'LINE':
				if e.dxf.start[0] > x['max']:
					x['max'] = e.dxf.start[0]
				else:
					x['max'] = x['max']
				if e.dxf.end[0] < x['min']:
					x['min'] = e.dxf.end[0]
				else:
					x['min'] = x['min']
				if e.dxf.start[1] > y['max']:
					y['max'] = e.dxf.start[1]
				else:
					y['max'] = y['max']
				if e.dxf.end[1] < y['min']:
					y['min'] = e.dxf.end[1]
				else:
					y['min'] = y['min']
		blankx = x['max'] - x['min']
		blanky = y['max'] - y['min']
		return blankx, blanky


# dxf = DXF('test2')



# sum = dxf.length()

# blankx,blanky = dxf.blank()

# print(f'TOTAL LENGTH: {sum}')
# print(f'BLANK WIDTH: {blankx}')
# print(f'BLANK HEIGHT: {blanky}')
