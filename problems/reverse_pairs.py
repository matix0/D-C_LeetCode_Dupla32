class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort_and_count(nums, start, end):
            if start >= end:
                return 0

            mid = (start + end) // 2
            count = merge_sort_and_count(nums, start, mid) + merge_sort_and_count(
                nums, mid + 1, end
            )

            # Contador de pares reversos nos dois arrays
            j = mid + 1
            for i in range(start, mid + 1):
                while j <= end and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge das metades
            temp = []
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1
            temp.extend(nums[i : mid + 1])
            temp.extend(nums[j : end + 1])

            nums[start : end + 1] = temp

            return count

        return merge_sort_and_count(nums, 0, len(nums) - 1)
