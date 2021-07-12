from typing import List
from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        s = paragraph.lower()
        s = re.sub('[^\w]', ' ', s).split()
        counter = Counter(s)
        for item in banned:
            if item in counter.keys():
                counter.pop(item)

        return counter.most_common(1)[0][0]


paragraph = "Bob!"
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
