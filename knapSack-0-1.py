def knapSack(W, w, v, N):
  for i in range(N):
    for j in range(W+1):
      cap = j
      cw = w[i]
      cv = v[i]
      if i == 0:
        if cw <= cap:
          dp[i][j] = cv
      else:
        if cw <= cap:
          dp[i][j] = max(dp[i-1][j], dp[i-1][j-cw]+cv)
        else:
          dp[i][j] = dp[i-1][j]
  return dp[N-1][W]

W = 10
w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
N = len(w)
dp = [[0 for i in range(W+1)] for j in range(N)]
print(knapSack(W, w, v, N))
