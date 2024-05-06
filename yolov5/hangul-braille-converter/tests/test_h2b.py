# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package
import hbcvt

def test_hangul_to_braille():
    answer = [['안', [['ㅇ', [[1, 1, 0, 1, 1, 0]]], ['ㅏ', [[1, 1, 0, 0, 0, 1]]], ['ㄴ', [[0, 1, 0, 0, 1, 0]]]]], ['녕', [['ㄴ', [[1, 0, 0, 1, 0, 0]]], ['ㅕ', [[1, 0, 0, 0, 1, 1]]], ['ㅇ', [[0, 1, 1, 0, 1, 1]]]]], ['하', [['ㅎ', [[0, 1, 0, 1, 1, 0]]], ['ㅏ', [[1, 1, 0, 0, 0, 1]]]]], ['세', [['ㅅ', [[0, 0, 0, 0, 0, 1]]], ['ㅔ', [[1, 0, 1, 1, 1, 0]]]]], ['요', [['ㅇ', [[1, 1, 0, 1, 1, 0]]], ['ㅛ', [[0, 0, 1, 1, 0, 1]]]]], ['뷁', [['ㅂ', [[0, 0, 0, 1, 1, 0]]], ['ㅞ', [[1, 1, 1, 1, 0, 0], [1, 1, 1, 0, 1, 0]]], ['ㄺ', [[0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0]]]]]]
    result = hbcvt.h2b.text("안녕하세요뷁")
    correct = (result == answer)
    assert correct
    return correct

def test_non_hangul_to_braille():
    answer = [['h', [['h', [[1, 1, 0, 0, 1, 0]]]]], ['e', [['e', [[1, 0, 0, 0, 1, 0]]]]], ['l', [['l', [[1, 1, 1, 0, 0, 0]]]]], ['l', [['l', [[1, 1, 1, 0, 0, 0]]]]], ['o', [['o', [[1, 0, 1, 0, 1, 0]]]]], [' ', [[' ', [[0, 0, 0, 0, 0, 0]]]]], ['1', [['1', [[0, 0, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0]]]]], ['s', [['s', [[0, 1, 1, 1, 0, 0]]]]], ['t', [['t', [[0, 1, 1, 1, 1, 0]]]]], [' ', [[' ', [[0, 0, 0, 0, 0, 0]]]]], ['W', [['W', [[0, 0, 0, 0, 0, 1], [0, 1, 1, 1, 1, 1]]]]], ['o', [['o', [[1, 0, 1, 0, 1, 0]]]]], ['r', [['r', [[1, 1, 1, 0, 1, 0]]]]], ['l', [['l', [[1, 1, 1, 0, 0, 0]]]]], ['d', [['d', [[1, 0, 0, 1, 1, 0]]]]], ['!', [['!', [[0, 1, 1, 0, 1, 0]]]]]];
    result = hbcvt.h2b.text("hello 1st World!")
    correct = (result == answer)
    assert correct
    return correct

