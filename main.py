# -*- coding: utf-8 -*-
def analyze_text(text, include_all_chars=False):
    """
    分析文本字符频率，按频率降序、字符升序排列
    :param text: 输入文本
    :param include_all_chars: 是否统计所有字符（默认仅统计字母）
    :return: 排序后的字符列表
    """
    char_count = {}
    for char in text:
        # 根据参数决定统计范围
        if include_all_chars or char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # 按频率降序、字符本身升序排序
    sorted_chars = sorted(char_count, key=lambda x: (-char_count[x], x))
    return sorted_chars

if __name__ == "__main__":
    print("===== 文本字符频率分析器 =====")
    # 读取输入（兼容多行/单行，空行结束）
    print("请输入文本（输入空行结束）:")
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except (EOFError, KeyboardInterrupt):
            break  # 捕获异常，避免程序崩溃
    
    # 处理输入
    text = "\n".join(lines).strip()
    if not text:
        print("错误：未输入有效文本！")
    else:
        # 调用分析函数（默认仅统计字母，可修改为 include_all_chars=True 统计所有字符）
        result = analyze_text(text)
        
        # 输出结果
        print("\n===== 分析结果 =====")
        if not result:
            print("未检测到有效字符！")
        else:
            print(f"字符按频率降序排列：\n{', '.join(result)}")
