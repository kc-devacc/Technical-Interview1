import pytest
from technical_interview import score_for_word, generate_bag, create_random_hand

def test_correct_score_generated_for_word():
    assert score_for_word('guardian') == 10

def test_get_zero_for_no_valid_word():
    assert score_for_word('') == 0

def test_word_generation_function_finds_all_words():
    pass 

def test_player_hand_is_added_to():
    assert len(create_random_hand(7)) == 7
    assert len(create_random_hand(0)) == 0
    assert len(create_random_hand(4)) == 4

def test_bag_created_with_distribution():
    pass


