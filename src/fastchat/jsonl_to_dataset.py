from datasets import load_dataset, DatasetDict


def parse(train_jsonl_file_path, test_jsonl_file_path, output_dir):
    # 加载 JSONL 文件为数据集
    dataset = load_dataset(
        'json',
        data_files={'train': train_jsonl_file_path, 'test': test_jsonl_file_path}
    )

    # 打印一些数据以检查是否加载成功
    print(dataset)

    # 保存数据集到本地磁盘
    dataset.save_to_disk(output_dir)
    print(f"Dataset saved to {output_dir}")


if __name__ == "__main__":
    train_jsonl_file_path = 'train.jsonl'  # 替换为你的 train JSONL 文件路径
    test_jsonl_file_path = 'test.jsonl'  # 替换为你的 test JSONL 文件路径
    output_dir = './dataset'  # 替换为你想要保存数据集的目录

    parse(train_jsonl_file_path, test_jsonl_file_path, output_dir)