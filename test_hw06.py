import pytest
import hw06_main
from unittest.mock import patch



# Globals
st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]


# Part 1
# ===========
def test_1_1_get_letter_more_than_one_character(capsys, monkeypatch):
    with patch('builtins.input', side_effect=["ABC", "A"]) as mock_input:
        result = hw06_main.get_letter()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: it needs to be a single character."
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_1_2_get_letter_more_than_one_character_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["ABC", "BCA", "A"]) as mock_input:
        result = hw06_main.get_letter()
    hint2 = f"\n\n *** Did your loop break after a successful symbol was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 3, hint2


def test_1_3_get_letter_wrong_character(capsys, monkeypatch):
    with patch('builtins.input', side_effect=["@", "A"]) as mock_input:
        result = hw06_main.get_letter()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: You provided the wrong character."
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_1_4_get_letter_wrong_character_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["@", "F", "A"]) as mock_input:
        result = hw06_main.get_letter()
    hint2 = f"\n\n *** Did your loop break after a successful symbol was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 3, hint2



# Part 2
# ===========
def test_1_5_get_digit_more_than_one_digit(capsys, monkeypatch):
    with patch('builtins.input', side_effect=["123", "1"]) as mock_input:
        result = hw06_main.get_digit()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: a single digit needs to be in [1,3]."
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_1_6_get_digit_more_than_one_digit_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["123", "123", "1"]) as mock_input:
        result = hw06_main.get_digit()
    hint2 = f"\n\n *** Did your loop break after a successful symbol was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 3, hint2


def test_1_7_get_digit_wrong_digit(capsys, monkeypatch):
    with patch('builtins.input', side_effect=["@", "1"]) as mock_input:
        result = hw06_main.get_digit()
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "Error: your input should be only digits."
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_1_8_get_digit_wrong_digit_does_not_continue(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["@", "4", "1"]) as mock_input:
        result = hw06_main.get_digit()
    hint2 = f"\n\n *** Did your loop break after a successful symbol was provided? \n *** Did it continue if the word was wrong?"
    assert mock_input.call_count == 3, hint2



# Part 3
# ===========

def test_1_9_check_pattern_prints_correct_string_C2(capsys, monkeypatch):
    result = hw06_main.check_pattern("C", "2", st_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "@C@2 C2C2"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1


def test_1_10_check_pattern_prints_correct_string_A1(capsys, monkeypatch):
    result = hw06_main.check_pattern("A", "1", st_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    expected = "AA@1"
    hint1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}"
    assert expected in captured.out, hint1

def test_1_10_check_pattern_prints_correct_string_C3(capsys, monkeypatch):
    let = "C"
    dig = "3"
    result = hw06_main.check_pattern(let, dig, st_list)
    captured = capsys.readouterr()
    printout = ""
    if captured.out == "":
        printout = "<Nothing>"
    else:
        printout = captured.out
    printout = printout.strip("\n")
    expected = "Strings with the pattern:\n<Nothing>"
    len_p = len(printout)
    len_exp = len("Strings with the pattern:")
    hint1 = f"\n\n *** For input \n{let+dig}\n *** Your printout after \'Strings with the pattern:\' should be an empty line.\n\n"
    msg1 = f"\n\n *** required printout must have: \n{expected}\n *** Your printout is\n{printout}\n\n"
    # msg2 = f"the length of the expected 'Strings with the pattern:' is {len_exp}\n\n"
    # msg3 = f"the length of the printed 'Strings with the pattern:' is {len_p}\n"
    msg = hint1+msg1
    cond =  len_exp-2  < len_p < len_exp+2
    assert cond, msg


# Part 4
# ===========
def test_1_12_repeat_runs_if_successful(capsys, monkeypatch):
    # with patch('builtins.input', side_effect=["two words", "dog", "toad"]) as mock_input:
    with patch('builtins.input', side_effect=["C", "2", "y", "A", "1", "n", "C"]) as mock_input:
        result = hw06_main.main()
    hint = "\n\n**** DEBUGGING HINT: \n you should restart the main loop if the input is 'y' and stop it otherwise"
    assert mock_input.call_count == 6, hint


#     # Part 4
#     # ===========
#     @patch('builtins.input', side_effect=["C","2", "y", "A", "1", EndError])
#     def test_4_main_H_runs_again_with_y(self, side_effect):
#         print ("\ninside test_4_main_H_runs_again_with_y")
#         with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
#             msg_exit = "\n\n**** DEBUGGING HINT: \n you should restart the main loop if the input is 'y'"
#             with self.assertRaises(EndError, msg = msg_exit):
#                 result = hw06_main.main()


# if __name__ == '__main__':
#     unittest.main()
