from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        value = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance: {value} kilometers."

    def __repr__(self) -> str:
        value = int(self.km) if self.km == int(self.km) else self.km
        return f"Distance(km={value})"

    def _get_km(self, other: Any) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    def __add__(self, other: Any) -> "Distance":
        return Distance(self.km + self._get_km(other))

    def __iadd__(self, other: Any) -> "Distance":
        self.km += self._get_km(other)
        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: Any) -> bool:
        return self.km < self._get_km(other)

    def __gt__(self, other: Any) -> bool:
        return self.km > self._get_km(other)

    def __eq__(self, other: Any) -> bool:
        return round(self.km, 2) == round(self._get_km(other), 2)

    def __le__(self, other: Any) -> bool:
        return self.km <= self._get_km(other)

    def __ge__(self, other: Any) -> bool:
        return self.km >= self._get_km(other)
