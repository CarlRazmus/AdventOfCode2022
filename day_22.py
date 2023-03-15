import input_reader as ir
import pprint as pp

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
DIRECTIONS = {RIGHT : (1,0), DOWN : (0, 1), LEFT : (-1, 0), UP : (0, -1)}

def get_next_facing(facing, turn):
  return (facing + (1 if turn == "R" else -1)) % 4

def get_next_pos_with_wrapping(val, inc, max_len):
  next_val = val + inc
  if next_val < 0:
    next_val = max_len
  elif next_val > max_len:
    next_val = 0
  return next_val

def move_to_next_location(pos, facing):
  direction = DIRECTIONS[facing]
  next_pos = pos
  next_pos_char = " "
  while next_pos_char == " ":
    next_x = get_next_pos_with_wrapping(next_pos[0], direction[0], max_width -1)
    next_y = get_next_pos_with_wrapping(next_pos[1], direction[1], len(char_lines) - 1)
    next_pos = (next_x, next_y)
    next_pos_char = char_lines[next_pos[1]][next_pos[0]]
  if next_pos_char == "#":
    #print("hit stone, stay at ", pos)
    return pos
  return next_pos

if __name__ == "__main__":
  lines = ir.read_input_lines()
  char_lines = lines[:-1]
  instructions = [c for c in lines[-1]]
  max_width = max([len(v) for v in char_lines])
  char_lines = [l + " " * (max_width - len(l)) for l in char_lines]
  pos = (min([idx for idx, val in enumerate(char_lines[0]) if val != " "]), 0)
  facing = RIGHT
  print_directions = {0 : ">", 1 : "v", 2 : "<", 3 : "^"}
  while instructions:
    #print("current pos", pos)
    next_arg = instructions.pop(0)
    if next_arg.isnumeric():
      while len(instructions) > 0 and instructions[0].isnumeric():
        next_arg = next_arg + instructions.pop(0)
      #print("moving", next_arg, "steps in direction", facing)
      for move_idx in range(int(next_arg)):
        #s = char_lines[pos[1]]
        #x = pos[1]
        #char_lines[pos[1]] = s[:x] + print_directions[facing] + (s[x + 1] if x < max_width else "")
        pos = move_to_next_location(pos, facing)
    else:
      facing = get_next_facing(facing=facing, turn=next_arg)

  #for l in char_lines:
  #  print(l)
  print("last pos", pos)
  print((pos[1] + 1) * 1000 + (pos[0] + 1) * 4 + facing)
  #pp.pprint(char_lines)