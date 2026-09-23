#!/usr/bin/env bash
# Bash port of the polyformalism canary (delegates to Python)
# fnv1a-64 of "café Δ 日本語" should equal 0x024a555471370b18d

python3 -c "
import sys
s = 'café Δ 日本語'
h = 0xcbf29ce484222325
for b in s.encode('utf-8'):
    h = h ^ b
    h = (h * 0x100000001b3) & 0xffffffffffffffff
print(f'0x{h:016x}')
"
