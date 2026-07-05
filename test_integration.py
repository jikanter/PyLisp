import pytest
from typing_extensions import Any
import lisp
from lisp import Lisper, Reader

STRUCTURES = {
    'addition':  ("(+ 1 2)", 3),
    'subtraction': ("(- 10 11)", -1),
    'multiplication': ("(* 3 4)", 12),
    'division': ("(/ 10 2)", 5)
}

def assert_eval_eq(test, expected):
    l = Lisper()
    r = Reader(l)
    actual : Any = l.eval(r.get_sexpr(test))
    # should not be bear int, should be a lisp.Number
    assert actual.v == expected


def test_lisp_():
    l = Lisper()
    assert l

def test_reader_():
    l = Lisper()
    r = Reader(l)
    assert r

def test_addition():
    t_c = STRUCTURES['addition']
    expected = t_c[1]
    l = Lisper()
    r = Reader(l)
    result = l.eval(r.get_sexpr(t_c[0]))
    # should not be bear int, should be a lisp.Number
    assert type(result) != type(expected)
    assert isinstance(result, lisp.NumberObject)
    assert result.v == expected

def test_subtraction():
    t_c = STRUCTURES['subtraction']
    expected = t_c[1]
    l = Lisper()
    r = Reader(l)
    result = l.eval(r.get_sexpr(t_c[0]))
    # should not be bear int, should be a lisp.Number
    assert type(result) != type(expected)
    assert isinstance(result, lisp.NumberObject)
    assert result.v == expected

def test_multiplication():
    t_c = STRUCTURES['multiplication']
    expected = t_c[1]
    l = Lisper()
    r = Reader(l)
    result = l.eval(r.get_sexpr(t_c[0]))
    # should not be bear int, should be a lisp.Number
    assert type(result) != type(expected)
    assert isinstance(result, lisp.NumberObject)
    assert result.v == expected

def test_division():
    t_c = STRUCTURES['division']
    expected = t_c[1]
    l = Lisper()
    r = Reader(l)
    result = l.eval(r.get_sexpr(t_c[0]))
    # should not be bear int, should be a lisp.Number
    assert type(result) != type(expected)
    assert isinstance(result, lisp.NumberObject)
    assert result.v == expected

def test_exponentiation():
    assert_eval_eq("(+ (+ 1 2) 3)", 6)
    # that fails, it is inverted
    assert_eval_eq("(- 2 (+ 3 4))", -5)
    assert_eval_eq("(- 4 2)", 2)
