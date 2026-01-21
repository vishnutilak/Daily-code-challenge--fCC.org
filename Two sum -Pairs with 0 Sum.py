class Solution:
    def getPairs(self, arr):
        arr.sort()
        n = len(arr)
        res = []

        left, right = 0, n - 1

        while left < right:
            s = arr[left] + arr[right]

            if s == 0:
                res.append([arr[left], arr[right]])

                # skip duplicates
                left_val = arr[left]
                right_val = arr[right]

                while left < right and arr[left] == left_val:
                    left += 1
                while left < right and arr[right] == right_val:
                    right -= 1

            elif s < 0:
                left += 1
            else:
                right -= 1

        return res
