from collections import deque
class FirstUnique:

    # have a queue that is initialized with the nums array
    # define a count hashmap
    # in the showFirstUnique function, remove the non-unique members first
    # then, return the first element in the queue if the queue is non-empty
    # in the add function, if the element is already in the count map, update the count
    # if not, add to the queue and set the count of that element to 1


    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.count = {}

        for num in nums:
            self.add(num) 
        

    def showFirstUnique(self) -> int:
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()

        return self.queue[0] if self.queue else -1



    def add(self, value: int) -> None:
        if value in self.count:
            self.count[value] += 1
        else:
            self.queue.append(value)
            self.count[value] = 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
