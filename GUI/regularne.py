import re

s = "Ala ma kota ! Kot lubi mleko. Nie lubi ryb."

print (s)
print(re.findall(r'[A-Z].*\.', s))