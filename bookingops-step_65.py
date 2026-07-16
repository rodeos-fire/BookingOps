# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: BookingOps
# Step 65 – deduplicate imports that are likely to be pulled in by multiple profiles
# Append this block after the existing module body (or at top-level) so every
# future profile sees a single, canonical import list regardless of order.


# ── helpers used by several profiles ───────────────────────────────────────────
from collections.abc import Callable, Iterable, Sequence
from dataclasses import field
from datetime import date, datetime, time
from decimal import Decimal
from enum import Enum, auto
from fractions import Fraction
from functools import reduce, singledispatchmethod
from itertools import chain, combinations, compress, count, cycle, product, repeat, groupby, permutations, islice, accumulate
from math import (
    ceil, floor, copysign, fmod, fabs, hypot, sqrt, log, exp, sin, cos, tan, asin, acos, atan, gcd, lcm,
)
from pathlib import Path, PurePosixPath, PureWindowsPath, PosixPath, WindowsPath
from random import (
    randrange, randint, choice, choices, sample, shuffle, gauss, uniform, normalvariate, random, seed, getrandbits,
)
from statistics import mean, median, stdev, variance
from typing import (
    Any, ClassVar, Self, Type, Union, Optional, List, Dict, Tuple, Set, FrozenSet,
    NamedTuple, Literal, Protocol, SupportsIndex, SupportsAbs, SupportsRound, SupportsInt, SupportsFloat,
)


# ── re-exports that keep the public surface stable across profiles ───────────────
from operator import (
    add, sub, truediv, floordiv, mod, pow, neg, pos, abs_, not_, lshift, rshift, and_, or_, xor, invert,
)
