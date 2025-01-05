# epub_maker

创建这个仓库的起因是，我在得到上重读王烁老师的专栏《王烁·大学·问》时发现，专栏中的一些文章并没有被收录在《在耶鲁精进》之中。

恰巧最近在学习 epub 制作，索性就拿王烁老师的这个专栏来练习。

王烁老师的文章常读常新，在此推荐，有能力的可移步得到，付费支持。

## 使用方法

`transform.py` 脚本依赖[pandoc](https://pandoc.org/)工具实现将 Markdown 文件转换为 EPUB 文件。所以使用脚本前，需要先安装 pandoc。

Windows 可以直接访问官网下载安装，Mac 中可以使用 Homebrew 安装，详见官网指南。

`transform.py` 脚本最后测试成功的 pandoc 版本为 v3.6.1。

## 补充说明

1. 由于 pandoc 对 LaTex 的转换存在错误，所以文本中原先由 LaTex 编写的公式，现在被转换为 JPG。
2. 启用 `metadata.yaml` 文件对生成的 EPUB 文件的 metadata 进行设定，而非原先脚本内部设定的默认指令。
3. `metadata.yaml` 中的关键字`lang`指定了 EPUB 的语言格式，在 pandoc 执行时，如果出现缺失 `translations/zh.yaml` 的 warning，可以不做关注，转换好的 EPUB 的 metadata 中依然会被设定为中文。如果需要消除 warning，可以在 [pandoc GitHub](https://github.com/jgm/pandoc/tree/main/data/translations) 下载相关文件，并放入 pandoc 的 User data directory。Mac 环境下执行`pandoc --version`即可看到默认指定目录，如目录不存在，自建即可。
