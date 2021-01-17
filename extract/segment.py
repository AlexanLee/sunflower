# -*-coding:utf-8-*-
import jieba
import os
import re


def segment(in_path, out_path):
    path_dir = os.listdir(in_path)
    for all_dir in path_dir:
        child = os.path.join(in_path, all_dir)
        if os.path.isfile(child):
            segment_person(child, out_path)
            continue
        segment(child)


def segment_person(in_path, out_path):
    with open(in_path) as f:
        lines = f.readlines()
        pattern = re.compile(r'\d+\d*')
        index = ''.join(pattern.findall(f.name))
        out_lines = []
        jieba.load_userdict('../data/dict.txt')
        for line in lines:
            seg_list = jieba.cut(line, cut_all=False)
            out_lines.append('|'.join(seg_list))
            # out_lines += '\n'
            # print('|'.join(seg_list))
        with open(out_path + index + '.txt', 'wb') as fout:
            fout.write(''.join(out_lines).encode())


if __name__ == '__main__':
    print('segment')
    segment('../data/sjz/clean/', out_path='../data/sjz/segment/')
