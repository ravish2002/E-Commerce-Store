# def checkIsAP(arr, n):
#     if (n == 1): 
#         return True
  
#     arr.sort();
 
#     d = arr[1] - arr[0]
  
#     for i in range(2, n): 
#         if (arr[i] - arr[i - 1] != d):
#             return False
 
#     return True
 


# def checkIsGP(arr, n):
#     if (n == 1): 
#         return True

#     arr.sort()
 
#     r = arr[1] / arr[0]

#     for i in range(2, n):
#         if (arr[i] / arr[i - 1] != r):
#             return False
 
#     return True



# n = len(arr)

# isAP = checkIsAP(arr, n)
# if isAP:
#     return "Arithmetic"

# isGP = checkIsGP(arr, n)
# if isGP:
#     return "Geometric"

# return -1

s = "MrtyNNgMM"
    new_str = ""
    i = 0
    while i < len(s):
        if s[i] == 'M':
            if len(new_str) > 0:
                new_str += new_str[-1]
                i += 1
            i += 1
        elif i < len(s) - 1 and s[i + 1] == 'M':
            new_str += s[i]
            new_str += s[i]
            i += 2
        elif s[i] == 'N':
            i += 2
        else:
            new_str += s[i]
            i += 1
    return new_str