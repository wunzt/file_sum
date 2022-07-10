# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 7/10/2022
# Description: Reads a text file that contains a list of numbers, sums them, and writes the sum to a new .txt file.

def file_sum(nums):
    """Takes as a parameter a text file that contains a list of numbers one to a line, sums them, and writes the sum
    to a new file, sum.txt."""

    sum = 0

    with open(nums, "r") as infile:
        for line in infile:
            sum += float(line)
            print(sum)

    with open("sum.txt", "w") as outfile:
        outfile.write(str(sum))