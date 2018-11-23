import pprint
people = {}
number = 0
for number in range(1, 4):
    person_name = input("What's his name?")
    person_gender = input("Whaat's gender?")
    person_occupation = input("What's your job?")
    person_star = input("Where are you form?")
    people[person_name]= { 'Name' : person_name, 'Gender' : person_gender, 'Occupation' : person_occupation, 'Home Planet' : person_star }
    print(people[person_name])
    number += 1
else:
    pprint.pprint(people)
    

    
