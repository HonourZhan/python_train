def index_KMP(S, T, pos):
    NextVal = getNext(T)
    i, j = pos, 1
    while i <= S[0] and j <= T[0]:
        if j == 0 or S[i] == T[j]:  # j==0表示主串当前的S[i]和模式串的T[1]都不匹配，只有将主串和模式串同时后移一位继续匹配；
            # S[i] == T[j]表示当前主串和模式串指向的字符匹配，继续后移查看下一位是否匹配
            i += 1
            j += 1
        else:
            j = NextVal[j]  # 移动T用T的另一个字符和S匹配
    if j > T[0]:
        return i - T[0]
    else:
        return 0
 
 
def getNext(T):
    next1 = [T[0], 0]
    i, j = 1, 0
    while i < T[0]:
        if j == 0 or T[i] == T[j]:  # 初始化next[1]以及找不到任何的Pk'==Pj时next[j+1]=1和计算Pk==Pj时，next[j+1] = next[j] + 1
            i += 1
            j += 1
            next1.append(j)
        else:
            j = next1[j]
    return next1
 
 
def getNextVal(T):
    nextval = [T[0], 0]
    i, j = 1, 0
    while j < T[0]:
        if j == 0 or T[i] == T[j]:
            i += 1
            j += 1
            if T[i] != T[j]:
                nextval.append(j)
            else:
                nextval.append(nextval[j])
        else:
            j = nextval[j]
    return nextval
 
 
 
 
if __name__ == '__main__':
    S = list('acabaabaabcacaabc')
    S.insert(0, len(S))  # S = [6, 'a', 'b', 'b', 'a', 'b', 'a']
    T = list('abaabc')
    T.insert(0, len(T))  # T = [3, 'a', 'b', 'a']
    getNext(T)
    T1 = list('aaaab')
    T1.insert(0, len(T1))
    getNextVal(T1)
    print(index_KMP(S, T, 1))
