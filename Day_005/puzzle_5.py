
# 12-05-2020

# https://adventofcode.com/2020/day/5

import pandas as pd 

## apply function to frame 
raw=[]
with open('input.txt','r') as f:
    for line in f:
        for i in line.split():
            raw.append(i)

seats = pd.DataFrame(raw, columns={"tik_info"})

#0: 0123|4567
#1: 0123|4567
#2: 0123|4567
#...
#127: 0123|4567

## FIND ROWS FUNCTION 
def find_row(tickets = pd.DataFrame()):
    # static variables (i) 
    row_numbers=[]
    mn = 0
    mx = tickets.size
    ticket_row = range(0,7)
    for i in range(mn,mx):
        # static variable (j)
        row_num = 0
        low = 0 
        high = 127
        for j in ticket_row:
            mid = round(high/2)
            # if last i set to row_num 
            if (j == max(ticket_row)):
                #keep high
                if tickets[i][j] == "F": row_num = low
                # keep low 
                elif tickets[i][j] == "B": row_num = high
                else: print("type 1 error")
            else:
                #keep range < mid
                if tickets[i][j] == "F": high = mid
                #keep range > mid
                elif tickets[i][j] == "B": low = mid
                else: print("type 2 error")
        row_numbers.append(row_num)
    return(row_numbers)

find_row(tickets = seats["tik_info"])


seats["tik_info"][0][7]

ticket_row = range(0,8)
