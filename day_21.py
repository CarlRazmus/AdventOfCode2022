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

#def reduce_monkeys(monkeys):
#    reduced = True
#    reduced_monkeys = dict(monkeys)
#    while reduced:
#        reduced = False
#        for name, monkey in monkeys.items():
#            if monkey.value is not None:
#                continue
#            if name == "humn":
#                continue
#            left = monkeys[monkey.left_operand].value
#            right = monkeys[monkey.right_operand].value
#            if left is not None and right is not None:
#                reduced = True
#                monkey.value = monkey.shout()
#                reduced_monkeys.pop(monkey.left_operand)
#                reduced_monkeys.pop(monkey.right_operand)
#        monkeys = dict(reduced_monkeys)
#    return reduced_monkeys

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
    start_val = monkeys["humn"].value
    original_left, original_right = monkeys["root"].shout()
    original_diff = abs(original_right - original_left)

    #find scaling constant
    monkeys["humn"].value = start_val + 1
    left, right = monkeys["root"].shout()
    diff = abs(left - right)
    print("diff", diff)
    print(original_diff - diff)
    scaling_factor = int(original_diff / int((original_diff - diff)))
    print("scaling_factor", scaling_factor)

    #try to set it to a reasonable value since the scaling is constant
    monkeys["humn"].value = start_val + scaling_factor

    previous_diff = 0
    while True:
        monkeys["humn"].value = monkeys["humn"].value - 1
        left, right = monkeys["root"].shout()
        #print("left", left, "right", right)
        diff = abs(left - right)
        print(diff)
        if left == right:
            break
        print("diff from last iteration", previous_diff - diff)
        previous_diff = diff

    print(monkeys["humn"].value)
