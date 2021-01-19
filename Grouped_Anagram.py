class Solution:
   def groupAnagrams(self, strs):
      result = {}
      for i in strs:
         x = "".join(sorted(i))
         if x in result:
             result[x] = [i]
         else:
             result[x].append(i)
      return list(result.values())
ob1 = Solution()
