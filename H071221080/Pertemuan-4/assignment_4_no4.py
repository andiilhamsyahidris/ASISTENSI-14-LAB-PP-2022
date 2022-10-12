# Program Mengatur Pergerakan Robot Menggunakan Function

def robot():
    x = 0
    y = 0
    while True:
        s = input().upper()
        if s == 'END':
            print('Robot has been stopped')
            break
        elif s == 'RESET':
            x -= x
            y -= y
            print(f'x{x} y{y}')
        else:
            s = list(s)
            for i in s:
                if i == 'R':
                    print(f'x{x} y{y}')
                    x += 1
                    print(f'x{x} y{y}')
                elif i == 'L':
                    print(f'x{x} y{y}')
                    x -= 1
                    print(f'x{x} y{y}')
                elif i == 'U':
                    print(f'x{x} y{y}')
                    y += 1
                    print(f'x{x} y{y}')
                elif i == 'D':
                    print(f'x{x} y{y}')
                    y -= 1
                    print(f'x{x} y{y}')
                else:
                    continue

robot()