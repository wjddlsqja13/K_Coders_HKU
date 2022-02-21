def isBalanced(s):
    if len(s)%2 != 0:
        return 'NO'
      
    result = []
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '[' or s[i] == '{':
            result.append(s[i])
        else:
            if not result:
                return 'NO'
            elif s[i] == ')' and result[-1] == '(':
                result.pop()
            elif s[i] == ']' and result[-1] == '[':
                result.pop()
            elif s[i] == '}' and result[-1] == '{':
                result.pop()
                
    if not result:
        return 'YES'
    else:
        return 'NO'
