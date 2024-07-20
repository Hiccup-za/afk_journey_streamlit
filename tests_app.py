from streamlit.testing.v1 import AppTest
import pytest

@pytest.fixture
def app_test():
    return AppTest.from_file("app.py")

def test_empty_input(app_test):
    at = app_test.run()
    at.button[0].click().run()
    assert at.error[0].value == "Question cannot be empty."

def test_short_input(app_test):
    at = app_test.run()
    at.text_input[0].input("one_word").run()
    at.button[0].click().run()
    assert at.error[0].value == "Please enter at least two words."

def test_no_question_found(app_test):
    at = app_test.run()
    at.text_input[0].input("one two three").run()
    at.button[0].click().run()
    assert at.error[0].value == "No matching question found."

def test_true_question(app_test):
    at = app_test.run()
    at.text_input[0].input("Arden is one").run()
    at.button[0].click().run()
    assert at.markdown[0].value == "**Question:** Arden is one of the Three Sages in the Dark Forest."
    assert at.markdown[1].value == "**Answer:** :green[True]"

def test_false_question(app_test):
    at = app_test.run()
    at.text_input[0].input("Atalanta is a").run()
    at.button[0].click().run()
    assert at.markdown[0].value == "**Question:** Atalanta is a notorious thief."
    assert at.markdown[1].value == "**Answer:** :red[False]"