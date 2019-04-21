favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']

for coder in coders:
    if coder in favorite_languages.keys():
        print(coder+" : Thanks for take the polling")
    else:
        print(coder+" : Please thake our poll")
