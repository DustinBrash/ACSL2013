from copy import copy

def input_pos():
    pos = raw_input("Input: ")
    if len(pos) < 4:
        return None
    pos = pos.replace(" ", '')
    pos = pos.split(',')
    pos_white = []
    pos_black = []
    for i in range(int(pos.pop(0))):
        pos_white.append(int(pos.pop(0)))
    for i in range(int(pos.pop(0))):
        pos_black.append(int(pos.pop(0)))

    return pos_white, pos_black

def test_read(filename):
    with open(filename, 'r') as f:
        for line in f:
            if line != '\n':
                pos = copy(line)
                pos = pos.replace(" ", '')
                pos = pos.replace('\n', '')
                test = copy(pos)
                test = test.replace(',', '')
                if not (test.isdigit()):
                    yield 'NONE'
                else:
                    pos = pos.split(',')
                    pos_white = []
                    pos_black = []
                    try:
                        for i in range(int(pos.pop(0))):
                            pos_white.append(int(pos.pop(0)))
                        for i in range(int(pos.pop(0))):
                            pos_black.append(int(pos.pop(0)))

                        yield pos_white, pos_black
                    except IndexError:
                        yield 'NONE'
            else:
                yield 'NONE'
#check surrounding spots of white sones
    #if white continue, if black check if opp is empty, if empty check if next step black
#capture by incrementing steps

def check_x(pos, white, black):
    if pos % 5 == 0:
        check = -1
        #no away
        return check_toward(pos, check, white, black)
    elif (pos - 1) % 5 == 0:
        check = 1
        #no away
        return check_toward(pos, check, white, black)
    elif (pos - 2) % 5 == 0:
        end, step, away =  check_toward(pos, 1 , white, black)
        if end != None:
            return end, step, away
        else:
            end, step, away = check_away(pos, 1, white, black)
            if end != None:
                return end, step, away
    elif (pos + 2) % 5 == 0:
        end, step, away = check_toward(pos, -1, white, black)
        if end != None:
            return end, step, away
        else:
            end, step, away = check_away(pos, -1, white, black)
            if end != None:
                return end, step, away
    else:
        #row check
        for i in (-1, 1):
            end, step, away = check_toward(pos, i, white, black)
            if end != None:
                return end, step, away
            else:
                end, step, away = check_away(pos, i, white, black)
                if end != None:
                    return end, step, away
    return None, None, None
        
def check_y(pos, white, black):
    if pos in range(1, 6):
        check = 5
        #no away
        return check_toward(pos, check, white, black)
    elif pos in range(21, 26):
        check = -5
        #no away
        return check_toward(pos, check, white, black)
    else:
        for i in (-5, 5):
            end, step, away = check_away(pos, i, white, black)
            if end != None:
                return end, step, away
            else:
                end, step, away = check_toward(pos, i, white, black)
                if end != None:
                    return end, step, away
    return None, None, None
        
def check_l(pos, white, black):
    if (pos - 1) % 5 == 0:
        return None, None, None
    elif pos % 5 == 0:
        #no away check
        for i in (4, -6):
            end, step, away = check_toward(pos, i, white, black)
            if end != None:
                return end, step, away
    elif (pos - 2) % 5 == 0:
        for i in (-6, 4):
            end, step, away = check_away(pos, i, white, black)
            if end != None:
                return end, step, away
    elif pos in range(21, 26):
        check = -6
        #no away
        return check_toward(pos, check, white, black)
    elif pos in range(1, 6):
        check = 4
        #no away
        return check_toward(pos, check, white, black)
    else:
        #row check
        for i in (4, -6):
            end, step, away = check_away(pos, i, white, black)
            if end != None:
                return end, step, away
            else:
                end, step, away = check_toward(pos, i, white, black)
                if end != None:
                    return end, step, away
    return None, None, None

def check_r(pos, white, black):
    if pos % 5 == 0:
        return None, None, None
    elif (pos - 1) % 5 == 0:
        #no away check
        for i in (-4, 6):
            end, step, away = check_toward(pos, i, white, black)
            if end != None:
                return end, step, away
    elif (pos + 1) % 5 == 0:
        for i in (6, -4):
            end, step, away = check_away(pos, i, white, black)
            if end != None:
                return end, step, away
    elif pos in range(1, 6):
        check = 6
        #no away
        return check_toward(pos, check, white, black)
    elif pos in range(21, 26):
        check = -4
        #no away
        return check_toward(pos, check, white, black)
    else:
        # row check
        for i in (-4, 6):
            end, step, away = check_toward(pos, i, white, black)
            if end != None:
                return end, step, away
            else:
                end, step, away = check_away(pos, i, white, black)
                if end != None:
                    return end, step, away
    return None, None, None

def check_away(pos, step, white, black):
    if (pos + step) not in black:
        return None, None, None
    elif (pos - step) in (white + black):
        return None, None, None
    else:
        return (pos, step, True)
            
def check_toward(pos, step, white, black):
    if (pos + step) in (black + white):
        return None, None, None
    elif (pos + (2 * step)) not in black:
        return None, None, None
    else:
        return (pos, step, False)

def capture(pos, step, away, white, black, out = []):
    second = copy(out)
    if away:
        if pos + step in black:
            second.append(pos + step)
            return capture((pos + step), step, away, white, black, second)
        else:
            return out
    else:
        if pos + 2 * step in black:
            second.append(pos + 2 * step)
            return capture((pos + step), step, away, white, black, second)
        else:
            return out
    
def axis_check(pos, white, black):
    pos2, step, away = check_x(pos, white, black)
    if pos2 == None:
        pos2, step, away = check_y(pos, white, black)
    return pos2, step, away

def diag_check(pos, white, black):
    pos2, step, away = check_l(pos, white, black)
    if pos2 == None:
        pos2, step, away = check_r(pos, white, black)
    return pos2, step, away

def move(white, black):
    for stone in white:
        pos, step, away = axis_check(stone, white, black)
        if pos != None:
            return capture(pos, step, away, white, black)
        if stone % 2 == 1:
            pos, step, away = diag_check(stone, white, black)
            if pos != None:
                return capture(pos, step, away, white, black)
    return 'NONE'

def main(filename):
    for a in test_read(filename):
        if a == 'NONE':
            print 'NONE'
        else:
            out = move(a[0], a[1])
            if out == 'NONE':
                print 'NONE'
            else:
                print str(sorted(out))[1:-1]

#ladder of process
        #main analyzes file for input lines
        #move checks cardinal and secondary directions
        #axis check checks cardianls, diag check checks secondaries
        
        
    
