import io
import pytest

from contextlib import redirect_stdout

from app.main import Distance


@pytest.mark.parametrize(
    'kilometers',
    [
        (50,),
        (100,),
        (300,)
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
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_add(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    dist2 = distance + kilometers2
    assert dist2 == result, (
        f"The sum of 'Distance({kilometers})' and {kilometers2} "
        f"should equal to {result}"
    )


@pytest.mark.parametrize(
    'kilometers,kilometers2,result',
    [
        (50, 15, 65),
        (100, 30, 130),
        (300, 100, 400)
    ]
)
def test_distance_class_iadd(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    instance_1 = distance
    distance += kilometers2
    instance_2 = distance
    assert distance.km == result, (
        f"Attribute 'km' of Distance instance should become {result} "
        f"when your initial 'km' equals to {kilometers} "
        f"and you '+=' {kilometers2} to your instance"
    )
    assert instance_1 is instance_2, (
        "__iadd__ should return the same instance"
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
    distance = Distance(kilometers)
    assert distance * number == result, (
        f"Instance multiplied by {number} should equal to {result}, "
        f"when instance.km equals to {kilometers}"
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
    distance = Distance(kilometers)
    assert distance / number == result, (
        f"Instance divided by {number} should equal to {result}, "
        f"when instance.km equals to {kilometers}"
    )


@pytest.mark.parametrize(
    'kilometers,number,result',
    [
        (50, 20, 10),
        (30, 100, 30),
        (45, 10, 5)
    ]
)
def test_distance_class_mod(kilometers, number, result):
    distance = Distance(kilometers)
    assert distance % number == result, (
        f"Instance modulo {number} should equal to {result}, "
        f"when instance.km equals to {kilometers}"
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
def test_distance_class_eq(kilometers, kilometers2, result):
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
def test_distance_class_gt(kilometers, kilometers2, result):
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
def test_distance_class_ge(kilometers, kilometers2, result):
    distance = Distance(kilometers)
    assert (distance >= kilometers2) is result, (
        f"'Distance({kilometers}) => {kilometers2}' should equal to {result}"
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
def test_distance_class_lt(kilometers, kilometers2, result):
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
def test_distance_class_le(kilometers, kilometers2, result):
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



