"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = [0]

        ins = []

        for meeting in intervals:
            ins.append([meeting.start, meeting.end])

        ins.sort()

        intervals = ins

        for s, e in intervals:
            for i in range(len(rooms)):
                if rooms[i] <= s:
                    rooms[i] = e
                    break
            
            else:
                rooms.append(e)
        
        return len(rooms)