def luckBalance(k, contests):
    # Write your code here
    contests.sort(reverse=True)
    score = 0
    count = 0
    for i in contests:
        if i[1] == 0:
            score += i[0]
        else:
            if count < k:
                score += i[0]
                count += 1
            else:
                score -= i[0]
    return score
