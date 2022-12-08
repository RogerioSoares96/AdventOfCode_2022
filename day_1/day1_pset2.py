calories_data = open("day1_input.txt", "r").readlines()
elfs_list = []
elf_calories = 0
for line in calories_data:
    if line.strip():
        elf_calories += int(line)
    else:
        elfs_list.append(elf_calories)
        elf_calories = 0
elfs_list.sort()
print(elfs_list[len(elfs_list) - 1] + elfs_list[len(elfs_list) - 2] + elfs_list[len(elfs_list) - 3])