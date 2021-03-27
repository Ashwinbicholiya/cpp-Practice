def countOccurrences(needle,haystack):
    res=[int(x) for x in str(haystack)]
    occurance = res.count(needle)
    return occurance

needle=int(input())
haystack=int(input())
result = countOccurrences(needle,haystack)
print(result)