__name__ = 'Formating'
#Written by Dustin Brashear

def seperate_strings(s):
    format_str = None
    value_str = None
    value_str = s.split(',')[-1]
    length = len(value_str) + 1
    value_str = value_str.lstrip()
    format_str = s[:0 - length]
    return format_str, value_str

def comma(f, v):    
    out = star3(f, v)
    if '*' in out:
        dif = v
        out = out[0: -1 * len(dif)] + insert_comma(dif)
    else:
        dif = v[:len(out)]
        out = insert_comma(dif)        
    return out

def insert_comma(dif):
    num_com = (len(dif) - 1) / 3
    start = len(dif) % 3
    ret = ''
    fin = ''
    for n in range(len(dif)):
        ret += dif[-n - 1]
        if (n + 1) % 3 == 0:
            ret += ','
    if ret[-1] == ',':
        ret = ret[:-1]
    for n in range(len(ret)):
        fin += ret[-1 * (n + 1)]
    return fin

def exponent(f, v):
    out = ''
    power = str(len(v) - 1)
    if len(f) == 2:
        num = int(v)
        num = round(num, 1 - len(v))
        out = str(num)[0] + '.0E' + power
    else:
        form = f[:-2]
        power = str(len(v) - 1)
        num = rounding(form, v[1:])
        out = v[0] + num + 'E' + power
    return out

def money_filled(f, v):    
    b = decimal(f, v)
    a = b.split('.')[0]
    b = '.' + b.split('.')[1]
    check = False
    if '*' in a:
        for n in range(len(a)):
            index = -1 * (n + 1)
            if (not check) and (a[index] == '*'):
                check = True
                a = a[:index + 1] + '$' + a[index + 1:]        
    else:
        a = '$' + a
    return a + b
def money(f, v):
    out = decimal(f, v)
    while out[0] == '*':
        out = out[1:]
    return '$' + out

def decimal(f, v):
    l = f.split('.')
    l2 = v.split('.')
    b = rounding(l[1], l2[1])
    a = star3(l[0], l2[0])
    return a + b

def rounding(f, v):
    v_temp = v
    dif = len(f) - len(v)
    if dif > 0:
        for n in range(dif):
            v_temp += '0'
        v_temp = '.' + v_temp
    else:       
        num = str(int(round(int(v_temp), dif)))
        v_temp = '.' + num[:len(f)]           
    return v_temp
    

def star3(f, v):
    out = ''
    count = f.count('&')
    hold = ''
    dif = count - len(v)
    if dif > 0:
        for n in range(dif):
            out += '*'
        out += v[:count - dif]
    elif dif < 0:
        out = v[:dif]
    else:
        out = v
    return out

num = 0
while (num < 5):
    out = 'Something went wrong. Very wrong.'
    input_string = raw_input('Enter format string and value: ')
    form, val = seperate_strings(input_string)
    if ',' in form:
        out =  comma(form, val)
    elif form[-1] == 'E':
        out =  exponent(form, val)
    elif '.' in form:
        if form[:2] == '*$':
            out = money_filled(form, val)
        elif form[0] == '$':
            out = money(form, val)
        else:
            out = decimal(form, val)
    else:
        out = star3(form, val)
    print out
    num += 1
