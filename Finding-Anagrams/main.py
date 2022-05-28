# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    for substr in str1:
        if substr in str2:
            continue
        else:
            return False
    return True if str1 else None 

print(find_anagram("below", "elbow"))
print(find_anagram("hello", "check"))           


