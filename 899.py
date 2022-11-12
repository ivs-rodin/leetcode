###
# Explanation of the solution:
# 1. Let k == 1:
#     There is no other ways to make lexicographically smallest string except
#     making len(s) swaps s[0] to the end of string and find lexicographically
#     smallest string rotation
# 2. Let k > 1:
    # 2.a: Any i j elements of s can be swapped (see swap() function below)
    # 2.b: With swap function sort of sorting can be implemented (for example BubbleSort) 
    # 2.c: So the result of function orderlyQueue is sorted s

    # def swap0End(self, s, n):
    #     """Swaps n times first element of s to the end

    #     Note that n times swap first element to the end is equivalent to
    #     [s' s''] -> [s'' s']
    #     """
    #     print(f"swap0End {n}\n\t{s} -> \n\t{s[n:]+s[:n]}")
    #     return s[n:]+s[:n]

    # def swap1End(self, s, n):
    #     """Swaps n times second element of s to the end

    #     Note that n times swap second element to the end is equivalent to
    #     [s_0 s' s''] -> [s_0 s'' s']
    #     """
    #     print(f"swap1End {n}\n\t{s} -> \n\t{[s[0]]+s[n+1:]+s[1:n+1]}")
    #     return [s[0]]+s[n+1:]+s[1:n+1]

    # def swap01(self, s):
    #     """Swaps first and second element of s

    #     Note that first and second element swap is equivalent to
    #     swap0End(s, 1)
    #     swap1End(s, len(s)-2)
    #     """
    #     print(f"swap01\n\t{s} -> \n\t{[s[1]]+[s[0]]+s[2:]}")
    #     return [s[1]]+[s[0]]+s[2:]

    # def swap(self, s, i, j):
    #     print(f"SWAP {i} and {j}")
    #     n = len(s)

    #     # s = [s', s_i, s'', s_j, s''']
    #     s = self.swap0End(s, i)

    #     # s = [s_i, s'', s_j, s''', s']
    #     s = self.swap1End(s, j-i-1)

    #     # s = [s_i, s_j, s''', s', s'']
    #     s = self.swap01(s)

    #     # s = [s_j, s_i, s''', s', s'']
    #     s = self.swap1End(s, 1+(n-1-j)+i)

    #     # s = [s_j, s'', s_i, s''', s']
    #     s = self.swap0End(s, 1+(j-i-1))

    #     # s = [s_i, s''', s', s_j, s'']
    #     s = self.swap0End(s, 1+(n-1-j))

    #     # s = [s', s_j, s'', s_i, s''']
    #     return s
###


class Solution(object):
    def orderlyQueue(self, s, k):
        minStr = 'z'*len(s)
        if k == 1:
            for i in range(len(s)):
                cStr = s[i:]+s[:i]
                if cStr < minStr:
                    minStr = cStr
        else:
            minStr = ''.join(c for c in sorted(s))
        return minStr

s = Solution()
strIn = 'baaca'
k = 3
print(s.orderlyQueue(strIn, k))