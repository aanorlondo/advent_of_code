import os, datetime

STRENGTH = "J123456789TQKA"


class Hand:
    def __init__(self, cards: str, bid: str) -> None:
        self.sequence = cards
        self.cards = tuple([i for i in cards])
        self.bid = int(bid)
        self.type = self.get_type()

    def get_type(self) -> int:
        jokers = self.cards.count("J")
        card_kinds = set(self.cards)
        card_kinds.discard("J")
        match (len(card_kinds)):
            case 0:
                return 7  # All jokers
            case 1:
                return 7  # Five of a Kind
            case 2:
                for card in card_kinds:
                    if self.cards.count(card) + jokers == 4:
                        return 6  # Four of a Kind
                return 5  # Full house
            case 3:
                for card in card_kinds:
                    if self.cards.count(card) + jokers == 3:
                        return 4  # Three of a Kind
                return 3  # Two pairs
            case 4:
                return 2  # One pair
            case 5:
                return 1  # High hand


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def main(debug=False) -> None:
    lines = read_input(debug)
    hands = []
    for line in lines:
        cards, bid = line.strip().split()
        hands.append(Hand(cards=cards, bid=bid))
    hands.sort(key=lambda x: (x.type, [STRENGTH.index(c) for c in x.sequence]))
    winnings = 0
    for hand in hands:
        winnings += hand.bid * (hands.index(hand) + 1)
    print(winnings)


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

# 1ST TRY: 246894760 CORRECT
