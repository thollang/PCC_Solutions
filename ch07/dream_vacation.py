name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

resoponse={}

while True:
    name = input(name_prompt)
    place = input(place_prompt)

    resoponse[name]=place

    repeat=input(continue_prompt)
    if repeat == 'no':
        break

print("---------------------------")
for name,place in resoponse.items():
    print(name.title() + " would like to visit " + place.title() + ".")
