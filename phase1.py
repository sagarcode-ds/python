# day 1
# Write a script that reads a .txt file, counts how often each word appears, and writes the top 10 most frequent words to a new .txt file.
# manually created input.txt
# with open('input.txt','r') as f:
#     content=f.read().lower()
# words=content.split()
#     # print(words)
# word_frequency={}
# for word in words:
#     word_frequency[word]=word_frequency.get(word,0)+1
# # print(word_frequency)
# sorted_words = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
# with open('new.txt','w') as f:
#     f.write('top 10 most frequent words')
#     for word in sorted_words[:10]:
#         f.write(f"{word[0]}:{word[1]}"+"\n\n")
