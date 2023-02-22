import string


# Define a function to read the dictionary and create a hash table
def create_hash_table():
    # Open the words.txt file and read it into a list
    with open('words.txt', 'r') as f:
        words = f.read().split()

    # Remove words with non-lowercase letters
    words = [word for word in words if all(letter in string.ascii_lowercase for letter in word)]

    # Create a hash table to store the sorted version of each word
    hash_table = {}

    # Iterate over each word in the dictionary and sort its letters to create a key
    for word in words:
        key = ''.join(sorted(word))

        # Add the original word to the hash table using the key as the key
        if key in hash_table:
            hash_table[key].append(word)
        else:
            hash_table[key] = [word]

    return hash_table


# Define a function to find anagrams for a given word
def find_anagrams(word, hash_table):
    # Sort the letters of the word to create a key
    key = ''.join(sorted(word))

    # Check if the key is in the hash table
    if key in hash_table:
        # Return the number of anagrams and the list of anagrams
        anagrams = hash_table[key]
        return len(anagrams), ' '.join(anagrams)
    else:
        return 0, ''


# Call the create_hash_table function to create the hash table
hash_table = create_hash_table()

# Call the find_anagrams function for each word in the input and print the output
with open('example_input.txt', 'r') as f:
    for line in f:
        word = line.strip().lower()
        count, anagrams = find_anagrams(word, hash_table)
        print(word, count, anagrams)
