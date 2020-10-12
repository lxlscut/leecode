class Solution:
    def __init__(self):
        pass


    def generate(self,n):
        if n == 0:
            return []
        result = []
        if n>0:
            self.help(n,n,'',result)
        return result

    def help(self,l,r,item,result):
        if r<l:
            return
        if l ==0 and r ==0:
            result.append(item)
        if l>0:
            self.help(l-1,r,item+'(',result)
        if r>0:
            self.help(l,r-1,item+')',result)


if __name__ == '__main__':
    a = Solution()
    b = a.generate(3)
    print(b)