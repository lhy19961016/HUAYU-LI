def word_count_in_str(string, keyword):
    return len(string.split(keyword))-1


s = input('Введите строку символов:')
max_time=0
cur_time=0
i=0
temp=s[i]
max_time=word_count_in_str(s,temp)
i=i+1

while i < len(s):
    temp=s[i]
    cur_time=word_count_in_str(s,temp)
    if cur_time > max_time:
        max_time = cur_time
    i=i+1
    
print('максимальное количество символов в строке:',max_time)
