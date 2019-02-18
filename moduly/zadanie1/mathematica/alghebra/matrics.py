def add_metrices(m1, m2):
    m3 = []
    for i in range (len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2 [i][j])
        m3.append(row)
    return m3


def sub_metrices(m1, m2):
    m3 = []
    for i in range (len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] - m2 [i][j])
        m3.append(row)
    return m3