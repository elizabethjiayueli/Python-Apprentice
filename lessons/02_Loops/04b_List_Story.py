"""
Use the words in the list to create a story. 

Use indexing to get words from the list, then 
append them to the story

"""

words = ['Once', '👦', 'upon', '🐕', 'park', 'met', 'with', 'a', 'the', 
    'time', 'to', 'who', '🐈', '👧', 'and', 'went', 'had', 'play', '⚽.', 'they']
indices = [0,2,7,9,1,5,6,13,11,16,7,12,14,19,15,10,8,4,10,17,18]
story = []
for i in indices:
    words[i]
    story.append(words[i])
# Create a story using the words in the list

# Display the story to the user
print(' '.join(story))