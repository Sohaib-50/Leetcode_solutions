class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        r_queue = []
        d_queue = []
        count_senators = len(senate)

        for i, senator in enumerate(senate):
            if senator == 'R':
                r_queue.append(i)
            else:
                d_queue.append(i)

        print("Before:", r_queue, d_queue)

        while r_queue and d_queue:
            earliest_r = r_queue.pop(0)
            earliest_d = d_queue.pop(0)

            if earliest_r < earliest_d:
                r_queue.append(earliest_r + count_senators)
            else:
                d_queue.append(earliest_d + count_senators)

        print("After:", r_queue, d_queue)

        if len(r_queue) == 0:
            return "Dire"
        return "Radiant"
