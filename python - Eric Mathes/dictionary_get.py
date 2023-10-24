alien_0 = {'color': 'green', 'speed': 'slow'}

# print(alien_0['points']) this line throws an arrow, bcos there's no 
# points key assigned

# to address issue, get() could be used to handle the error it might throw
point_value = alien_0.get('points', 'No point value assigned')
print(point_value)