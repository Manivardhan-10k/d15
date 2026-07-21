def CheckAnagrams(A, B):
      
    A=list(A)
    A.sort()
    A="".join(A)
    B=list(B)
    B.sort()
    B="".join(B)
    if A==B:
        return True
    else:
        return False