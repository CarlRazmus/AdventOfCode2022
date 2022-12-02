import input_reader as ir


winning_hands = {"PAPER": "ROCK", "SCISSOR": "PAPER", "ROCK": "SCISSOR"}
losing_hands = {"PAPER": "SCISSOR", "SCISSOR": "ROCK", "ROCK": "PAPER"}
translation = {"A": "ROCK", "B": "PAPER", "C": "SCISSOR", "X": "ROCK", "Y": "PAPER", "Z": "SCISSOR"}
hand_scores = {"ROCK": 1, "PAPER": 2, "SCISSOR": 3}


def calc_score(elf, player):
    win_score = 6 if winning_hands[player] == elf else 3 if elf == player else 0
    return win_score + hand_scores[player]

def get_player_hand(elf, command):
    return winning_hands[elf] if command == "ROCK" else elf if command == "PAPER" else losing_hands[elf]

if __name__ == "__main__":
    hands = [[translation[x], translation[y]] for x, y in ir.get_lines_as_strings(ir.read_input_lines())]
    print(sum([calc_score(elf, player) for elf, player in hands]))
    print(sum([calc_score(elf, get_player_hand(elf, player)) for elf, player in hands]))
