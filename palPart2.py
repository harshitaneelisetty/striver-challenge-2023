#https://www.codingninjas.com/codestudio/problems/palindrome-partitioning-ll_8230732?challengeSlug=striver-sde-challenge

def palindromePartitioning(string):
    n = len(string)

    cuts = [0 for _ in range(n)]
    is_palindrome = [[True for _ in range(n)] for _ in range(n)]

    for length in range(2, n+1):
        for i in range(0, n-length+1):
            j = i + length - 1

            if length == 2:
                is_palindrome[i][j] = (string[i] == string[j])
            else:
                is_palindrome[i][j] = (string[i] == string[j]) and is_palindrome[i+1][j-1]

    for i in range(0, n):
        if is_palindrome[0][i] == True:
            cuts[i] = 0
        else:
            cuts[i] = sys.maxsize
            for j in range(0, i):
                if is_palindrome[j + 1][i] == True and 1 + cuts[j] < cuts[i]:
                    cuts[i] = 1 + cuts[j]

    return cuts[n-1]
