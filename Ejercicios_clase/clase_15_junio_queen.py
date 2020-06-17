

string = """The merry old queen of Katoren has died
and there’s no heir to the throne. Six sour ministers rule the land
and claim that they’re looking for a new queen,
but nothing happens – for seventeen years. 
Then suddenly there’s a girl standing at the door of the royal
palace who was born on the night the queen died.

This girl, <name> , has firmly resolved to become the new queen of Katoren and
she asks the six ministers what she must do in order to be considered for 
the role. The ministers, afraid of losing their splendid position at court, give the
girl seven almost impossible tasks, which can be brought to a successful
conclusion only by one who possesses royal attributes such as wisdom,
courage and self-sacrifice. The six ministers are convinced that <name> will fall
at the first hurdle, but she turns out to have an amazing amount of
persistence and ingenuity.
"""


filename = 'queen_of_Katoren.txt'

def change_name(list_line, name="Lisa"):
    """
    Function that changes name in list
    """
    
    k = 0 # índice para recorrer line
    
    for t in list_line:
        if t == "<name>":
            list_line[k] = name
        k += 1
    return list_line        

with open(filename, 'w+') as f:

    for line in string.splitlines():
        
        if '<name>' in line:
            l = line.split()
            l = change_name(l)
            l = ' '.join(l)
            line = l
            print(line)
            
        f.write(line + '\n')
