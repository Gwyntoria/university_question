import os
import subprocess
from pathlib import Path

book_title = "王烁·大学·问"
book_author = "王烁"

def create_epub():
    # 设置输入和输出路径
    input_dir = Path("../md")
    output_file = f"{book_title}.epub"
    cover_image = Path("../assets/cover.jpg")  # 添加封面图片路径
    
    # 确保输入目录是绝对路径
    input_dir = input_dir.resolve()
    cover_image = cover_image.resolve()  # 转换封面路径为绝对路径
    print(f"Input directory: {input_dir}")
    print(f"Cover image path: {cover_image}")  # 打印封面路径
    
    # 按照特定顺序排列文件
    file_order = [
        "0.发刊辞.md",
        "1.耶鲁故事.md",
        "2.极简金融课.md",
        "3.极简谈判课.md",
        "4.财智逻辑.md",
        "5.在美国看美国.md",
        "6.问答.md",
    ]
    
    # 检查所有文件是否存在，并打印详细信息
    missing_files = []
    for file in file_order:
        file_path = input_dir / file
        print(f"Checking file: {file_path}")
        if not file_path.exists():
            print(f"warning: file {file_path} does not exist")
            missing_files.append(file)
        else:
            print(f"Found file: {file_path}")
    
    if missing_files:
        print(f"The following files are missing: {missing_files}")
        return

    # 构建输入文件列表
    input_files = [str(input_dir / filename) for filename in file_order]

    # 构建pandoc命令
    command = [
        "pandoc",
        "--from=markdown",
        "--to=epub",
        "-o",
        output_file,
        "--toc",  # 添加目录
        "--toc-depth=2",
        "--epub-chapter-level=2",
        "--metadata", f"title={book_title}",
        "--metadata", f"author={book_author}",
    ]

    # 如果封面图片存在，添加到命令中
    if cover_image.exists():
        command.extend(["--epub-cover-image", str(cover_image)])
    else:
        print(f"警告：封面图片 {cover_image} 不存在")
    
    command.extend(input_files)

    # 打印完整的命令以便调试
    print("Executing command:")
    print(" ".join(command))

    try:
        # 执行转换，并捕获输出
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print("Pandoc stdout:", result.stdout)
        print("Pandoc stderr:", result.stderr)
        
        epub_path = f"../epub/{output_file}"
        if os.path.exists(epub_path):
            os.remove(epub_path)
        os.rename(output_file, os.path.join("../epub", output_file))
        
        print(f"成功创建EPUB文件: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"转换过程中发生错误：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")


if __name__ == "__main__":
    create_epub()
