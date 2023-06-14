import re

file_path = "main.py"


def find_unused_functions(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    defined_functions = set()
    called_functions = set()

    for line_num, line in enumerate(lines, start=1):
        pattern = re.compile("def .*\(.*\):")
        match = pattern.search(line)

        if match is not None:
            words = line.strip().split()
            for word_num, word in enumerate(words, start=1):
                if word == "def":
                    funcName = words[word_num].split("(")[0]
                    if funcName != "main":
                        defined_functions.add(funcName)
                break

        pattern = re.compile("\w+\(.*\)[^:]")
        match = pattern.search(line)
        if match is not None:
            called_func = match.group(0).split("(")[0]
            called_functions.add(called_func)

    for called_func in called_functions:
        if called_func in defined_functions:
            defined_functions.remove(called_func)

    return defined_functions


unused_funcs = find_unused_functions(file_path)


def remove_unused_functions(file_path, unused_funcs):
    with open(file_path, "r") as file:
        lines = file.readlines()

    lines_to_delete = set()

    for line_num in range(len(lines)):
        line = lines[line_num]
        for func in unused_funcs:
            pattern = re.compile("def " + func + "\(.*\)\:")
            match = pattern.search(line)
            if match is not None:
                lines_to_delete.add(line_num)

                func_def_line = line_num + 1
                while lines[func_def_line][0] == " ":
                    lines_to_delete.add(func_def_line)
                    func_def_line += 1

    with open(file_path, "w") as file:
        for line_num, line in enumerate(lines):
            if not lines_to_delete.__contains__(line_num):
                file.writelines(line)


remove_unused_functions(file_path, unused_funcs)
