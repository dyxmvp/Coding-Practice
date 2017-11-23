# Solution 1:
def presses(phrase):
    #your code here
    keys = [[chr(i), chr(i+1), chr(i+2)] for i in range(97, 112, 3)]
    keys2 = [chr(i) for i in range(112, 123)]
    keys2 = [keys2[:4], keys2[4:7], keys2[7:]]
    keys.extend(keys2)
    for n, k in enumerate(keys):
        k.append(str(n + 2))
    keys.extend([[' ', '0'], ['1'], ['#'], ['*']])
    count = 0
    for p in phrase.lower():
        for k in keys:
            if p in k:
                count += k.index(p) + 1
                break
    return count

# Solution 2:
BUTTONS = [ '1',   'abc2',  'def3',
          'ghi4',  'jkl5',  'mno6',
          'pqrs7', 'tuv8', 'wxyz9',
            '*',   ' 0',    '#'   ]
def presses(phrase):
    return sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button)