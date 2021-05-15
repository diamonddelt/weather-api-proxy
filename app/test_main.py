import pytest
from flask import Flask, request
import main

def test_example_method():
    a = 1
    b = 2
    assert a + 1 == b, f"Test Failed: {a} + 1 != {b}"

# Positive API Tests

def test_debug():
    assert main.debug() == "<p>Hello, World!</p>"

def test_health_check():
    assert main.health_check() == {"status": "ok"}

