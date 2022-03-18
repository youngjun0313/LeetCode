from collections import deque
def solution(n, edge):
    adjs=[]
    for _ in range(n):
        adjs.append([])
    for e in edge:
        adjs[e[0]-1].append(e[1]-1)
        adjs[e[1]-1].append(e[0]-1)
    visited=[False]*n
    distances=[0]*n
    Q=deque()
    Q.append(0)
    md=0
    ans=0
    while(len(Q)>0):
        node = Q.popleft()
        if(not visited[node]):
            visited[node]=True
            for i in adjs[node]:
                print(i)
                if(not visited[i] and distances[i]==0):
                    Q.append(i)
                    distances[i]=distances[node]+1
                    if(md<distances[i]):
                        ans=1
                        md=distances[i]
                    elif(md==distances[i]):
                        ans+=1
    return ans
        
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))