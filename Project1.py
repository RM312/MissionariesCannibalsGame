boat_side = 'Right'
missionaries_on_right = 3
cannibals_on_right = 3 
missionaries_on_left = 0
cannibals_on_left = 0 

print('Missionaries=',missionaries_on_left, 'Cannibals=',cannibals_on_left, '|-----B|', 'Missionaries=',missionaries_on_right,'Cannibals=',cannibals_on_right)

while True:

    missionaries = int(input('No of Missionaries or Enter 10 to quit : '))
    if missionaries == 10:
        print('You Quit. Game Over!')
        break
    cannibals = int(input('No.of Cannibals : '))

    if (missionaries + cannibals) != 1 and (missionaries + cannibals) != 2:
        print('Invalid Move')
        continue

    if boat_side == 'Right':
        if missionaries_on_right < missionaries or cannibals_on_right < cannibals:
            print('Invalid Move')
            continue

        missionaries_on_right -= missionaries
        cannibals_on_right -= cannibals

        missionaries_on_left += missionaries
        cannibals_on_left += cannibals
        
        print('Missionaries=',missionaries_on_left, 'Cannibals=',cannibals_on_left, '|B-----|', 'Missionaries=',missionaries_on_right,'Cannibals=',cannibals_on_right)
        
        boat_side = 'Left'

    else:
        if missionaries_on_left < missionaries or cannibals_on_left < cannibals:
            print('Invalid Move')
            continue
            
        missionaries_on_left -= missionaries
        cannibals_on_left -= cannibals

        missionaries_on_right += missionaries
        cannibals_on_right += cannibals
        
        print('Missionaries=',missionaries_on_left, 'Cannibals=',cannibals_on_left, '|-----B|', 'Missionaries=',missionaries_on_right,'Cannibals=',cannibals_on_right)
        boat_side = 'Right'

    if (missionaries_on_right < cannibals_on_right and missionaries_on_right > 0) or (missionaries_on_left < cannibals_on_left and missionaries_on_left > 0):
        print('You Lose')
        break

    if missionaries_on_left == 3 and cannibals_on_left == 3:
        print('You Win')
        break
