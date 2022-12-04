import input_reader as ir

translation = {"A": "ROCK", "B": "PAPER", "C": "SCISSOR", "X": "ROCK", "Y": "PAPER", "Z": "SCISSOR"}
translation2 = {"A": "ROCK", "B": "PAPER", "C": "SCISSOR", "X": "LOSE", "Y": "DRAW", "Z": "WIN"}
hand_scores = {"ROCK": 1, "PAPER": 2, "SCISSOR": 3}
win_combos = {"PAPER": "ROCK", "SCISSOR": "PAPER", "ROCK": "SCISSOR"}

def calc_score(elf, player):
    win_score = 6 if win_combos[player] == elf else 3 if elf == player else 0
    return win_score + hand_scores[player]

def get_losing_hand(hand):
    return win_combos[win_combos[hand]]

def get_player_hand(elf, command):
    return win_combos[elf] if command == "LOSE" else elf if command == "DRAW" else get_losing_hand(elf)

if __name__ == "__main__":
    hands = [[translation[x], translation[y]] for x, y in ir.get_lines_as_strings()]
    print(sum([calc_score(elf, player) for elf, player in hands]))

    hands = [[translation2[x], translation2[y]] for x, y in ir.get_lines_as_strings()]
    print(sum([calc_score(elf, get_player_hand(elf, player)) for elf, player in hands]))
