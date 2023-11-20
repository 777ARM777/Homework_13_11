class Solution:
    def sortArray(self, array: List[int]) -> List[int]:
        min_element = min(array)
        max_element = max(array)
        res = []

        count = [0] * (max_element - min_element + 1)
        for i in range(len(array)):
            count[array[i] - min_element] += 1

        for i in range(len(count)):
            res.extend([i + min_element] * count[i])
        return res