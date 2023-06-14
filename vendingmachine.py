def take():
    given = int(input('Input money: '))
    print('You have given %d.' % given)
    return given


class vending:
    beverage = {3000: ['Coca Cola', 'Fanta'], 3500: ['Sprite', 'Dr. Pepper'], 2000: ['Water, Pocari Sweat']}

    def choice1(self):
        print('3000: Coca Cola, Fanta')
        print('3500: Sprite, Dr. Pepper')
        print('2000: Water, Pocari Sweat')
        select1 = int(input('Choose a price! '))
        return select1

    def choice2(self, selected_price):
        print('Which one would you like?', vending.beverage[selected_price])
        select2 = input('')
        return select2

    def outcome(self, selected_beverage, money_given, cost):
        print('You have chosen: %s' % selected_beverage)
        print('The cost is %d' % cost)
        if money_given - cost > 0:
            print('%d will be returned. Enjoy your beverage!' % (money_given - cost))
        elif money_given - cost == 0:
            print('Enjoy your beverage!')
        else:
            print('Not enough money!')


machine = vending()

print('Welcome')
money = take()
chosen_price = machine.choice1()
chosen_beverage = machine.choice2(chosen_price)
machine.outcome(chosen_beverage, money, chosen_price)