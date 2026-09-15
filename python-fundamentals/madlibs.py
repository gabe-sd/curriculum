

ask_user = ["noun", "noun", "verb ending in ing", 
            "verb ending in ing","adverb", "vehicle", "noun"]

chosen = []

for i in ask_user:
  pick = input("Enter a(n) " + i)
  chosen.append(pick)


story = '''
Yesterday my \033[4m\033[1m%s\033[0m and I went to big bear. There was so much snow!
My sister and I had a \033[4m\033[1m%s\033[0m fight.  And while we where \033[4m\033[1m%s\033[0m,
a big brown bear came \033[4m\033[1m%s\033[0m towards us. It was so \033[4m\033[1m%s\033[0m! Luckly,
we hopped in our \033[4m\033[1m%s\033[0m right away and escaped the bear. When we got
home, we saw on the news that the bear got ranover by a \033[4m\033[1m%s\033[0m.
''' % tuple(chosen)

print(story)


