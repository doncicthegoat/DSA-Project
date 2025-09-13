

def detect_royal_flush(lst):

    suits = {"Diamonds":[],"Hearts":[],"Spades":[],"Clubs":[]}
    for card in lst:
        suits[card.suit].append(card)
    for suit in suits.values():
        try:
            if suit[-5].value == 10:

                return suit[-5:]
        except IndexError:

            continue

    return []

def detect_flush(lst):
    suits = {"Diamonds": [], "Hearts": [], "Spades": [], "Clubs": []}
    for card in lst:
        suits[card.suit].append(card)

    for suit in suits.values():
        if len(suit) >= 5:
            return suit[-5:]
    return []



def detect_four_of_a_kind(hand):
   lst=hand
   i = -1
   j = i - 3
   while j >= -len(lst) and len(lst) > 0:


       if lst[i].value == lst[j].value:
           return [lst[i],lst[i-1],lst[i-2],lst[j]]
       else:
           i -= 1
           j = i - 3
   return []

def detect_three_of_a_kind(lst):

   i = -1
   j = i - 2
   while j >= -len(lst) and len(lst) > 0:


       if lst[i].value == lst[j].value:
           return [lst[i],lst[i-1],lst[j]]
       else:
           i -= 1
           j = i - 2
   return []


def detect_one_pair(lst):
    i = -1
    j = i - 1
    while j >= -len(lst) and len(lst)>0:

        if lst[i].value == lst[j].value:
            return [lst[i],lst[j]]
        else:
            i -= 1
            j = i - 1
    return []

def detect_two_pair(lst):
    other_pair = detect_one_pair(lst)

    if other_pair:
        new_cards = []
        for card in lst:
            if card not in other_pair:
                new_cards.append(card)
        lst = new_cards
        i = -1
        j = i - 1
        while j >= -len(lst) and len(lst) > 0:

            if lst[i].value == lst[j].value and lst[i].value:
                return ([lst[j], lst[i]] + other_pair)
            else:
                i -= 1
                j = i - 1

    return []




def remove_duplicates(lst):
    if len(lst) > 0:
       result = [lst[0]]
       for i in range(1, len(lst)):
           if lst[i] != result[-1]:
               result.append(lst[i])
       return result
    else:
        return []

def detect_straight(lst):

    card_values=[card.value for card in lst]
    card_values=remove_duplicates(card_values)


    if all(val in card_values for val in [14,2,3,4,5]):
        hand_to_return=[]
        for value in [14,2,3,4,5]:
            for card in lst:
                if card.value == value and card not in hand_to_return:
                    hand_to_return.append(card)
                    break
        return hand_to_return


    for i in range(len(card_values) - 4):
        if card_values[i:i + 5] == list(range(card_values[i], card_values[i] + 5)):
            hand_to_return = []
            for value in card_values[i:i + 5]:
                for card in lst:
                    if card.value == value and card not in hand_to_return:
                        hand_to_return.append(card)
                        break
            return hand_to_return
    return []

def detect_straight_flush(lst):
    suits = {"Diamonds":[],"Hearts":[],"Spades":[],"Clubs":[]}
    for card in lst:
        suits[card.suit].append(card)


    for suit in suits.values():
        if len(suit) > 0:
            if detect_straight(suit):
                return detect_straight(suit)
    return []

def detect_full_house(hand):

    """three_of_a_kind_result=detect_three_of_a_kind(hand)
    if not three_of_a_kind_result:
        return []


    one_pair_result = detect_one_pair(hand)
    if not one_pair_result:
        return []


    if  three_of_a_kind_result[2]!=one_pair_result[1]:
        full_house_cards= three_of_a_kind_result+one_pair_result


        return full_house_cards
    return []"""
    def update(cards, lst):
        new_cards = []
        for card in cards:
            if all((card.value,card.suit) != (card1.value,card1.suit) for card1 in lst):
                new_cards.append(card)
        cards = new_cards
        return cards

    temp = hand[:]
    three_of_a_kind_result = detect_three_of_a_kind(temp)
    if not three_of_a_kind_result:
        return []
    temp= update(temp,three_of_a_kind_result)

    one_pair_result = detect_one_pair(temp)
    if not one_pair_result:
        return []
    temp = update(temp,one_pair_result)

    if three_of_a_kind_result[2] != one_pair_result[1]:
        full_house_cards = three_of_a_kind_result + one_pair_result

        return full_house_cards
    return []