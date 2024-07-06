# Usage: python alpaca_to_sharegpt.py -f xxx.json -o yyy.json
# Please replace the target JSON file

import json
import argparse


def convert_to_sharegpt(input_file, output_file):
    # 读取原始 JSON 数据
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 转换成 ShareGPT 格式
    sharegpt_data = []

    for index, item in enumerate(data):
        conversation = []

        if item.get('instruction'):
            conversation.append({
                "from": "human",
                "value": item['instruction']
            })

        if item.get('input'):
            conversation.append({
                "from": "human",
                "value": item['input']
            })

        if item.get('output'):
            conversation.append({
                "from": "assistant",
                "value": item['output']
            })

        sharegpt_data.append({
            "id": str(index),
            "conversations": conversation
        })

    # 保存为 ShareGPT 格式的 JSON 文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sharegpt_data, f, ensure_ascii=False, indent=4)

    print(f"转换完成并保存为 {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to ShareGPT format.")
    parser.add_argument("-f", "--file", type=str, required=True, help="Path to the input med.json file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Path for the output ShareGPT JSON file")

    args = parser.parse_args()

    convert_to_sharegpt(args.file, args.output)