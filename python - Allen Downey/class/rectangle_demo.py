from point_demo import Point

import copy

class Rectangle:
    """
    Represents a rectangle:
    
    attributes: width, height and corner
    """

box = Rectangle()
box.width = 6
box.height = 3
box.corner = Point()
box.corner.x = 0
box.corner.y = 0

box2 = copy.copy(box) # bcos copy is a shallow operation, deepcopy is used when 
                      # you need to copy an object and its embedded objects
print(box is box2)
print(box.corner is box2.corner)

box3 = copy.deepcopy(box)
print(box is box3)
print(box.corner is box3.corner)

#print(box.width, box.height, box.corner.x, box.corner.y)

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.width/2
    return (p.x,p.y)


box_center = find_center(box)
grow_rectangle(box,50,180)
#print(box_center)