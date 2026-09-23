"""Python reference implementation of the polyformalism canary."""

CANARY_INPUT = "café Δ 日本語"
EXPECTED = 0x024a555471370b18d


def fnv1a_64(s: str) -> int:
    """FNV-1a 64-bit hash. Reference for the polyformalism fleet."""
    h = 0xcbf29ce484222325
    for b in s.encode("utf-8"):
        h = h ^ b
        h = (h * 0x100000001b3) & 0xffffffffffffffff
    return h


def verify() -> bool:
    """Verify the canary produces the expected hash."""
    return fnv1a_64(CANARY_INPUT) == EXPECTED


if __name__ == "__main__":
    h = fnv1a_64(CANARY_INPUT)
    print(f"Input: {CANARY_INPUT}")
    print(f"Hash:  0x{h:016x}")
    print(f"Expected: 0x{EXPECTED:016x}")
    print(f"Match: {verify()}")
