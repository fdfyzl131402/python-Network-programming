import re
with open("拉沟", "r") as f:
    content = f.read()

    ret = re.sub(r"<[a-z]*>|</[a-z]*>|\n", "", content)
    print(ret.lstrip())
