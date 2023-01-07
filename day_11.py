import input_reader as ir

monkeys = []

class Monkey():

    def __init__(self, id, items, op, divisible_by, monkey_true, monkey_false):
        self.id = id
        self.items = items
        self.operation = op
        self.divisible_by = divisible_by
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspection_times = 0

    def test_all_items_part1(self):
        while len(self.items) > 0:
            item = self.items.pop()
            self.inspection_times = self.inspection_times + 1
            arg1, operator, arg2 = self.operation.split()
            arg1 = item if arg1 == "old" else int(arg1)
            arg2 = item if arg2 == "old" else int(arg2)
            new_val = eval(str(arg1) + operator + str(arg2))
            new_val = int(new_val / 3)

            if new_val % self.divisible_by == 0:
                monkeys[self.monkey_true].items.append(new_val)
            else:
                monkeys[self.monkey_false].items.append(new_val)


    def test_all_items_part2(self):
        while len(self.items) > 0:
            item = self.items.pop()
            self.inspection_times = self.inspection_times + 1
            arg1, operator, arg2 = self.operation.split()
            arg1 = item if arg1 == "old" else int(arg1)
            arg2 = item if arg2 == "old" else int(arg2)
            new_val = eval(str(arg1) + operator + str(arg2))

            new_val = new_val % biggest_value
            if new_val % self.divisible_by == 0:
                monkeys[self.monkey_true].items.append(new_val)
            else:
                monkeys[self.monkey_false].items.append(new_val)


if __name__ == "__main__":
    monkey_inputs = [l.split("\n") for l in ir.get_with_separator("\n\n")]

    for m in monkey_inputs:
        monkey_id =  ir.get_with_regex_groups_int_cast(r"Monkey (\d+):", m[0])[0]
        items = m[1].split(":")[1].split(",")
        items = [int(x) for x in items]
        op = m[2].split(" = ")[1]
        divisible_by = int(m[3].split("divisible by ")[1])
        monkey_true = int(m[4].split("throw to monkey ")[1])
        monkey_false = int(m[5].split("throw to monkey ")[1])
        monkeys.append(Monkey(monkey_id, items, op, divisible_by, monkey_true, monkey_false))

    #part 1

    #part 2
    biggest_value = 1
    for monkey in monkeys:
        biggest_value = biggest_value * monkey.divisible_by
    print(biggest_value)
    for r in range(10000):
        for monkey in monkeys:
            monkey.test_all_items_part2()

        if r % 1000 == 0:
            print("after round ", r + 1)
            for monkey in monkeys:
                print("monkey ", monkey.id, monkey.inspection_times)
    s = sorted([monkey.inspection_times for monkey in monkeys])
    print(s[-1] * s[-2])
