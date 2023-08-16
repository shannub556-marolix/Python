s='python is easy'
new_list=[]
for word in s.split():
    if word=='is':
        new_list.append('is not')
    else:
        new_list.append(word)
print((' ').join(new_list))