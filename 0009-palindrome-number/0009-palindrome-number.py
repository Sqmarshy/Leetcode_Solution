class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c=-1
        if x<0:
            return False
        elif x==0:
            return True
        else:
            for i in range(len(str(x))//2):
                if str(x)[i]==str(x)[c]:
                    c-=1
                else:
                    return False
            return True