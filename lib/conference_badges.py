def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    return [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names] 

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    
    for room_assignment in room_assignments:
        print(room_assignment)


# arr = batch_badge_creator(["Arel", "Carol"])
# print(arr)


arr = assign_rooms(["Arel", "Carol"])
print(arr)

    