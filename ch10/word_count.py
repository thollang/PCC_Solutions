filename = 'the_life_of_charlemagne.txt'

try:
    with open(filename) as f_object:
        contents = f_object.read()
except FileNotFoundError:
    msg = "Sorry, the file {} does not exist".format(filename)
else:
    words = contents.split()
    num_words = len(words)
    print("the file {} has about {} words.".format(filename,str(num_words)))
