# put your code here.
#create function
def word_count(word_file):
    """
    Function takes in a word file as a parameter and prints
    the count of each unique word separated by spaces.
    """   

    #open the file  
    text_file = open(word_file)

    #create a empty dictionary
    word_dictionary = {}

    #iterate for line in file to grab words
    for line in text_file:
        word_list = line.rstrip().split(" ")

        #iterate words in each line into a dictionary
        #add 1 to the value for each word key
        for word in word_list:   
            word_dictionary[word] = word_dictionary.get(word, 0) + 1

    #print the dictionary 
    for word, count in word_dictionary.items():
        print(f'{word}: {count}')   

word_count("twain.txt")