class LongestSolution:
    def __init__(self,strs):
        self.strs = strs



    def get_perfix(self):
        if not self.strs:
            return
        result = []
        length = len(self.strs)
        for j in range(len(self.strs[0])):
            # print(self.strs[0][j])
            for string in self.strs[1:]:
                if j>len(string) or self.strs[0][j] != string[j]:
                    return self.strs[0][:j]
        return self.strs[0]

if __name__ == '__main__':
    a = ["aac", "aab", "aaa"]
    solution = LongestSolution(a)
    a = solution.get_perfix()
    print(a)