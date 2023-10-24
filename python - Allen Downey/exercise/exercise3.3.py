def draw_horizontal_divisions(symbol1, symbol2):
    print(f"{symbol1}{symbol2 * 4}",end= ' ')

def draw_vertical_divisions(symbol1, symbol2):
    print(f"{symbol1}{symbol2 * 4}", end= ' ')

draw_horizontal_divisions('+','-')
draw_horizontal_divisions('+','-')
print("\n")

for i in range(3):
    draw_vertical_divisions("|", ' ')
