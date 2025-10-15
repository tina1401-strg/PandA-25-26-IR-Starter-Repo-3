# Acceptance test: transcript as executable spec for Part 2
import io, sys, builtins
from pathlib import Path

# Import the app as a module
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from part2 import app  # type: ignore

def run_with_inputs(inputs):
    it = iter(inputs)
    out = io.StringIO()
    def fake_input(prompt=""):
        print(prompt, end="", file=out)
        try:
            return next(it)
        except StopIteration:
            raise EOFError
    old_stdout = sys.stdout
    old_input = builtins.input
    sys.stdout = out
    try:
        builtins.input = fake_input  # monkeypatch input
        app.main()
    finally:
        builtins.input = old_input
        sys.stdout = old_stdout
    return out.getvalue()

def normalize(s: str) -> str:
    # Normalize newlines and strip trailing spaces on each line
    return "\n".join(line.rstrip() for line in s.replace("\r\n", "\n").replace("\r", "\n").split("\n"))

def test_interaction_snapshot():
    inputs = [
        ":help",
        "love",
        ":highlight off",
        "love",
        ":quit",
    ]
    got = normalize(run_with_inputs(inputs))
    expected = normalize(Path(__file__).with_name("snapshot_interaction.txt").read_text(encoding="utf-8"))
    assert got == expected, "Transcript does not match expected snapshot.\n\nGOT:\n" + got
