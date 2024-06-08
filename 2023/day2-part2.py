def analys(game):
    game_number, game_sets = game.split(':')[0].split()[1], game.split(':')[1]
    sets = game_sets.split(';')
    color_unit = {'red': [0], 'green': [0], 'blue': [0]}
    for set in sets:
        colors = set.split(',')
        for color in colors:
            color_num, color_name = color[1:].split()
            color_unit[color_name].append(int(color_num))
    return (max(color_unit['blue']) * max(color_unit['green']) * max(color_unit['red']))
with open(r'<.txt>') as file: # Enter text file path into <.txt>
    text = file.readlines()

Point = 0
for line in text:
    Point += analys(line)
print(Point)
