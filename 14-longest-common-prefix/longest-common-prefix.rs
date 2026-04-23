impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.is_empty() {
            return "".to_string();
        }

        let first = &strs[0];

        for i in 0..first.len() {
            let ch = first.as_bytes()[i];

            for s in &strs[1..] {
                // bounds check + mismatch
                if i >= s.len() || s.as_bytes()[i] != ch {
                    return first[..i].to_string();
                }
            }
        }

        first.clone()
    }
}