class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleets = 0
        current_time = 0.0

        for pos, sp in cars:
            time_to_target = (target - pos) / sp
            if time_to_target > current_time:
                fleets += 1
                current_time = time_to_target

        return fleets