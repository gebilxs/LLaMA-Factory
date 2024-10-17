import json
import random
import argparse
import sys

def split_dataset(input_file, train_file, test_file, train_ratio=0.9):
    try:
        # 读取JSON文件
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 计算训练集大小
        train_size = int(len(data) * train_ratio)
        
        # 随机打乱数据
        random.shuffle(data)
        
        # 分割数据
        train_data = data[:train_size]
        test_data = data[train_size:]
        
        # 保存训练集
        with open(train_file, 'w', encoding='utf-8') as f:
            json.dump(train_data, f, ensure_ascii=False, indent=2)
        
        # 保存测试集
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, ensure_ascii=False, indent=2)
        
        print(f"总数据量: {len(data)}")
        print(f"训练集数量: {len(train_data)}")
        print(f"测试集数量: {len(test_data)}")
        print(f"训练集已保存到: {train_file}")
        print(f"测试集已保存到: {test_file}")

    except FileNotFoundError:
        print(f"错误: 找不到文件 '{input_file}'")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"错误: '{input_file}' 不是有效的JSON文件")
        sys.exit(1)
    except Exception as e:
        print(f"发生错误: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="将JSON数据集分割为训练集和测试集")
    parser.add_argument("input_file", help="输入的JSON文件路径")
    parser.add_argument("--train", default="data/finance_train_set.json", help="训练集输出文件名 (默认: train_set.json)")
    parser.add_argument("--test", default="data/finance_test_set.json", help="测试集输出文件名 (默认: test_set.json)")
    parser.add_argument("--ratio", type=float, default=0.9, help="训练集比例 (默认: 0.9)")

    args = parser.parse_args()

    split_dataset(args.input_file, args.train, args.test, args.ratio)

if __name__ == "__main__":
    main()