import sys

num_of_reviews = 0
correct_count = 0

file_name_ans = sys.argv[-2]
file_name_out = sys.argv[-1]

with open(file_name_ans, 'r') as ans, open(file_name_out, 'r') as output:
    for ans_line in ans:
        num_of_reviews += 1
        output_line = output.readline()
        if ans_line == output_line:
            correct_count += 1
ans.close()
output.close()

print(correct_count)
print(correct_count / num_of_reviews)
