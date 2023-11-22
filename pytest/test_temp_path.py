# pytest提供内置​fixture /function​参数来请求任意资源
# 在测试函数签名中列出名称​tmp_path​, pytest将在执行测试函数调用之前查找并调用一个​fixture​工厂来创建资源。
# 在运行测试之前，pytest会创建一个每个测试调用唯一的临时目录，并将其作为​tmp_path​参数传递给测试函数。

def test_needs_files(temp_path):
    print(temp_path)
    assert 0

#  通过下面的命令来了解内置pytest fixture的类型
# $ pytest -q test_temp_path.py 