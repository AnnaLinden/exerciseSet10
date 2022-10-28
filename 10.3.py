# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators
# to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bot_floor, top_floor):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.curr_floor = bot_floor

    def go_to_floor(self, floor_num):
        while self.curr_floor != floor_num:
            if floor_num > self.curr_floor:
                self.floor_up()
            elif floor_num < self.curr_floor:
                self.floor_down()

    def floor_up(self, ):
        self.curr_floor += 1
        print(f"The elevator is on floor : {self.curr_floor}.")

    def floor_down(self):
        self.curr_floor -= 1
        print(f"The elevator is on floor : {self.curr_floor}.")


class Building:
    def __init__(self, bot_floor, top_floor, elev_num):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.elev_num = elev_num
        self.elevators = []
        self.create_elevators(self.elev_num)

    def create_elevators(self, elev_num):
        num = 0
        while num != self.elev_num:
            num += 1
            self.elevators.append(Elevator(self.bot_floor, self.top_floor))
            # print("elevator is created")

    def run_elevator(self, num_of_elev, floor_num):
        elevator_index = num_of_elev - 1
        self.elevators[elevator_index].go_to_floor(floor_num)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.curr_floor = elevator.bot_floor
            print(f"The elevator is now on {elevator.curr_floor} floor.")

build1 = Building(1,10,2)
build1.run_elevator(1,5)
build1.run_elevator(2,10)
build1.fire_alarm()