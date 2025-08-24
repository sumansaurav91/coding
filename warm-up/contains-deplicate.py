# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return True
        seen[num] = True
    return False

# Example usage:
print(containsDuplicate([1, 2, 3, 1]))  # Output
# True
print(containsDuplicate([1, 2, 3, 4]))  # Output
# False
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output
# True

# Time complexity: O(n)
# Space complexity: O(n)
# True
# False
# True

def containsDuplicate(nums):
    set_nums = set()
    for num in nums:
        if num in set_nums:
            return True
        set_nums.add(num)
    return False