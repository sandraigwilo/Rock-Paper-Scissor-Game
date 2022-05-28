# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    fp = open(filename, "r")
    text = fp.read()
    fp.close() 
    return text



def count_words():
    text = read_file_content("Reading-Text-Files\story.txt")
    # [assignment] Add your code here
    substr = ("as", "would")
    return {i: text.count(i) for i in substr}

print(count_words())    


