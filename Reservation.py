class Reservations:
    def __init__(self):
        self.taken = {'vacant': ['A1', 'A2', 'B3', 'B4'], 'occupied': ['A3', 'A4', 'B1', 'B2']}

    def monitor(self):
        seats = []
        print('The seats are placed as followed:')
        for i in range(2):
            row = []
            for j in range(4):
                if i == 0:
                    row.append('A' + str(j + 1))
                else:
                    row.append('B' + str(j + 1))
            seats.append(row)

        for row in seats:
            print(row)
        return ""

    def select(self):
        print('The remaining seats are: ')
        print(self.taken['vacant'])
        seat_choice = input('Please choose a seat! ')
        return seat_choice

    def outcome(self, choice):
        print('You have chosen %s.' % choice)
        print('Your seat is successfully reserved.')


print('Welcome!')
reservation = Reservations()
reservation.monitor()
print('')
choice = reservation.select()
print('')
reservation.outcome(choice)