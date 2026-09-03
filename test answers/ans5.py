def find_kth_largest(nums: List[int], k: int) -> int:
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
