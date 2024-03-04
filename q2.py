

def question_2(m): # fib

    def dfs(n):
        if n <= 1:
            return n
        return dfs(n-1) + dfs(n-2)

    p = 1
    while not dfs(p) >= m:
        p+=1
    return dfs(p) == m # True or False


print(question_2(35))