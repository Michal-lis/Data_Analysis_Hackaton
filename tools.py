def parser_krzys(a):
    l = []
    for pair in a[0].split('(((')[1].split(')))')[0].split(','):
        a = float(pair.split(' ')[0])
        b = float(pair.split(' ')[1])
        l.append((a, b))
    return l
