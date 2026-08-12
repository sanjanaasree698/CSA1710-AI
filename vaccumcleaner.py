# Python Program for Vacuum Cleaner Problem

# Rooms and their status
rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

# Vacuum starts in Room A
current_room = 'A'

print("Initial State:")
print(rooms)

# Cleaning process
while 'Dirty' in rooms.values():

    if rooms[current_room] == 'Dirty':
        print("\nVacuum is in Room", current_room)
        print("Room", current_room, "is Dirty -> Cleaning")
        rooms[current_room] = 'Clean'

    # Move to the other room
    if current_room == 'A':
        current_room = 'B'
    else:
        current_room = 'A'

print("\nFinal State:")
print(rooms)
print("\nAll rooms are clean.")