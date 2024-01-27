class Solution:

    def hIndex(self, citations: List[int]) -> int:
        def hasAtLeastHPapersWithHCitations(h, citations):
            return sum(cnt >= h for cnt in citations) >= h     # has h papers with citations => h
        # How does this work with us not having to explicitly sort the array?
        low = 0
        high = len(citations)

        while low <= high:
            mid = (low + high) // 2
            print(mid)
            if hasAtLeastHPapersWithHCitations(mid, citations):
                low = mid + 1
            else:
                high = mid - 1

        return high
