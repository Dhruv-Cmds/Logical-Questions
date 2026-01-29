# Author: Dhruv

# Given a file server.log:
# Extract only lines that contain "ERROR"
# Write them into a new file errors.txt
# Also print:
# total lines in file
# total error lines

def errors():

    total_errors_line = 0
    total_lines = 0
    errors_lines = []

    with open("s_erver.log" , "r") as f:

        for i in f:
            total_lines += 1

            if "ERROR" in i:
                total_errors_line += 1
                errors_lines.append(i)

    with open("s_errors.txt" , "w") as f:

        for i in errors_lines:
            f.write(i)

    print(f"Total error lines are :{total_errors_line}")
    print(f"Total lines area :{total_lines}")

errors()