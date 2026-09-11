class Solution:
    def nextGreaterElement(self, nums1, nums2):

        stack = []
        greater = {}

        for num in nums2:

            while stack and num > stack[-1]:
                x = stack.pop()
                greater[x] = num

            stack.append(num)

        answer = []

        for num in nums1:
            if num in greater:
                answer.append(greater[num])
            else:
                answer.append(-1)
        return answer