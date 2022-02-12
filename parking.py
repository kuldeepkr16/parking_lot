class CarDetails:
    def __init__(self, reg_number, color, slot, next_=None):
        self.reg_number = reg_number
        self.color = color
        self.slot = slot
        self.next = next_


class Parking:
    def __init__(self):
        self.head = None

    def park_at_given_slot(self, reg_number, color, slot):
        if not self.head or slot == 1:
            car = CarDetails(reg_number, color, 1, self.head)
            self.head = car
            return
        car_i = self.head
        while car_i:
            if car_i.slot == slot - 1:
                car_i.next = CarDetails(reg_number, color, slot, car_i.next)

            car_i = car_i.next

    def free_given_slot(self, slot):
        if slot == 1:
            self.head = self.head.next
            return
        car_i = self.head
        car_i_prev = None
        while car_i:
            if car_i.slot == slot:
                if car_i == self.head:
                    self.head = self.head.next
                    break
                else:
                    car_i_prev.next = car_i.next
                    break
            car_i_prev = car_i
            car_i = car_i.next

    def get_car_details(self):
        if self.head is None:
            return "No cars parked"
        car_i = self.head
        car_list = list()
        while car_i:
            car_list.append({"reg_number": car_i.reg_number, "color": car_i.color, "slot": car_i.slot})
            car_i = car_i.next
        return car_list


def create_car_register(slots):
    cars_dict = dict()
    i = 1
    while i <= slots:
        cars_dict.update({i: False})
        i += 1
    return cars_dict


if __name__ == '__main__':
    car_parking = None
    cars_dict = None
    capacity = 0
    while True:
        cmd = input("$ ")
        if "create_parking_lot " in cmd:
            try:
                _, capacity = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue
            car_parking = Parking()
            cars_dict = create_car_register(int(capacity))
            print(f"Created a parking lot with {capacity} slots")
        if not car_parking:
            print("No Parking Lot Found")
            continue
        if "park " in cmd:
            slot = 0
            try:
                _, reg_number, color = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue

            parking_lot_full = False
            for slot, status in cars_dict.items():
                if not status:
                    car_parking.park_at_given_slot(reg_number, color.lower(), slot)
                    cars_dict[slot] = True
                    print(f"Allocated slot number: {slot}")
                    break
            else:
                print("Sorry, parking lot is full")
        if "leave " in cmd:
            try:
                _, slot = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue

            slot = int(slot)
            if slot < 0 or slot > int(capacity):
                print(f"Invalid slot {slot}")
                continue
            if not cars_dict[slot]:
                print(f"No cars found at slot {slot}")
                continue
            car_parking.free_given_slot(slot)
            cars_dict[slot] = False
            print(f"Slot number {slot} is free")
        if "status" in cmd:
            if not car_parking:
                print("No Parking Lot Found")
            else:
                car_details = car_parking.get_car_details()
                if "No cars parked" in car_details:
                    print(car_details)
                    continue
                print("Slot No.")
                for details in car_details:
                    print(details.get("slot"))
                print("Registration No")
                for details in car_details:
                    print(details.get("reg_number"))
                print("Colour")
                for details in car_details:
                    print(details.get("color"))
        if "registration_numbers_for_cars_with_colour " in cmd:
            try:
                _, color = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue

            car_details = car_parking.get_car_details()
            if "No cars parked" in car_details:
                print(car_details)
                continue
            Found = False
            for details in car_details:
                if details.get("color") == color.lower():
                    Found = True
                    print(details.get("reg_number"))
            if not Found:
                print("Not found")
        if "slot_numbers_for_cars_with_colour " in cmd:
            try:
                _, color = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue

            car_details = car_parking.get_car_details()
            if "No cars parked" in car_details:
                print(car_details)
                continue
            Found = False
            for details in car_details:
                if details.get("color") == color.lower():
                    Found = True
                    print(details.get("slot"))
            if not Found:
                print("Not found")
        if "slot_number_for_registration_number " in cmd:
            try:
                _, reg_number = cmd.split(" ")
            except ValueError as e:
                print("Wrong command format, please try with correct command")
                continue

            car_details = car_parking.get_car_details()
            if "No cars parked" in car_details:
                print(car_details)
                continue
            Found = False
            for details in car_details:
                if details.get("reg_number") == reg_number:
                    Found = True
                    print(details.get("slot"))
            if not Found:
                print("Not found")
        if cmd == "exit":
            break
