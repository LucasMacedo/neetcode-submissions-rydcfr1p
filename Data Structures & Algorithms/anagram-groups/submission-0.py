class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_an = {}

        for i in strs:
            key = "".join(sorted(i))
            group_an.setdefault(key, []).append(i)

        return list(group_an.values())

        