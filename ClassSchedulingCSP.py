from itertools import product

# ----------------------------------
# Task 2: Class Scheduling (CSP)
# ----------------------------------
subjects = ['Math', 'Physics', 'Chemistry', 'Programming', 'English']
rooms = ['RoomA', 'RoomB', 'Lab']
time_slots = ['9AM', '11AM', '2PM']

special_requirements = {'Programming': 'Lab'}
schedule = {}

def is_valid(subject, room, time):
    for s, (r, t) in schedule.items():
        if r == room and t == time:
            return False  # Room already occupied at that time
        if s == subject and t == time:
            return False  # Subject already scheduled at that time
    if subject in special_requirements and room != special_requirements[subject]:
        return False  # Programming must be in Lab
    return True

def solve_schedule(index):
    if index == len(subjects):
        return True
    subject = subjects[index]
    for room, time in product(rooms, time_slots):
        if is_valid(subject, room, time):
            schedule[subject] = (room, time)
            if solve_schedule(index + 1):
                return True
            del schedule[subject]
    return False

# Output
print("\n📅 Task 2: Class Schedule")
if solve_schedule(0):
    for subject in subjects:
        room, time = schedule[subject]
        print(f"{subject:12} ➤ Room: {room}, Time: {time}")
else:
    print("No valid schedule found.")