n = int(input())
word_list=[' ' for _ in range(n)]

for i in range(n):
    word_list[i] = input()

word_list= set(word_list)
sorted_word_list = sorted(word_list) #sort alphabetically
sorted_word_list = sorted(sorted_word_list,key=len) #sort in length
for word in sorted_word_list :
    print(word)