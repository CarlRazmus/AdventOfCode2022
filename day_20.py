import input_reader as ir

def encrypt(original_file, encrypted_file):
    encrypted_file_length = len(encrypted_file)
    for original_idx, original_steps in original_file:
        encrypted_idx = encrypted_file.index((original_idx, original_steps))
        steps = original_steps % (encrypted_file_length - 1)
        encrypted_file = encrypted_file[encrypted_idx + 1:] + encrypted_file[0 : encrypted_idx]
        encrypted_file.insert(steps, (original_idx, original_steps))
    return encrypted_file

def calc_sum(encrypted_file):
    encrypted_file_length = len(encrypted_file)
    for idx, t in enumerate(encrypted_file):
        if t[1] == 0:
            break
    idx1 = (idx + 1000) % encrypted_file_length
    idx2 = (idx + 2000) % encrypted_file_length
    idx3 = (idx + 3000) % encrypted_file_length
    return sum([encrypted_file[idx1][1], encrypted_file[idx2][1], encrypted_file[idx3][1]])

if __name__ == "__main__":
    part1_input = list(enumerate(ir.get_lines_as_int()))
    part2_input = [(idx, val * 811589153) for idx, val in part1_input]
    part_1_encrypted = encrypt(part1_input, list(part1_input))
    part_2_encrypted = list(part2_input)
    for _ in range(10):
        part_2_encrypted = encrypt(part2_input, part_2_encrypted)
    print("part 1", calc_sum(part_1_encrypted))
    print("part 2", calc_sum(part_2_encrypted))
