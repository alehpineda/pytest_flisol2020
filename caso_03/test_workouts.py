import pytest

from workouts import print_workout_days

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize(
    "valor, esperado",
    [
        ("upper body #1", "Mon\n"),
        ("lower body #1", "Tue\n"),
        ("30 min cardio", "Wed\n"),
        ("upper body #2", "Thu\n"),
        ("lower body #2", "Fri\n"),
        ("pesas", "No matching workout\n"),
        ("spinning", "No matching workout\n"),
        ("upper", "Mon, Thu\n"),
        ("lower", "Tue, Fri\n"),
    ],
)
def test_print_workout(capsys, valor, esperado):
    print_workout_days(valor)
    capturado = capsys.readouterr()
    assert capturado.out == esperado
