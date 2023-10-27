#INTRO TO IT 2nd COURSE
from itertools import product
s = 'ЕКМОПРТЬ'
combs = product(s, repeat=5)
c = 0
for comb in combs:
    c += 1
    st = ''.join(comb)
    print(c, st)
    if st[0] != 'Е' and st.count('К') == 2 and c % 2 == 0:
        print(c, st)
        break