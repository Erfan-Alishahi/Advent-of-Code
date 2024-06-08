def analys(game):
    threshold = {'red': 12, 'green': 13, 'blue': 14}
    game_number, game_sets = game.split(':')[0].split()[1], game.split(':')[1]
    sets = game_sets.split(';')
    flag = True
    for set in sets:
        colors = set.split(',')
        for color in colors:
            color_num, color_name = color[1:].split()
            if threshold[color_name] < int(color_num):
                flag = False
    if flag:
        return int(game_number)
    else:
        return 0

with open(f'<.txt>') as file: # Enter text file path into <.txt>
    text = file.readlines()

Point = 0
for line in text:
    Point += analys(line)
print(Point)