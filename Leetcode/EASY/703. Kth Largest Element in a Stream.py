import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappushpop(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)  # 小的都pop掉
        return self.minHeap[0]  #最上面的就是kth


def main():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))

main()