# import modules
import math
import random


# define functions
def money_stage(eur_key):
    # print('DEBUG - money_stage - eur_key:', eur_key)
    # print('DEBUG - money_stage - diff:', diff)
    # difference is met -> do nothing
    if diff == 0:
        return
    # absolute difference is less than eur_cent -> do nothing
    if math.fabs(diff) < eur_key:
        return
    # determine if we take or put money
    take_money = False
    if diff < 0:
        take_money = True
        # print('DEBUG - take_money:', take_money)
    # when taking money, make sure we have s/th to take in this money stage
    avail = eur[eur_key]
    # print('DEBUG - eur_key:', str(eur_key) + ', avail:', avail)
    if take_money and avail == 0:
        return
    # check if diff is euros only, then ignore cents
    if math.modf(diff)[0] == 0 and eur_key < 1:
        return
    # take / give money with 10% probability
    prob = random.random()
    # print ('DEBUG - prob:', prob)
    if prob < 0.1 or ( diff == 0.01 and eur_key == 0.01 ):
        # when about to hand out the money stage item, make sure all the stages equal or beneath can still service the
        #     spare amount
        spare = calc_current(eur_key)
        new_abs_diff = round(abs(diff + eur_key), 2)
        # print('DEBUG - spare:', spare)
        if take_money:
            if new_abs_diff < spare:
                print('DEBUG - taking one money item of: ' + str(eur_key) + ', new_abs_diff: ' + str(new_abs_diff)
                      + ', spare: ' + str(spare))
                eur[eur_key] = eur[eur_key] - 1
        else:
            print('DEBUG - adding one money item of:', eur_key)
            eur[eur_key] = eur[eur_key] + 1


def calc_current(init_stage):
    result = 0.0
    for calc_key in eur:
        if calc_key <= init_stage:
            result += calc_key * eur[calc_key]
    result = round(result, 2)
    # print('DEBUG - calc_current(' + str(init_stage) + '): ' + str(result))
    return round(result, 2)


# define start values (150,02 EUR)
eur = { 200: 0, 100: 0, 50: 2, 20: 0, 10: 2, 5: 4, 2: 2, 1: 2, 0.5: 4, 0.2: 7, 0.1: 3, 0.05: 4, 0.02: 5, 0.01: 2 }

# print current amount
print('Current:', calc_current(200))

# loop forever, on each loop: fall through the money stages, applying each stage with 10% probability until the
#     difference is met

while True:
    # prompt for new amount
    new = float(input('Neuer Betrag: ').replace(',', '.'))
    # pre-calculate the difference
    diff = round(new - calc_current(200), 2)
    # print('DEBUG - initial diff:', diff)
    while diff != 0:
        for key in eur:
            # try to apply money item
            money_stage(key)
            # re-calculate the difference
            diff = round(new - calc_current(200), 2)
            # print('DEBUG - diff:', diff)
    # print resulting money stages
    for key in eur:
        print(str(key) + ':', eur[key])
