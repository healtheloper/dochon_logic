# int -> n진법 10진법으로 변환하기 int(num, n)
# -> num은 str형태로 넣어야 함
# 배열의 각 요소 합치기 ''.join(arr)
# -> int는 못합치므로, map(str,arr) 을 통해 str로 변환, '' 안에는 합치는 문자열 추가 가능
def convert(n, arr):
    if n == 0:
        return arr
    else:
        arr.append(n%3)
        n = n//3
        convert(n, arr)
def solution(n):
    arr = []
    convert(n, arr)
    convert_num = ''.join(map(str, arr))
    answer = int(convert_num, 3)
    return answer