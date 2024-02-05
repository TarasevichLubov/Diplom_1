class TestBun:
    def test_name_of_bun_true(self, bun):
        assert bun.get_name() == "Слойка"

    def test_price_of_bun_true(self, bun):
        assert bun.get_price() == 20.01
