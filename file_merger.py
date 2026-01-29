# Author: Dhruv

# File Merger Tool (Real-world)
# Given:
# a.txt
# b.txt 
# c.txt
# Write a program to: 
# Merge all into final.txt
# Add header before each file:
# --- a.txt --- content... 
# --- b.txt --- content...    
# Also print:
# total characters merged 
# total lines merged 


def merge():
    total_characters_merged = 0
    total_lines_merged = 0

    with open ("a.txt" , "r") as f:
        content = f.read()
        total_characters_merged += len(content)
        total_lines_merged += content.count("\n")

    with open ("b.txt" , "r") as f:
        content1 = f.read()
        total_characters_merged += len(content1)
        total_lines_merged += content1.count("\n")

    with open ("c.txt" , "r") as f:
        content2 = f.read()
        total_characters_merged += len(content2)
        total_lines_merged += content2.count("\n")

    merge_content = content + content1 + content2

    with open ("s_final.txt" , "w") as f:
        f.write(merge_content)

        print("Total characters are merged :" , total_characters_merged)
        print("Total lines merged:", total_lines_merged)

merge()
4