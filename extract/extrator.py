# -*-coding:utf-8-*-
import os
import re

SJZ = '0311'


def each_file(in_path, out_path):
    path_dir = os.listdir(in_path)
    for all_dir in path_dir:
        child = os.path.join(in_path, all_dir)
        if os.path.isfile(child):
            unique_person(child, out_path)
            continue
        each_file(child)


def unique_person(in_path, out_path):
    with open(in_path) as f:
        pattern = re.compile(r'\d+\d*')
        index = ''.join(pattern.findall(f.name))
        print(index)
        lines = f.readlines()
        out_lines = []
        for line in lines:
            if "确诊病例" in line[:10]:
                line = line.replace("确诊病例", SJZ + index, 1)
                out_lines.append(line)

        with open(out_path + index + '.txt', 'wb') as fout:
            fout.write(''.join(out_lines).encode())


if __name__ == '__main__':
    print('main')
    each_file('../data/sjz/text/', '../data/sjz/clean/')
