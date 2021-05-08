def solution(s):
    answer = s.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('zero', '0')
    return int(answer)


print(solution('one4seveneight'))    # 1478
print(solution('23four5six7'))    # 234567
print(solution('2three45sixseven'))    # 234567
print(solution('123'))    # 123