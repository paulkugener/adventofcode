#! python3

from copy import deepcopy as copy

m = []
steps = 100
part2 = True

with open("./2015/18input", "r") as f:
    for line in f:
        line = line.rstrip()
        list1 = []
        list1[:0] = line
        m.append(list1)

if part2:
    m[0][0] = '#'
    m[0][99] = '#'
    m[99][0] = '#'
    m[99][99] = '#'

for _ in range(steps):
    m_helper = copy(m)
    for j in range(0, 100):
        for i in range(0, 100):

            # get neighbors' state
            neighbors = []
            for jj in range(j-1, j+2):
                for ii in range(i-1, i+2):
                    if jj < 0 or jj > 99 or ii < 0 or ii > 99:
                        neighbors.append('.') # out of bounds is OFF
                    elif jj == j and ii == i:
                        continue
                    else:
                        neighbors.append(m[jj][ii])
            on = neighbors.count('#')
            # off = neighbors.count('.')
            # assert(on + off == 8)

            # if light is ON
            if m[j][i] == '#':
                if on == 2 or on == 3:
                    m_helper[j][i] = '#'
                else:
                    m_helper[j][i] = '.'

            # if light is OFF
            elif m[j][i] == '.':
                if on == 3:
                    m_helper[j][i] = '#'
                else:
                    m_helper[j][i] = '.'
    if part2:
        m_helper[0][0] = '#'
        m_helper[0][99] = '#'
        m_helper[99][0] = '#'
        m_helper[99][99] = '#'
    m = m_helper

result = 0
for j in m:
    result += j.count('#')
print(result)
