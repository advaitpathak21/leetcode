class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        openb = ['[', '{']
        closeb = [']', '}']
        spacer = 0
        res = []
        flag = 0
        curr = ''
        for c, i in enumerate(A):
            if i in openb: 
                if curr: 
                    print(curr)
                    res.append(curr)
                curr = spacer*'\t' + i
                print(curr)
                res.append(curr)
                curr = ''
                spacer += 1
                flag = 0
                continue

            if i in closeb:
                spacer -= 1 
                if curr: 
                    print(curr)
                    res.append(curr)
                curr = spacer*'\t' + i
                print(curr)
                res.append(curr)
                curr = ''
                flag = 0
                continue

            if flag == 2 and i != ',':
                curr += i

            if flag == 0:
                op = spacer*'\t' + i
                curr += op
                flag = 2

            if i == ',':
                if A[c-1] in closeb:
                    res[-1] += i
                else:
                    curr += i
                    print(curr)
                    res.append(curr)
                    curr = ''
                    flag = 0 
 
        return res

x = Solution()
a = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
x.prettyJSON(a)