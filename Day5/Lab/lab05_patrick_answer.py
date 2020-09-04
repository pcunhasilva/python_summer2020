import re
import os

# Set Directory
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day5/Lab')

# open text file of 2008 NH primary Obama speech
with open("obama-nh.txt", "r") as f:
    text = f.readlines()

## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

# compile the regular expression
keyword = re.compile(r"the\s")

# TODO: print all lines that DO NOT contain "the "
l = []
for line in text:
    if not keyword.search(line.lower()):
        print(line)
        l.append(line)
len(l)

# TODO: print lines that contain a word of any length starting with s and ending with e
allwords = re.findall(r"\bs\w*e\b", " ".join(str(x) for x in text))
l = []
for line in text:
    for i in range(len(allwords)):
        if allwords[i] in line.split():
            l.append(line)
            print(line)

# date = raw_input("Please enter a date in the format MM.DD.YY: ")
# Print the date input in the following format:
# Month: MM
# Day: DD
# Year: YY
mytest = "Please enter a date in the format MM.DD.YY: 08.14.19"
dateFormat = re.compile(r"(\d{2})\.(\d{2})\.(\d{2})")
l = dateFormat.search(mytest)
print("Month: {}\nDay: {}\nYear: {}".format(l.group(1), l.group(2), l.group(3)))
