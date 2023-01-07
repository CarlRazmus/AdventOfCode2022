import input_reader as ir

class Monkey:

    def __init__(self, value = None, left_operand = None, operator = None, right_operand = None) -> None:
        self.value = value
        self.left_operand = left_operand
        self.operator = operator
        self.right_operand = right_operand

    def shout(self):
        if self.value is not None:
            return self.value
        if self.operator == "+":
            return monkeys[self.left_operand].shout() + monkeys[self.right_operand].shout()
        if self.operator == "-":
            return monkeys[self.left_operand].shout() - monkeys[self.right_operand].shout()
        if self.operator == "*":
            return monkeys[self.left_operand].shout() * monkeys[self.right_operand].shout()
        if self.operator == "/":
            return monkeys[self.left_operand].shout() / monkeys[self.right_operand].shout()
        if self.operator == "=":
            val1 = monkeys[self.left_operand].shout()
            val2 = monkeys[self.right_operand].shout()
            return (val1, val2)

if __name__ == "__main__":
    monkey_inputs = ir.read_input_lines()
    monkeys = {}
    for monkey_line in monkey_inputs:
        parts = monkey_line.split()
        if len(parts) == 2:
            monkeys[parts[0].strip(":")] = Monkey(value=int(parts[1]))
        else:
            monkeys[parts[0].strip(":")] = Monkey(left_operand=parts[1], operator=parts[2], right_operand=parts[3])

    #part1
    print("part1", monkeys["root"].shout())

    #part 2
    monkeys["root"].operator = "="
    while True:
        original_left, original_right = monkeys["root"].shout()
        original_diff = abs(original_right - original_left)

        #find scaling constant
        start_val = monkeys["humn"].value
        monkeys["humn"].value = start_val + 1
        left, right = monkeys["root"].shout()
        diff = abs(left - right)
        print("diff", diff)
        print(original_diff - diff)
        scaling_factor = int(diff  / (original_diff - diff))
        print("scaling_factor", scaling_factor)

        #try to set it to a reasonable value since the scaling is ~constant
        monkeys["humn"].value = start_val + scaling_factor

        #verify if estimation is close enough to desired shout value
        left, right = monkeys["root"].shout()
        diff = abs(left - right)
        print("current diff ", diff, "\n")
        if abs(left - right) == 0:
            print(monkeys["humn"].value)
            break

    print(monkeys["humn"].value)
