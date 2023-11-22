import pytest
import re

def f():
    return 4

# Pytest支持显示最常用的子表达式的值，包括调用、属性、比较以及二进制和一元操作符。这允许您在不使用样板代码的情况下使用惯用的python构造，同时不丢失内省信息。

# 如果您使用这样的断言指定消息,根本不会发生任何断言内省，消息将简单地显示在回溯中.
def test_function():
    a = f()
    assert a % 2 == 0, "value was odd, should be even"

# 可以使用pytest.raises來引發異常斷言
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

# 需要訪問實際的異常信息
def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert "maximum recursion" in str(excinfo.value)
    # excinfo 是一個ExceptionInfo的實例，它包含有關異常的信息
    # excinfo.type：異常類型
    # excinfo.value：異常實例
    # excinfo.traceback：異常的回溯

# 可以向上下文管理器傳遞一個match參數，以便檢查異常的字符串表示形式是否匹配（類似unittest中的 TestCase.assertRaisesRegex）。
def my_function():
    raise ValueError("Exception 123 raised")

def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        my_function()
    
def test_match_2():
    with pytest.raises(ValueError) as excinfo:
        my_function()
    assert excinfo.match(r".* 123 .*")

def test_match_3():
    with pytest.raises(ValueError) as excinfo:
        my_function()
    
    err_msg = str(excinfo.value)
    print(err_msg)
    assert re.search(r".* 123 .*", err_msg) is not None