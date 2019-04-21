# Read from the file file.txt and output all valid phone numbers to stdout.

# 注意""不要丢了，其中的空格，()是普通字符，" "不要丢了
# ^：表示行首，以...开始，这里表示以(xxx) 或者xxx-开始，注意空格
# ()：选择操作符，要么是([0-9]\{3\}) ，要么是[0-9]\{3\}-
# |：或者连接操作符，表示或者
# []：单字符占位，[0-9]表示一位数字
# {n}：匹配n位，[0-9]\{3\}匹配三位连续数字
# $：表示行尾，结束

grep "^\(([0-9]\{3\}) \|[0-9]\{3\}-\)[0-9]\{3\}-[0-9]\{4\}$" file.txt
