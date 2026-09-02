class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        ans = 0

        for j in range(n):
            leftSmaller = 0
            leftGreater = 0
            rightSmaller = 0
            rightGreater = 0

            # Check elements on the left
            for i in range(j):
                if rating[i] < rating[j]:
                    leftSmaller += 1
                elif rating[i] > rating[j]:
                    leftGreater += 1

            # Check elements on the right
            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    rightSmaller += 1
                elif rating[k] > rating[j]:
                    rightGreater += 1

            # Increasing: smaller on left + greater on right
            ans += leftSmaller * rightGreater

            # Decreasing: greater on left + smaller on right
            ans += leftGreater * rightSmaller

        return ans