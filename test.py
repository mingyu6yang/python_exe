import numpy as np

with open("data/non-code_file.txt","r") as f:
    data = f.readlines()
    res = 0
    for i in data:
        res += int(i)
    with open("res.txt", "w") as f:
        f.write(str(res))



