def generateParenthesis(n):
    r_result = []
    parenti = '()'
    
    m_s = parenti * n
    r_result.append(m_s)
    
    for i in range(1, n):
        #LEFT
        l_par = '(' * i
        r_par = ')' * i
        add_par = parenti * (n-i)

        
        m = l_par + add_par + r_par
        r_result.append(m)

        if i > 1:
            l = l_par + r_par + add_par
            r = add_par + l_par + r_par
            r_result.append(l)
            r_result.append(r)

    return r_result


# print(generateParenthesis(2))
# print(generateParenthesis(3))
print(generateParenthesis(4))
# print(generateParenthesis(5))
