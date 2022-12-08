with open('day2_pset_input.txt', 'r') as strategy_guide:
    strategy_guide = strategy_guide.readlines()
    points = 0
    for line in strategy_guide:
        if "A X\n" == line:
            points += (1 + 3)
        if "A Y\n" == line:
            points += (2 + 6)
        if "A Z\n" == line:
            points += (3 + 0)
        if "B X\n" == line:
            points += (1 + 0)
        if "B Y\n" == line:
            points += (2 + 3)
        if "B Z\n" == line:
            points += (3 + 6)
        if "C X\n" == line:
            points += (1 + 6)
        if "C Y\n" == line:
            points += (2 + 0)
        if "C Z\n" == line:
            points += (3 + 3)
    print(points)
            
