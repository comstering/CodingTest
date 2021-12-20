import sys
count = sys.stdin.readline()
locate_list = list(map(int, sys.stdin.readline().split()))
locate_set = sorted(list(set(locate_list)))
locate_dic = {v: i for i, v in enumerate(locate_set)}

locate_result = [locate_dic[i] for i in locate_list]

print(' '.join(map(str, locate_result)))