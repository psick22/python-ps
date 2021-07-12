from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                dig_logs.append(log)
            else:
                let_logs.append(log)
        let_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return let_logs + dig_logs


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(Solution().reorderLogFiles(logs))
