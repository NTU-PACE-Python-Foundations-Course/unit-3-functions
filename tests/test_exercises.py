import pytest


def test_exercise_1_apply_discount(tb):
    apply_discount = tb.ref("apply_discount")

    assert apply_discount(100) == pytest.approx(90.0)
    assert apply_discount(100, discount_rate=0.25) == pytest.approx(75.0)


def test_exercise_2_analyse_scores(tb):
    scores = [72, 88, 91, 65, 79]
    analyse_scores = tb.ref("analyse_scores")

    highest, lowest, average = analyse_scores(scores)

    assert highest == max(scores)
    assert lowest == min(scores)
    assert average == pytest.approx(sum(scores) / len(scores))


def test_exercise_3_area_and_perimeter(tb):
    area = tb.ref("area")
    perimeter = tb.ref("perimeter")

    assert area(4, 3) == 12
    assert area(10, 2) == 20
    assert perimeter(4, 3) == 14
    assert perimeter(5, 5) == 20


def test_exercise_4_composing_functions(tb):
    apply_discount = tb.ref("apply_discount")
    add_gst = tb.ref("add_gst")
    final_price = tb.ref("final_price")

    assert add_gst(100) == pytest.approx(109.0)

    expected = add_gst(apply_discount(200))
    assert final_price(200) == pytest.approx(expected)
