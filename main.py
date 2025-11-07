# -*- coding: utf-8 -*-
# 在此文件处编辑代码
def analyze_text(text):
    # 统计字符出现频率（仅字母，区分大小写）
    char_count = {}
    for char in text:
        if char.isalpha():  # 仅统计字母
            char_count[char] = char_count.get(char, 0) + 1
    
    # 按频率降序排序，频率相同则按字符升序排列
    sorted_chars = sorted(char_count.keys(), key=lambda x: (-char_count[x], x))
    return sorted_chars

# 主程序，已完整
if __name__ == "__main__":
    print("文本字符频率分析器")
    print("================")
    print("请输入一段文本（输入空行结束）:")

    # 读取多行输入
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break

    # 合并输入文本
    text = "\n".join(lines)

    if not text.strip():
        print("未输入有效文本！")
    else:
        # 分析文本
        sorted_chars = analyze_text(text)

        # 打印结果
        print("\n字符频率降序排列:")
        print(", ".join(sorted_chars))

        # 提示用户比较不同语言
        print("\n提示：尝试输入中英文文本，观察字符频率差异~")
