class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        openb = ['[', '{']
        closeb = [']', '}']
        spacer = 0
        res = []
        curr = ''

        for c, i in enumerate(A):
            if i in openb: 
                if curr: 
                    print(curr)
                    res.append(spacer*'\t' + curr)
                curr = spacer*'\t' + i
                print(curr)
                res.append(curr)
                curr = ''
                spacer += 1
            elif i in closeb:
                if curr: 
                    print(curr)
                    res.append(spacer*'\t' + curr)
                spacer -= 1 
                curr = spacer*'\t' + i
                print(curr)
                res.append(curr)
                curr = ''
            elif i == " ":
                curr = ''
            elif i == ',':
                if A[c-1] in closeb:
                    res[-1] += i
                else:
                    curr = spacer*'\t' + curr + i
                    print(curr)
                    res.append(curr)
                    curr = ''
            else:
                curr += i
 
        return res

x = Solution()
a = '{"attributes":[{"nm":"ACCOUNT","lv":[{"v":{"Id":null,"State":null},"vt":"java.util.Map","cn":1}],"vt":"java.util.Map","status":"SUCCESS","lmd":13585},{"nm":"PROFILE","lv":[{"v":{"Party":null,"Ads":null},"vt":"java.util.Map","cn":2}],"vt":"java.util.Map","status":"SUCCESS","lmd":41962}]}'
x.prettyJSON(a)