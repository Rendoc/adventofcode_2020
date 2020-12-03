
class Password:
    def __init__(self, pw, letter, lower, upper):
        self.pw = pw
        self.letter = letter
        self.lower = int(lower)
        self.upper = int(upper)
    
    def isValid(self):
        return self.lower <= self.pw.count(self.letter) and self.pw.count(self.letter) <= self.upper
    
    def isValid_part2(self):
        pos1 = self.lower - 1
        pos2 = self.upper - 1

        return (self.pw[pos1]==self.letter) ^ (self.pw[pos2]==self.letter)

def convert(line):
    a, b = line.split(":")
    password = b.strip()
    interval, letter = a.split(" ")
    lower, upper = interval.split("-")
    return Password(password, letter, lower, upper)

def test():
    test_1 = "1-3 a: abcde"
    test_2 = "1-3 b: cdefg"
    test_3 = "2-9 c: ccccccccc"
    count = 0
    for i in [test_1, test_2, test_3]:
        if convert(i).isValid():
            count += 1
    return count

def part_1():
    count = 0
    with open('input_day2_part2.txt', 'r') as r:
        for line in r.readlines():
            if convert(line).isValid():
                count += 1
    return count

def part_2():
    count = 0
    with open('input_day2_part2.txt', 'r') as r:
        for line in r.readlines():
            if convert(line).isValid_part2():
                count += 1
    return count

if __name__ == "__main__":
    print(test())
    print(part_1())
    print(part_2())


    