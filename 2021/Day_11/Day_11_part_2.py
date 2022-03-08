import numpy as np

path = './input_day11'


class NavigateWithOctopuses:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            data = [list(line.strip()) for line in f.readlines()]

        self.data = np.array(data).astype(int)

    def moving(self):
        step = 1
        switch = True
        while switch:
            max_oct = []

            self.data = self.take_step()
            max_oct += self.find_lights()

            self.find_adjacent_flashes(max_oct)

            if self.find_lights():
                coors = self.find_lights(True)
                self.data[coors] = 0
                if len(coors[0]) == self.data.shape[0]*self.data.shape[1]:
                    return step

            step += 1

    def take_step(self):
        return self.data + 1

    def find_lights(self, coors=False):
        if any(np.unique(self.data) > 9) and not coors:
            coors = np.where(self.data > 9)
            return [tuple([a, b]) for a, b in zip(coors[0], coors[1])]
        elif coors:
            return np.where(self.data > 9)
        else:
            return []

    def find_adjacent(self, x, y):
        adjacent = []
        if x > 0:
            adjacent.append((x - 1, y))
        if x < self.data.shape[0] - 1:
            adjacent.append((x + 1, y))
        if y > 0:
            adjacent.append((x, y - 1))
        if y < self.data.shape[1] - 1:
            adjacent.append((x, y + 1))
        if x > 0 and y > 0:
            adjacent.append((x - 1, y - 1))
        if x > 0 and y < self.data.shape[1] - 1:
            adjacent.append((x - 1, y + 1))
        if x < self.data.shape[0] - 1 and y > 0:
            adjacent.append((x + 1, y - 1))
        if x < self.data.shape[0] - 1 and y < self.data.shape[1] - 1:
            adjacent.append((x + 1, y + 1))

        if adjacent:
            x = np.array([item[0] for item in adjacent])
            y = np.array([item[1] for item in adjacent])
            adjacent = (x, y)

        return adjacent

    def find_adjacent_flashes(self, max_octopuses):
        max_octopuses_checked = []
        while len(max_octopuses) != 0:
            max_octopuses = list(set(max_octopuses) - set(max_octopuses_checked))
            if not max_octopuses:
                break
            if max_octopuses[0] not in max_octopuses_checked:
                (x, y) = max_octopuses[0]
            else:
                max_octopuses.pop(0)
                continue
            nearby = self.find_adjacent(x, y)
            self.data[nearby] += 1
            max_octopuses += self.find_lights()
            # for item in nearby:
            #     self.data[item[0], item[1]] += 1
            #     if self.data[item[0], item[1]] > 9 and (item[0], item[1]) not in max_octopuses_checked:
            #         max_octopuses.append((item[0], item[1]))
            max_octopuses_checked.append(max_octopuses.pop(0))


te = NavigateWithOctopuses(path)
flashes = te.moving()
print(flashes)
