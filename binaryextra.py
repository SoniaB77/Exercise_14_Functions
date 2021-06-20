def solution(n):
    n = bin(n)
    trail_removed = n[2:].rstrip('0').split('1')
    print(trail_removed)
    # print (trail_removed)
    # gap_list = trail_removed.split(1)
    max_gap = max(trail_removed)
    print(len(max_gap))

solution(20)

solution(529)

solution(1041)

# test = int(input("number: "))
# print(bin(test))
# solution(test)

# def solution(N):
#     max_gap = 0
#     current_gap = 0
#     # Skip the tailing zero(s)
#     while N > 0 and N%2 == 0:
#         N //= 2
#     while N > 0:
#         remainder = N%2
#         if remainder == 0:
#             # Inside a gap
#             current_gap += 1
#         else:
#             # Gap ends
#             if current_gap != 0:
#                 max_gap = max(current_gap, max_gap)
#                 current_gap = 0
#         N //= 2
#     return max_gap