length = input("What is the length of the room in meters?")
L = int(length)
width = input("What is the width of the room in meters?")
W = int(width)
height = input("What is the height of the room in meters?")
H = int(height)
Room_Area_m = W * L
Room_Volume_m = W * L * H
Room_Area_mm = Room_Area_m * 1000000
Room_Volume_mm = Room_Volume_m * 1000000000
print ("Room area is {} m²".format(Room_Area_m))
print ("Room volume is {} m³".format(Room_Volume_m))
print ("Room area is {} mm²".format(Room_Area_mm))
print ("Room volume is {} mm³".format(Room_Volume_mm))
if L > W and L > H:
    print ("The dominant dimension of the room is its length")
elif W > H and W > L:
    print ("The dominant dimension of the room is its width")
elif H > W and H > L: 
    print ("The dominant dimension of the room is its height")
elif W == H == L:
    print ("The room is a cube, there is no dominant dimension")
elif W < H:
    print ("The height and length are equal and are the dominant dimensions of the room")
elif W == H:
    print ("The width and height are equal and are the dominant dimensions of the room")
else:
    print ("The width and length are equal and are the dominant dimensions of the room")



    