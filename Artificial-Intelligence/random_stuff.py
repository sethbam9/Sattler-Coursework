class Jug():
    def __init__(self, name, water, capacity):
        self.name = name 
        self.water = water 
        self.capacity = capacity
        
jug1 = Jug("one", 3, 12)
jug2 = Jug("two", 6, 8)
ground = Jug("ground", None, None)

def transfer(giver, receiver):
    if receiver.name == "ground":
        receiver.water = 0
        return
    if receiver.water + giver.water > receiver.capacity:
        given = receiver.capacity - receiver.water
        receiver.water = receiver.capacity
        giver.water -= given
    else:
        receiver.water += giver.water
        giver.water = 0
    print(giver.water, receiver.water)

# transfer(jug1, jug2)


class Object:
    def __init__(self, name, x, y, z, xx, yy, zz):
        self.name = name
        self.x = x 
        self.y = y 
        self.z = z 
        self.xx = xx
        self.yy = yy
        self.zz = zz

    def move(self, x, y):
        self.x += x
        self.y += y

def create_plane(objects, plane):
    for obj in objects:
        for y in range(len(plane)):
            for x in range(len(plane[y])):
                if x in range(obj.x-1, obj.x + obj.xx-1) and y in range(obj.y-1, obj.y + obj.yy-1):
                    plane[y][x] = obj.name
    return plane

def display(plane):
    for i in range(len(plane)):
        print(i+1, plane[i])
    print("\n")

a = Object("A", 1, 3, 2, 3, 2, 2)
b = Object("B", 2, 2, 1, 1, 1, 2)
objects = [a, b]
width = 4
length = 4
height = 4
plane2D = [['o' for x in range(width)] for y in range(height)]
plane3D = [[['o' for x in range(width)] for y in range(length)] for z in range(height)]

# display(create_plane(objects, plane))
# a.move(3, -1)
# b.move(-2, 1)

def create_plane3D(objects, plane):
    for obj in objects:
        for z in range(len(plane)):
            for y in range(len(plane[z])):
                for x in range(len(plane[z][y])):
                    if x in range(obj.x-1, obj.x + obj.xx-1) \
                    and y in range(obj.y-1, obj.y + obj.yy-1) \
                    and z in range(obj.z-1, obj.z + obj.zz-1):
                        plane[z][y][x] = obj.name
    return plane

# display(create_plane3D(objects, plane3D))