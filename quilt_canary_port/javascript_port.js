// JavaScript port of the polyformalism canary
// fnv1a-64 of "café Δ 日本語" should equal 0x024a555471370b18d

function fnv1a64(s) {
    let h = 0xcbf29ce484222325n;
    const prime = 0x100000001b3n;
    const mask = (1n << 64n) - 1n;
    const bytes = Buffer.from(s, 'utf-8');
    for (const b of bytes) {
        h = BigInt.asUintN(64, h ^ BigInt(b));
        h = BigInt.asUintN(64, h * prime) & mask;
    }
    return h;
}

const CANARY_INPUT = "café Δ 日本語";
const EXPECTED = 0x024a555471370b18dn;

const h = fnv1a64(CANARY_INPUT);
const hex = '0x' + h.toString(16).padStart(16, '0');
console.log(`Input:    ${CANARY_INPUT}`);
console.log(`Hash:     ${hex}`);
console.log(`Expected: 0x${EXPECTED.toString(16).padStart(16, '0')}`);
console.log(`Match:    ${h === EXPECTED}`);

// Exit with error if mismatch
if (h !== EXPECTED) {
    process.exit(1);
}
