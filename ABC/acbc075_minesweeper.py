H,W=list(map(int,input().split()))
data=[]
around='.'*(W+2)
data.append(around)
for i in range(H):
    temp='.'+input()+'.'
    data.append(temp)
data.append(around)


for i in range(1,H+1):
    mine_line=[]
    for j in range(1,W+1):
        mine_num=0
        if data[i][j]=='#':
            mine_num='#'
            mine_line.append(mine_num)
            pass
        else:
            if data[i-1][j-1]=='#':
                mine_num+=1
            if data[i-1][j]=='#':
                mine_num+=1
            if data[i-1][j+1]=='#':
                mine_num+=1
            if data[i][j-1]=='#':
                mine_num+=1
            if data[i][j+1]=='#':
                mine_num+=1
            if data[i+1][j-1]=='#':
                mine_num+=1
            if data[i+1][j]=='#':
                mine_num+=1
            if data[i+1][j+1]=='#':
                mine_num+=1
            mine_line.append(str(mine_num))
    rslt=''.join(mine_line)
    print(rslt)
