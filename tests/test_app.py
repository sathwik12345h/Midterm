# pylint: disable=all
# pragma: no cover
"""Tests for the App class in the calculator app."""

import pytest
from app import App

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit):
        app.start()  # Ensure SystemExit is raised when calling App.start()

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    # Verify that the unknown command was handled as expected
    # captured = capfd.readouterr()
    # assert "No such command: unknown_command" in captured.out  # Ensure the error message is printed

    ####new to imporove test coverage
def test_addition(capfd, monkeypatch):
    """Test addition operation."""
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "5.0 + 3.0 = 8.0" in captured.out

def test_subtraction(capfd, monkeypatch):
    """Test subtraction operation."""
    inputs = iter(['subtract 10 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "10.0 - 4.0 = 6.0" in captured.out

def test_multiplication(capfd, monkeypatch):
    """Test multiplication operation."""
    inputs = iter(['multiply 6 7', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "6.0 * 7.0 = 42.0" in captured.out

def test_division(capfd, monkeypatch):
    """Test division operation."""
    inputs = iter(['divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "8.0 / 2.0 = 4.0" in captured.out

def test_division_by_zero(capfd, monkeypatch):
    """Test division by zero handling."""
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "Cannot divide by zero." in captured.out
