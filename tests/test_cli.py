from portfolio.cli import main


def test_main_add(capsys):
    assert main(["add", "2", "3"]) == 0
    captured = capsys.readouterr()
    assert captured.out.strip().endswith("5.0")
