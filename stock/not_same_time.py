import numpy as np

def best_profit(prices):
    length = len(prices)
    dp = np.zeros((length,2),dtype=np.float)

    for i in range(length):
        if (i-1) == -1:
            dp[i,0] = 0
            dp[i,1] = -prices[i]
            continue
        # 卖了股票手里就有钱了
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
        # 新买进股票之前必须卖出去
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i])
    print(dp)
    return dp[length-1][0]


if __name__ == '__main__':
    prices =  [7,1,5,3,6,4]
    res = best_profit(prices)
    print(res)