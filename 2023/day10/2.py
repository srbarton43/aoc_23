input = "sample-4.txt"
input = "input.txt"

import numpy as np
import pprint

def main():
    grid = []
    with open(input, "r") as f:
        for line in f:
            line = line.strip()
            grid.append([c for c in line])

    grid = np.asarray(grid)
    print(grid)
    points = getStart(grid)
    start = points[0]
    points = traverse(grid, start, points)
    alg(points)

    

def getStart(grid):
    for r, row in enumerate(grid):
        for c, sq in enumerate(row):
            if sq == 'S':
                start = (r, c)
                break
        else:
            continue
        break

    print(start)
    start1 = start2 = None
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    r, c = start
    sR, sC = start
    points = [start]
    for dr, dc in dirs:
        print(grid[r+dr, c+dc])
        if dr is 0:
            match dc:
                case 1: # right
                    print("foo")
                    if grid[(r, c+dc)] in ['7', 'J', '-']:
                        if not start1:
                            start1 = (r, c+dc)
                        else:
                            start2 = (r, c+dc)
                            break
                case -1:
                    if grid[(r, c+dc)] in ['F', 'L', '-']:
                        if not start1:
                            start1 = (r, c+dc)
                        else:
                            start2 = (r, c+dc)
                            break
        else:
            match dr:
                case 1: # down
                    if grid[r+dr, c] in ['L', 'J', '|']:
                        if not start1:
                            start1 = (r+dr, c)
                        else:
                            start2 = (r+dr, c)
                            break
                case -1:
                    if grid[r+dr, c] in ['F', '7', '|']:
                        if not start1:
                            start1 = (r+dr, c)
                        else:
                            start2 = (r+dr, c)
                            break
              
    print(start1, start2)
    points = [start, start2]
    print(points)
    return points

def traverse(grid, start, points):
    while True:
        prev, cur = points[-2:]

        next = getNext(grid, cur, prev)
        if next == start: break
        points.append(next)

    return points

def alg(points):
    sum = 0
    pLen = len(points)
    for i in range(pLen):
        n = (i+1) % pLen
        sum += points[i][1] * points[n][0] - points[i][0] * points[n][1]
    
    count = round((sum/2) - pLen/2 + 1)

    print(f'total: {count}')

def getNext(grid, cur, prev):
    pr, pc = prev
    cr, cc = cur
    print(grid[cur])
    sq = grid[cur]
    grid[cur] = '*'
    match sq:
        case '|':
            if pr > cr:
                return (cr-1, cc)
            else:
                return (cr+1, cc)
        case '-':
            if pc > cc:
                return (cr, cc-1)
            else:
                return (cr, cc+1)
        case 'F':
            if pc-1 == cc: # to right
                return (cr+1, cc)
            else:
                return(cr, cc+1)
        case '7':
            if pc+1 == cc:
                return (cr+1, cc)
            else:
                return (cr, cc-1)
        case 'J':
            if pr+1 == cr:
                return (cr, cc-1)
            else:
                return (cr-1, cc)
        case 'L':
            if pr+1 == cr:
                return (cr, cc+1)
            else:
                return (cr-1, cc)
                
    return None

def fill(grid, loc):
    filled = 0
    checked = set()
    toCheck = [loc]
    while toCheck:
        cur = toCheck.pop()
        if cur in checked:
            continue
        else:
            checked.add(cur)
        print(len(toCheck))
        r, c = cur
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
            continue
        if grid[cur] in ['*', 'S', '0']:
            continue
        print(cur)
        grid[cur] = '0'
        toCheck.append((r-1, c))
        toCheck.append((r+1, c))
        toCheck.append((r, c+1))
        toCheck.append((r, c-1))
        filled += 1
    return filled
        
def fill_rec(grid, loc):
    r, c = loc
    # base case:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
        return 0
    if grid[loc] in ['*', '0', 'S']:
        return 0
    grid[loc] = '0'
    return 1 + fill(grid, (r, c+1)) + fill(grid, (r, c-1)) + fill(grid, (r+1, c)) + fill(grid, (r-1, c)) 

def fill_grid_inside():
    # fill stuff inside 
    prev = start
    cur = start1
    filled1 = 0
    grid1 = grid.copy()
    while cur != start:
        cr, cc = cur
        pr, pc = prev
        if cr == pr:
            if cc > pc:
                filled1 += fill(grid, (cr+1, cc))
            else:
                filled1 += fill(grid, (cr-1, cc))
        else:
            if cr < pr:
                filled1 += fill(grid, (cr, cc+1))
            else:
                filled1 += fill(grid, (cr, cc-1))
                
        temp = getNext(old, cur, prev)
        prev = cur
        cur = temp

    print(start2)
    prev = start
    cur = start2
    filled2 = 0
    while cur != start:
        cr, cc = cur
        pr, pc = prev
        if cr == pr:
            if cc > pc:
                filled2 += fill(grid1, (cr+1, cc))
            else:
                filled2 += fill(grid1, (cr-1, cc))
        else:
            if cr < pr:
                filled2 += fill(grid1, (cr, cc+1))
            else:
                filled2 += fill(grid1, (cr, cc-1))
                
        temp = getNext(old1, cur, prev)
        prev = cur
        cur = temp


if __name__ == "__main__":
    main()

# potential ans: 415
