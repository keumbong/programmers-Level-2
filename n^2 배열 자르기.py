def solution(n, left, right):
    arr_list = []
    for i in range(1, n + 1):
        arr = list(range(1, n + 1))
        for j in range(i):
            arr[j] = i
        arr_list += arr
    return arr_list[left:right+1]
# 시간초과


def solution(n, left, right):
    answer = []    
    for i in range(left, right + 1):
        answer.append(max(divmod(i, n)) + 1)
    return answer
