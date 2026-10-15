class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors=[]
        i=1
        while i*i<=num:
            if num%i==0 :
                divisors.append(i)
                if i!=num//i:
                    divisors.append(num//i)
            i+=1
        return (num==sum(divisors)-num)