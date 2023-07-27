import heapq
from collections import Counter

def topKFrequent(nums, k):
    # Count the frequency of each element in the array
    frequency = Counter(nums)
    
    # Create a min-heap to store the top k frequent elements
    heap = []
    
    # Iterate through the frequency dictionary
    for num, freq in frequency.items():
        # Push the element and its frequency into the heap
        heapq.heappush(heap, (freq, num))
        
        # If the heap size exceeds k, remove the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Retrieve the top k frequent elements from the heap
    top_k = [item[1] for item in heap]
    
    return top_k

# Example usage
nums = [1, 1, 1, 2, 2, 3]
k = 2

result = topKFrequent(nums, k)
print(result)
