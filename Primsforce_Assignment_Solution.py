number_of_chakravyhu = 11
enemy_power_in_chakravyuhu = list(map(int, input().split()))

initial_power_of_abhimanyu = int(input())
number_of_skips_abhimanyu_has = int(input())
number_of_times_abhimanyu_can_recharge = int(input())
def canAbhimanyuCrossChakravyuhu(enemy_power, chakravyuha_no, curr_power, behind_enempy_power, skips_available, recharge_available):
    if (chakravyuha_no == number_of_chakravyhu):
        # He has crossed all the enemies
        return True
    
    can_he_cross = False
    # Option 1: Abhimanyu can recharge if he has remaining recharge attempts and his power level is below the maximum limit.
    if (recharge_available > 0 and curr_power < initial_power_of_abhimanyu):
        can_he_cross |= canAbhimanyuCrossChakravyuhu(enemy_power, chakravyuha_no, initial_power_of_abhimanyu, behind_enempy_power, skips_available, recharge_available - 1)

    # If Abhimanyu can fight enemy coming from behind
    if (curr_power >= behind_enempy_power):
        curr_power -= behind_enempy_power
        behind_enempy_power = 0
    else:
        return False
    
    # Option 2: Abhimanyu can skip the enemy
    if (skips_available > 0):
        can_he_cross |= canAbhimanyuCrossChakravyuhu(enemy_power, chakravyuha_no + 1, curr_power, behind_enempy_power, skips_available - 1, recharge_available)

    # Option 3: Fight with current enemy if have greater power
    if (curr_power >= enemy_power[chakravyuha_no]):
        if (chakravyuha_no == 2 or chakravyuha_no == 6):
            behind_enempy_power = enemy_power[chakravyuha_no]//2

        can_he_cross |= canAbhimanyuCrossChakravyuhu(enemy_power, chakravyuha_no + 1, curr_power - enemy_power[chakravyuha_no], behind_enempy_power, skips_available, recharge_available)
    
    return can_he_cross


chakravyuha_number = 0

behind_enemy_power = 0

if canAbhimanyuCrossChakravyuhu(enemy_power_in_chakravyuhu, chakravyuha_number,
                                 initial_power_of_abhimanyu, behind_enemy_power, 
                                 number_of_skips_abhimanyu_has, number_of_times_abhimanyu_can_recharge):
    print("Abhimanyu has crossed the Chakravyuha")
else:
    print("Abhimanyu failed to cross the Chakravyuha")