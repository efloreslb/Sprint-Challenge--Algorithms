'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
   if len(word) <= 1:
      return 0

   # print(f'[0:1] {word[0:2]}')
   # print(f'[1:] {word[1:]}')

   if word[0:2] == 'th':
      return 1 + count_th(word[1:])

   # print(word[1:])
      
   return count_th(word[1:])

# print(f'total: {count_th("abcthefthghith")}')