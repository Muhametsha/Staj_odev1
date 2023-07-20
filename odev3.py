def longest_common_subarray(list1, list2):
    # Sub-function: Finds the longest common subarray in two arrays
    def find_longest_common_subarray(arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        max_length = 0  # Variable to track the length of the longest common subarray
        ending_index = 0  # Ending index of the longest common subarray
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Dynamic programming table

        # Finding the length of the longest common subarray using dynamic programming
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        ending_index = i

        # Finding the longest common subarray
        longest_subarray = arr1[ending_index - max_length:ending_index]
        return longest_subarray

    # Finding the length of the longest common subarray between the two lists
    longest_subarray = find_longest_common_subarray(list1, list2)
    return len(longest_subarray)

# Test
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
result = longest_common_subarray(list1, list2)
print(result)  # Output: 3 (Longest common subarray: [4, 5, 6])
