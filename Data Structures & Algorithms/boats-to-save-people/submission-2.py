class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort the people's array so we get weights in order
        # then have two pointers l and r
        # initialize a variable called boats to 0
        # initialize l to 0 and r at the end
        # from there, we try combinations
        # if l + r exceeds the limit or if r = limit, we bring r to the left
        # vice versa for not exceeding the limit
        # if both equal the limit, we bring both inward
        # we add 1 to boats if l + r = limit or r = limit
        # [1,2,4,5]
        # [1,2,2,3,3]
        people.sort()

        boats = 0
        l = 0
        r = len(people) - 1
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
            
            boats += 1
            r -= 1


        return boats
             




        

            

            
            

                
        


        
        
