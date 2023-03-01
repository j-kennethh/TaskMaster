from project import create, update, delete


def test_create(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "wash the dishes")
    data, i = create([], 0)
    assert data == [{"ID": 1, "Task": "wash the dishes"}] and i == 1


def test_update(monkeypatch):
    inputs = iter(["1", "do the laundry"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    data = update([{"ID": 1, "Task": "wash the dishes"}])
    assert data == [{"ID": 1, "Task": "do the laundry"}]


def test_delete(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    data = delete([{"ID": 1, "Task": "do the laundry"}])
    assert data == []