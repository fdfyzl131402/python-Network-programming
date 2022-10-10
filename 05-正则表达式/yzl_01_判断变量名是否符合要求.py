import re

index_names = ["yzl_01_good", "abcd_0214_better", "hhhhhh_0_no", "where_055beautiful"]

for name in index_names:

    req = re.match(r"[a-z]{2,5}_?\d{1,3}_?[a-z]{2,8}$", name)
    # match 可以自动判断开头但是不能判断结尾
    # 如果在正则表达式中出现了普通字符如. ？等等，仅仅只需要在前面加一个反斜杠进行转义

    if req:
        print("变量%s 符合条件" % req.group())

    else:
        print("变量%s 非法" % name)

