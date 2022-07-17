#
# def decodeAtIndex( s: str, k: int) -> str:
#     space = ''
#     for i in s:
#         if len(space) == k:
#             return space[k-1]
#         if not i.isdigit():
#             space = ''.join(i)
#         if i.isdigit():
#             space * int(i)
#     # print(space)
#
#
# # print(decodeAtIndex(s='ahdhe12', k = 5))



s = input('enter your two digits:')

a = int(s[0]) + int(s[1])

print(a)
