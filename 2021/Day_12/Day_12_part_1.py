import numpy as np

path = './input_day12'


class Navigation:
    def __init__(self, file_path):
        with open(file_path, 'r') as f:
            self.data = np.array([line.strip().split('-') for line in f.readlines()])

        uniques = list(np.unique(self.data))
        uniques.remove('start')
        uniques.remove('end')
        uniques.insert(0, 'start')
        uniques.insert(len(uniques), 'end')
        self.uniques = uniques
        self.encounter_dict = self.encounter_dictionary()

    def encounter_dictionary(self):
        nearby_dict = {}
        for item in self.uniques:
            temp_list = []
            points = np.where(self.data == item)
            for idx, y in enumerate(points[1]):
                temp_list.append(self.data[points[0][idx], abs(y - 1)])

            nearby_dict[item] = temp_list
        return nearby_dict

    def find_all_paths(self, start='start', end='end', path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.encounter_dict[start]:
            if node.isupper() or node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


te = Navigation(path)
path_lists = te.find_all_paths()
print(len(path_lists))
