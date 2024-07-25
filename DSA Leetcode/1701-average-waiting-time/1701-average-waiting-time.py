class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t=0
        total=0
        for arrival,complete in customers:
            if t>arrival:
                total=total+t-arrival
            else:
                t=arrival
            total=total+complete
            t+=complete
        return total/len(customers)