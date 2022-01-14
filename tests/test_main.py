import io
import pytest

from contextlib import redirect_stdout

from app.main import Distance

@pytest.mark.parametrize(
    'kilometers',
    [
        50,
        100,
        300
    ]
)
def test_distance_class_init(kilometers):
    distance = Distance(kilometers)
    assert distance.km == kilometers, (
        f"Instance attribute 'km' should equal to {kilometers} "
        f"when you create instance with 'Distance({kilometers})'"
    )


@pytest.mark.parametrize(
    'kilometers,output',
    [
        (50, "Distance: 50 kilometers.\n"),
        (100, "Distance: 100 kilometers.\n"),
        (300, "Distance: 300 kilometers.\n")
    ]
)
def test_distance_class_str(kilometers, output):
    distance = Distance(kilometers)
    f = io.StringIO()

    with redirect_stdout(f):
        print(distance)

    out = f.getvalue()

    assert out == output, (
        f"Output should equal to {output} "
        f"when you call 'print' with instance of Distance class"
    )


@pytest.mark.parametrize(
    'kilometers,output',
    [
        (50, "Distance(km=50)"),
        (100, "Distance(km=100)"),
        (300, "Distance(km=300)")
    ]
)
def test_distance_class_str(kilometers, output):
    distance = Distance(kilometers)

    assert repr(distance) == output, (
        f"'repr(distance)' should equal to {output} "
        f"when distance is created with 'Distance({kilometers})'"
    )


@pytest.mark.parametrize(
    'kilometers1,kilometers2,kilometers3',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_add_distance_and_distance(kilometers1, kilometers2, kilometers3):
    distance1 = Distance(kilometers1)
    distance2 = Distance(kilometers2)
    distance3 = distance1 + distance2
    assert isinstance(distance3, Distance), (
        "Result of sum of Distance instances should be "
        "Distance instance"
    )
    assert distance3.km == kilometers3, (
        f"distance3.km should equal to {kilometers3}, "
        f"when 'distance3 = Distance({kilometers1}) + Distance({kilometers2})'"
    )


@pytest.mark.parametrize(
    'kilometers1,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_add_distance_and_number(kilometers1, kilometers2, result):
    distance1 = Distance(kilometers1)
    distance2 = distance1 + kilometers2
    assert isinstance(distance2, Distance), (
        "Result of sum of Distance instance and number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance3 = Distance({kilometers1}) + {kilometers2}'"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_iadd_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    instance_1 = distance1
    distance2 = Distance(kilometers2)
    distance1 += distance2
    instance_2 = distance1
    assert instance_1 is instance_2, (
        "__iadd__ should return the same instance"
    )
    assert distance1.km == result, (
        f"distance1.km should equal to {result}, "
        f"when 'distance1' is Distance({kilometers}) and "
        f"'distance1 += Distance({kilometers2})"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_iadd_number(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    instance_1 = distance1
    distance1 += kilometers2
    instance_2 = distance1
    assert instance_1 is instance_2, (
        "__iadd__ should return the same instance"
    )
    assert distance1.km == result, (
        f"'distance1.km' should equal to {result}, "
        f"when 'distance1' is Distance({kilometers}) and "
        f"'distance1 += {kilometers2}'"
    )


@pytest.mark.parametrize(
    'kilometers,number,result',
    [
        (50, 3, 150),
        (30, 7, 210),
        (45, 5, 225)
    ]
)
def test_distance_class_mul(kilometers, number, result):
    distance1 = Distance(kilometers)
    distance2 = distance1 * number
    assert isinstance(distance2, Distance), (
        "Result of Distance instance multiplied by number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance2 = Distance({kilometers}) * {number}'"
    )


@pytest.mark.parametrize(
    'kilometers,number,result',
    [
        (50, 3, 16.67),
        (30, 7, 4.29),
        (45, 5, 9)
    ]
)
def test_distance_class_truediv(kilometers, number, result):
    distance1 = Distance(kilometers)
    distance2 = distance1 / number
    assert isinstance(distance2, Distance), (
        "Result of Distance instance divided by number should be "
        "Distance instance"
    )
    assert distance2.km == result, (
        f"distance2.km should equal to {result}, "
        f"when 'distance2 = Distance({kilometers}) / {number}'"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 30, True)
    ]
)
def test_distance_class_eq_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 == distance2) is result, (
        f"'Distance({kilometers}) == Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 30, True)
    ]
)
def test_distance_class_eq_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance == kilometers2) is result, (
        f"'Distance({kilometers}) == {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False)
    ]
)
def test_distance_class_gt_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 > distance2) is result, (
        f"'Distance({kilometers}) > Distance{kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False)
    ]
)
def test_distance_class_gt_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance > kilometers2) is result, (
        f"'Distance({kilometers}) > {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False)
    ]
)
def test_distance_class_ge_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 >= distance2) is result, (
        f"'Distance({kilometers}) >= Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, True),
        (300, 100, True),
        (30, 100, False)
    ]
)
def test_distance_class_ge_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance >= kilometers2) is result, (
        f"'Distance({kilometers}) >= {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True)
    ]
)
def test_distance_class_lt_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 < distance2) is result, (
        f"'Distance({kilometers}) < Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, False),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True)
    ]
)
def test_distance_class_lt_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance < kilometers2) is result, (
        f"'Distance({kilometers}) < {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True)
    ]
)
def test_distance_class_le_distance(kilometers, kilometers2, result):
    distance1 = Distance(kilometers)
    distance2 = Distance(kilometers2)
    assert (distance1 <= distance2) is result, (
        f"'Distance({kilometers}) <= Distance({kilometers2})' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 50, True),
        (100, 30, False),
        (300, 100, False),
        (30, 100, True)
    ]
)
def test_distance_class_le_number(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance <= kilometers2) is result, (
        f"'Distance({kilometers}) <= {kilometers2}' should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers',
    [
        50,
        100,
        300
    ]
)
def test_distance_class_len(kilometers):
    distance = Distance(kilometers)
    assert len(distance) == distance.km, (
        f"'len()' for instance should return instance.km"
    )
