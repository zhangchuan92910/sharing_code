def solution(dimensions, your_position, guard_position, distance):
    from collections import deque
    width,height = dimensions
    your_position = (your_position[0],your_position[1])
    guard_position = (guard_position[0],guard_position[1])
    def flip(block,direction):
        x,y,me,enemy = block
        if direction == 'up':
            nx = x
            ny = y+height
            nme = (me[0],height-me[1])
            nenemy = (enemy[0],height-enemy[1])
        elif direction == 'down':
            nx = x
            ny = y-height
            nme = (me[0],height-me[1])
            nenemy = (enemy[0],height-enemy[1])
        elif direction == 'left':
            nx = x-width
            ny = y
            nme = (width-me[0],me[1])
            nenemy = (width-enemy[0],enemy[1])
        elif direction == 'right':
            nx = x+width
            ny = y
            nme = (width-me[0],me[1])
            nenemy = (width-enemy[0],enemy[1])
        return (nx,ny,nme,nenemy)
    
    def v_dist(v):
        x,y=v
        return x**2+y**2<=distance**2
    
    def gcd(a,b):
        while a%b:
            a = a%b
            a,b = b,a
        return b if b>0 else -b
    def fraction(f):
        if f[1]==0:
            return (1,0) if f[0]>0 else (-1,0)
        elif f[0]==0:
            return (0,1) if f[1]>0 else (0,-1)
        i = gcd(f[0],f[1])
        return (f[0]/i,f[1]/i)
        
        
    queue = deque([(0,0,your_position,guard_position)])
    res = 0
    visited = set(queue)
    forbid = set()
    while queue:
        s = len(queue)
        for _ in range(s):
            block = queue.popleft()
            x,y,me,e = block
            hit_me = [me[0]+x-your_position[0],me[1]+y-your_position[1]]
            hit_e = [e[0]+x-your_position[0],e[1]+y-your_position[1]]
            if v_dist(hit_me):
                forbid.add(fraction(hit_me))
            if v_dist(hit_e):
                hit_e = fraction(hit_e)
                if hit_e not in forbid:
                    forbid.add(hit_e)
                    res+=1
                for direction in ['up','down','left','right']:
                    temp = flip(block,direction)
                    if temp not in visited:
                        visited.add(temp)
                        queue.append(temp)
    return res

print(solution([3,2], [1,1], [2,1], 4))
print(solution([300,275], [150,150], [185,100], 500))
