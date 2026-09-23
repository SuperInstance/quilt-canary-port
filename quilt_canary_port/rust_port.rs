//! Rust port of the polyformalism canary.
//! fnv1a-64 of "café Δ 日本語" should equal 0x024a555471370b18d.

pub const CANARY_INPUT: &str = "café Δ 日本語";
pub const EXPECTED: u64 = 0x024a555471370b18d;

pub fn fnv1a_64(s: &str) -> u64 {
    let mut h: u64 = 0xcbf29ce484222325;
    for b in s.as_bytes() {
        h ^= *b as u64;
        h = h.wrapping_mul(0x100000001b3);
    }
    h
}

#[cfg(test)]
mod tests {
    use super::*;
    
    #[test]
    fn canary_value() {
        assert_eq!(fnv1a_64(CANARY_INPUT), EXPECTED);
    }
}
