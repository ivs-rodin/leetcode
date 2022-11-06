class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        resD = {}
        mul = [1]
        mulStr = ''
        curF = ''
        cMul = 1
        for c in formula[::-1]:
            if c.isdigit():
                mulStr = c+mulStr
            else:
                if c == ')':
                    if len(mulStr):
                        mul.append(mul[-1]*int(mulStr))
                        mulStr = ''
                    else:
                        mul.append(mul[-1])
                elif c == '(':
                    mul = mul[:-1]
                else:
                    curF = c+curF
                    if c.isupper():
                        if len(mulStr):
                            cMul = int(mulStr)
                        if curF in resD:
                            resD[curF] += mul[-1]*cMul
                        else:
                            resD[curF] = mul[-1]*cMul
                        cMul = 1
                        curF = ''
                        mulStr = ''
        result = ''
        for k,v in sorted(resD.items()):
            result += k+(str(v) if v > 1 else '')
        return result


        