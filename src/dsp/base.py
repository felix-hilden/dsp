from collections import Counter
from dataclasses import dataclass
from typing import List, Union

from .facility import FacilityType


def maybe_wrap_resource_in_list(
    res: Union["Resource", List["Resource"]]
) -> List["Resource"]:
    if not isinstance(res, list):
        res = [res]
    return res


@dataclass(frozen=True)
class Resource:
    name: str

    def __mul__(self, other: int) -> List["Resource"]:
        return [self] * other

    def __rmul__(self, other):
        return self * other

    def __add__(self, other: Union["Resource", List["Resource"]]) -> List["Resource"]:
        return [self] + maybe_wrap_resource_in_list(other)

    def __radd__(self, other):
        return self + other


class Materials(dict):
    @classmethod
    def from_list(cls, materials: Union[Resource, List[Resource]]):
        counts = Counter(maybe_wrap_resource_in_list(materials))
        return cls(counts)

    def __mul__(self, other: int) -> "Materials":
        return type(self)({k: other * v for k, v in self.items()})

    def __add__(self, other: "Materials") -> "Materials":
        return type(self)(
            {
                k: self.get(k, 0) + other.get(k, 0)
                for k in set(self.keys()) | set(other.keys())
            }
        )

    def __sub__(self, other: "Materials") -> "Materials":
        new = {
            k: self.get(k, 0) - other.get(k, 0)
            for k in set(self.keys()) | set(other.keys())
        }
        return type(self)({k: v for k, v in new.items() if v != 0})

    def __rsub__(self, other: "Materials") -> "Materials":
        return self - other


class Recipe:
    def __init__(
        self,
        facility: FacilityType,
        secs: float,
        in_: Union[None, Resource, List[Resource]],
        out: Union[None, Resource, List[Resource]],
    ):
        self.facility = facility
        self.secs = secs
        self.in_ = Materials.from_list(in_ or [])
        self.out = Materials.from_list(out or [])
