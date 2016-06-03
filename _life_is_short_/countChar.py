import string

__author__ = 'sure GM'

def countchar(s):
    s = str(s).lower()
    lt = string.lowercase
    result = [0]*26
    for index, value in enumerate(lt):
        result[index]=s.count(value)
    return result

print countchar(raw_input())