"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dupes_table = {}
        for num in nums:
            if num in dupes_table.keys():
                return True
            dupes_table[num] = True
        return False


def check_solution() -> None:
    cd = Solution().containsDuplicate

    test_cases = [
        ([1,2,3,1], True),
        ([1,2,3,4], False),
        ([1,1,1,3,3,4,3,2,4,2], True),
    ]

    for index, test_case in enumerate(test_cases):
        numbers = test_case[0]
        expected_result = test_case[1]
        actual_result = cd(numbers)
        test_result = "PASS" if expected_result == actual_result else "FAIL"
        message = f"""
        Test Case {index + 1}: Nums: {numbers}
        Expected: {expected_result}
        Actual: {actual_result}
        PASS/FAIL: {test_result}
        {20*"="}
        """

        print(message)


if __name__ == "__main__":
    check_solution()
