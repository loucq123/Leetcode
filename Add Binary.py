class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        sum = ['0'] * (len(a) + 1)
        offset = 0
        for c in range(len(a) - 1, -1, -1):
            if a[c] == '1' and b[c] == '1':
                sum[c + 1] = str(offset)
                offset = 1
            elif a[c] == '0' and b[c] == '0':
                sum[c + 1] = str(offset)
                offset = 0
            else:
                sum[c + 1] = str(abs(offset - 1))
        if offset == 1:
            sum[0] = '1'
        notZeroIndex = 0
        while notZeroIndex < len(sum) - 1:
            if sum[notZeroIndex] == '0':
                notZeroIndex += 1
            else:
                break
        sum = sum[notZeroIndex:]
        return ''.join(sum)