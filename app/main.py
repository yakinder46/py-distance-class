from typing import Any


class Distance:
    def __init__(self, metters: int | float, cm: int | float = 0) -> None:
        self.meters_total = metters + cm / 100

    @property
    def km(self) -> float:
        return self.meters_total

    def __str__(self) -> str:
        value = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance: {value} kilometers."

    def __repr__(self) -> str:
        value = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance(km={value})"

    def _get_m(self, other: Any) -> float:
        if isinstance(other, Distance):
            return other.meters_total
        return float(other)

    def __add__(self, other: Any) -> "Distance":
        return Distance(self.meters_total + self._get_m(other))

    def __iadd__(self, other: Any) -> "Distance":
        self.meters_total += self._get_m(other)
        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.meters_total * number)

    def __truediv__(self, number: int | float) -> "Distance":
        return Distance(round(self.meters_total / number, 2))

    # Методы сравнения
    def __lt__(self, other: Any) -> bool:
        return self.meters_total < self._get_m(other)

    def __gt__(self, other: Any) -> bool:
        return self.meters_total > self._get_m(other)

    def __eq__(self, other: Any) -> bool:
        return round(self.meters_total, 2) == round(self._get_m(other), 2)

    def __le__(self, other: Any) -> bool:
        return self.meters_total <= self._get_m(other)

    def __ge__(self, other: Any) -> bool:
        return self.meters_total >= self._get_m(other)


class KiloDistance(Distance):
    def __init__(self, km: int | float) -> None:
        super().__init__(km * 1000)

    @property
    def km(self) -> float:
        return self.meters_total / 1000
