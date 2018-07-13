i = 1
print('  |  1   2   3   4   5   6   7   8   9')
print('--+-----------------------------------')
while i < 10:
        print(' {}|'.format(i), end='')
        j = 1
        while j < 10:
                print("%3d" % (i * j), end =" ")
                j = j + 1
        print()
        i = i + 1
