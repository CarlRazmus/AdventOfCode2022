import input_reader as ir


def find_unique_set(desired_len):
    for idx in range (len(chars) - desired_len):
        charset = set(chars[idx:idx+desired_len])
        if len(charset) == desired_len:
            print(idx + desired_len)
            break

if __name__ == "__main__":
    chars = ir.read_input()
    find_unique_set(4)
    find_unique_set(14)
