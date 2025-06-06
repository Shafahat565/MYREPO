# ----------------------------------
# Task 3: Rule-Based Expert Advisor
# ----------------------------------
def advisor(weather, time_available, deadlines, energy):
    rules = [
        (weather == 'sunny' and time_available > 2 and energy >= 6, 'Go to sports club'),
        (weather == 'rainy' and deadlines, 'Study indoors today'),
        (weather == 'cold' and energy < 3, 'Take rest today'),
        (time_available < 1, 'Do quick review of syllabus'),
        (not deadlines and energy >= 5, 'Relax or play'),
        (deadlines and energy >= 7, 'Focus on assignments and prepare quizzes'),
        (energy < 2, 'Take nap'),
        (weather == 'sunny' and not deadlines and time_available > 1, 'Attend seminar and learn something'),
        (weather == 'rainy' and energy >= 6, 'Work on project at home and gain skills'),
        (energy >= 4 and time_available >= 2, 'Group study with friends etc')
    ]
    for condition, action in rules:
        if condition:
            return action
    return 'No advice found'



print("\n🧠 Task 3: Expert Advisor")
advice = advisor(weather='sunny', time_available=2, deadlines=False, energy=7)
print("Advice:", advice)
