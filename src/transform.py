from pathlib import Path
from epub_converter import EpubConverter

book_title = "王烁·大学·问"
book_author = "王烁"

def create_epub():
    # 设置文件顺序
    file_order = [
        "0.发刊辞.md",
        "1.耶鲁故事.md",
        "2.极简金融课.md",
        "3.极简谈判课.md",
        "4.财智逻辑.md",
        "5.在美国看美国.md",
        "6.问答.md",
    ]
    
    # 创建转换器实例
    converter = EpubConverter(
        book_title=book_title,
        book_author=book_author,
        input_dir="../md",
        output_dir="../epub",
        file_order=file_order,
        cover_image_path="../assets/cover.jpg"
    )
    
    # 执行转换
    converter.create_epub()

if __name__ == "__main__":
    create_epub()
