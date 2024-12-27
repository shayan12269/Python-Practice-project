# Practice 32 | Count Occurrences of a Word or Number in a Sentence

# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Prompt the user to enter the word or number to find
find_word = input("Enter the word or number to count: ")
    
# Split the sentence into words, stripping any leading/trailing whitespace
separated_sentence = [word.strip() for word in sentence.split() if word.strip()]
    
# Initialize a counter for occurrences
count_word = 0

# Iterate through each word in the sentence to count occurrences
for word in separated_sentence:
    if word == find_word:
        count_word += 1
    # No action needed for non-matching words

# Display the count of the specified word or number
print(f"The count of '{find_word}' in the sentence is {count_word}")
