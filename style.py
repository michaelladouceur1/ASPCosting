from PyInquirer import style_from_dict, Token

# BLUE
color1 = '#7ec0f7'
# RED
color2 = '#ffaaaf'


style_1 = style_from_dict({
	Token.QuestionMark: color1,
	Token.Pointer: '#7ec0f7 bold',
	Token.Selected: color2
	})