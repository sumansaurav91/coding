
# Problems: Sort colors in an array
#
# Statement
#     Given an array, colors, which contains a combination of the following three elements:
#
#     * 0 (Representing red)
#     * 1 (Representing white)
#     * 2 (Representing blue)
#
#     Sort the array in place so that the elements of the same color are adjacent, and the final order is: red (0), then white (1), and then blue (2).
#     Note: You are not allowed to use any built-in sorting functions. The goal is to solve this efficiently without extra space.
#
#     Constraints:
#     * n == colors.length
#     * 1 ≤ n ≤ 300
#     * colors[i] is either 0, 1, or 2
# Algorithm: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
# Take 2 pointers, one at the start and one at the end.
# Iterate through the array and swap the elements based on their colors.

def sort_colors(colors):
    low, mid, high = 0, 0, len(colors) - 1
    while mid <= high:
        if colors[mid] == 0:
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
        elif colors[mid] == 1:
            mid += 1
        else:
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1
        print("Current array:", colors)
    return colors

if __name__ == "__main__":
    user_input = input("Enter the colors array (comma-separated, e.g., 2,0,2,1,1,0): ")
    colors = [int(x.strip()) for x in user_input.split(",") if x.strip() in {'0', '1', '2'}]
    sort_colors(colors)
    print("Sorted colors:", colors)

# Output Example:
# Enter the colors array (comma-separated, e.g., 2,0,2,1,1,0): 0,1,2,0,1,2
# Current array: [0, 1, 2, 0, 1, 2]
# Current array: [0, 1, 2, 0, 1, 2]
# Current array: [0, 1, 2, 0, 1, 2]
# Current array: [0, 1, 1, 0, 2, 2]
# Current array: [0, 1, 1, 0, 2, 2]
# Current array: [0, 0, 1, 1, 2, 2]
# Sorted colors: [0, 0, 1, 1, 2, 2]