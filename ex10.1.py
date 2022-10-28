# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The
# elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you
# make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down
# methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and
# tell what floor the elevator is after each move. Test the class by creating an elevator in the main program,
# tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bot_floor, top_floor):
        self.bot_floor = bot_floor
        self.top_floor = top_floor
        self.curr_floor = bot_floor

    def go_to_floor(self, floor_num):
        while (self.curr_floor != floor_num):
            if floor_num > self.curr_floor:
                self.floor_up()
            elif floor_num < self.curr_floor:
                self.floor_down()

    def floor_up(self, ):
        self.curr_floor += 1
        print (f"The elevator is on floor : {self.curr_floor}.")

    def floor_down(self):
        self.curr_floor -= 1
        print(f"The elevator is on floor : {self.curr_floor}.")

elevator1 = Elevator(1,10)
elevator1.go_to_floor(5)
elevator1.go_to_floor(elevator1.bot_floor)
