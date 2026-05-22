p = "the sun rose over the quiet hill. the hill was covered in soft green grass.a gentle wind moved through the grass, and the wind carried the smell of rain.rain fell softly on the hill, and the rain made the grass grow.the grass swayed with the wind as the sun warmed the hill again."
words=p.replace('.',' ').split()
# print(words)
d={}
for word in words:
    d[word] = d.get(word, 0) + 1
print(d)
sort=sorted(list(d.items())[1])
    

    