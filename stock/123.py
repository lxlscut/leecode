import numpy as np

def best_profit(prices,k):
    """
    :param prices: price为股票的价钱
    :param k: k为买卖的次数
    :return:
    """
    length = len(prices)
    dp = np.zeros((length,k+1,2),dtype=np.float)
    for i in range(length):
        for j in range(k,0,-1):
            if (i-1) == -1:
                dp[i,j,0] = 0
                dp[i,j,1] = -prices[i]
                continue
            # 卖了股票手里就有钱了,第三位为0表示无股票
            dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
            # 新买进股票之前必须卖出去，第三位为1表示有股票
            dp[i][j][1] = max(dp[i-1][j][1],dp[i-2][j-1][0]-prices[i])
    return dp[length-1][k][0]


if __name__ == '__main__':
    prices =  [7,1,5,3,6,4]
    res = best_profit(prices,1)
    print(res)