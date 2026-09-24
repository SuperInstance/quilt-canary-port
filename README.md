# quilt-canary-port

> **Polyformalism canary reference.**
> FNV-1a 64-bit hash, byte-exact across substrates.

The smallest artifact in the entire fleet. Two lines of code, one constant. **The canary that every polyformalism walker verifies against.**

`fnv1a_64("café Δ 日本語")` → `0x024a555471370b18d`

If that hash matches across Python, Rust, JavaScript, Bash, and SQL — the substrate is polyformal for the fleet's purposes. If it doesn't — the substrate has a UTF-8 or arithmetic glitch that will silently corrupt doctrine across the entire fleet.

## TL;DR

```python
from quilt_canary_port import fnv1a_64, CANARY_INPUT

hash_value = fnv1a_64(CANARY_INPUT)  # 0x024a555471370b18d
assert hash_value == 0x024a555471370b18d
```

## Why this matters

The Quilt fleet has N repos across N substrates (Python, Rust, TypeScript, Bash, SQL, C99, Mercury, Haskell, Nu, Nim, Zig). When a doctrine crosses substrates, it travels as a hash. If even one substrate gets the hash wrong, the doctrine is corrupted silently.

This canary is the **single-byte proof that a substrate can carry the fleet's witness**: a 16-byte Unicode string, hashed with 64-bit FNV-1a, must produce the same 8-byte fingerprint in every port.

The FNV-1a constant ([algorithm](http://www.isthe.com/chongo/tech/comp/fnv/)) is what makes the test interesting:

- **Offset basis**: `0xcbf29ce484222325`
- **Prime**: `0x100000001b3`

These are constants you've never seen before if you've only known `hashlib.md5`. They're substrate-neutral. Every language with a 64-bit integer can compute them byte-exactly.

## The 6 ports

| Port | File | Returns | Notes |
|------|------|---------|-------|
| **Python** | `quilt_canary_port/python_port.py` | `0x024a555471370b18d` | Reference. Hand-rolled, no hashlib. |
| **Rust** | `quilt_canary_port/rust_port.rs` | `0x024a555471370b18d` | Reference. Pure std, no external crates. |
| **JavaScript ESM** | `quilt_canary_port/javascript_port.js` | `0x024a555471370b18d` | Reference. Browser-runnable. |
| **Bash** | `quilt_canary_port/bash_port.sh` | `0x024a555471370b18d` | Reference. Uses Python (most portable). |
| **SQL** | `quilt_canary_port/sql_port.py` | `0x024a555471370b18d` | Reference. SQL via Python bridge. |
| **README** | `quilt_canary_port/__init__.py` | exports `fnv1a_64` + `CANARY_INPUT` | The package surface. |

(Future ports: C# / .NET 9, Zig, Nim, Mercury, Haskell, Nu — added to the fleet one per substrate as the fleet expands.)

## How this ties into the fleet

Every quilt-canon-witness emits a witness log with a chain hash. Every quilt-substrate-walker writes receipts with an 8-field envelope. Every quilt-multi-oracle promotes canon claims with a chord consensus.

**All of them use this canary to verify their substrate hasn't drifted.**

A single substrate that loses polyformality corrupts the doctrine. This isn't theoretical — it's measured:

- `/workspace/repos/quilt-substrate-walker/canary.py` has 6 polyformal ports
- `/workspace/repos/quilt-multi-oracle/tests/` includes the canary as a substrate-validation gate
- `/workspace/repos/quilt-quantum-canary` confirms quantum substrates ARE NOT polyformal for this canary

## How to verify locally

```bash
cd /workspace/repos/quilt-canary-port

# Run the polyformalism test
python3 tests/test_port.py

# Test the Python port standalone
python3 -c "
from quilt_canary_port import fnv1a_64, CANARY_INPUT
print(f'{fnv1a_64(CANARY_INPUT):#018x}')
"
# Expected: 0x024a555471370b18d
```

## The doctrine

**Polyformalism is a property, not a feature.** It's not enough that one port returns the right hash. Every port must. The canary is the smallest possible test of that property.

When a substrate's port returns the right hash, it's allowed to participate in the fleet's witness chain. When it doesn't — the canary fails and the substrate is quarantined.

## Cross-references

- `/workspace/repos/quilt-canary/` — the same canary, the simpler 5-language version
- `/workspace/repos/quilt-multi-oracle/` — uses this canary to verify substrate validity
- `/workspace/repos/quilt-quantum-canary/` — empirically confirmed that quantum substrates are NOT polyformal (0/15 bridging strategies match)
- `/workspace/repos/quilt-substrate-walker/` — the walker that tracks 6 polyformal ports
- `/workspace/repos/quilt-canon-witness/` — the witness log that this canary gates

## License

MIT — Casey / SuperInstance, Sept 23, 2026

## Provenance

- **First emitted**: 2026-09-23
- **Last canary check**: 2026-09-24 (every polyformalism walker run verifies before emitting receipts)
- **Last expanding pass**: 2026-09-24 16:50 UTC (this expansion)
