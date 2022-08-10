"""Functions to help play and score a game of blackjack."""

def value_of_card(card):
    """Determine the scoring value of a card."""
    face_cards = ('J', 'Q', 'K')
    number_cards = ('2','3','4','5','6','7','8','9','10')
    ace_card = ('A')

    if card in face_cards:
        card_value = 10
    elif card in number_cards:
        card_value = int(card)
    elif card in ace_card:
        card_value = 1

    return card_value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    if card_one_value > card_two_value:
        high_card = card_one
    elif card_one_value < card_two_value:
        high_card = card_two
    else:
        high_card = (card_one, card_two)

    return high_card

def value_of_hand(card_one, card_two):
    """Calculate the higherst possible value of hand"""
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    # Determine best values of aces in hand
    if card_one_value == 1:
        card_one_value = 11
    elif card_two_value == 1:
        card_two_value = 11

    # Get total value of hand
    hand_value = card_one_value + card_two_value

    return hand_value


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""
    # Get total value of hand
    hand_value = value_of_hand(card_one, card_two)

    # Determine most advantageous value for upcoming ace card
    if hand_value < 11:
        ace_card = 11
    else:
        ace_card = 1

    return ace_card


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    # Get total value of hand
    hand_value = value_of_hand(card_one, card_two)

    return hand_value == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)

    return card_one_value == card_two_value


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    hand_value = value_of_hand(card_one, card_two)
    double_down_cond = (9,10,11)
    ace_can_double_down = hand_value-10 in double_down_cond

    # Determine if reducing high ace value to 1 results in a double down condition
    if card_one == 'A' and ace_can_double_down:
        double_down = True
    elif card_two == 'A' and ace_can_double_down:
        double_down = True
    else:
        double_down = hand_value in double_down_cond

    return double_down
