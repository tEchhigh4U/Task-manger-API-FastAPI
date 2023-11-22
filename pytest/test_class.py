class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert not hasattr(x, "check")

    def test_three(self):
        x = "hello"
        assert getattr(x, "check", None) is None
    
    def test_four(self):
        x = "hello"
        assert hasattr(x, "check") is False
    
    def test_five(self):
        x = "hello"
        try:
            assert not hasattr(x, "check")
        except AttributeError:
            pass