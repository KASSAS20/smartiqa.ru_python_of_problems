s = 'пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'

# 1
s = s.capitalize()
# 2
index = s.find('сопровождать')
# 3
s = s.replace('сопровождать', 'поддерживать')
# 4
l = s.split(',')
new_s = ','.join(l)