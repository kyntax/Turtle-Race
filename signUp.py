file_name = 'userdata.txt'
non_blank_count = 0
with open(file_name) as f:
    for line in f:
        if line.strip():
            non_blank_count += 1
print(non_blank_count)