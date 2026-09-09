# 有問題的題目 (Problematic Challenges)

ISIP-CTF.Easy — challenges that are **blocked by a defect or a missing resource**, not
merely unsolved-because-hard. Current progress: **261/287**.

Categories below, most actionable first.

---

## A. 缺原始碼 / flag 拿不到 (missing source, or flag unreachable)

| ID | Challenge | Problem |
|----|-----------|---------|
| 123 | Level (`:20001`) | `BreakAll - Web/chals/Level` has **only `challenge.yml`, no `build/`** — the cookie challenge's source (`FLAG{I_like_cookie}`) is missing. Port 20001 currently serves a different challenge, SSRF-Noob (that one is fine). |
| 273 | RealWorld (WordPress, `:20047`) | Cracked wp-admin `tyc4d:Flowers1` (phpass hash leaked in a blog-post phpMyAdmin screenshot). Logged in, but the flag is **not** in any post/page/comment/option/media; theme+plugin files not writable (no RCE); REST API 404; DB not exposed → flag is DB-only, unreachable. |

---

## B. picoCTF / CSAW 自訂 flag，與證據不符 (custom flags don't match the evidence)

| ID | Challenge | What the evidence gives |
|----|-----------|-------------------------|
| 215 | picoCTF2017: digital-camouflage-50 | POST `pswrd=S04xWjZQWFZ5OQ==` → `KN1Z6PXVy9`; description (GPS/image.jpg) also mismatches the pcap. yml wants `8PFEo0ttHQ` — no derivation from the provided `data.pcap`. |
| 203 | CSAW Quals 2013: Networking 2 | pcap shows the captured user typing `flag{d316759c281bf925d600be698a4973d5}` as a password → **"Login incorrect"** (it's the *Networking 1* flag, shown failing on purpose). Real answer `flag{f9b43c9e9c05be5e08ea163007af5144}` (yml) is correct but only known from a CSAW writeup — not derivable from the single stream. |

---

## C. 需要 Windows / wine 才能執行 (need a Windows environment)

Windows PE binaries; no `wine`/Windows in this sandbox, static PE analysis didn't surface
the flags. All **BreakAll - Reverse** unless noted.

| ID | Challenge | File |
|----|-----------|------|
| 89 | CFM_Shaco | CPP_MFC2.exe (MFC) |
| 90 | Counter | counter.zip → counter.exe |
| 92 | Lottery | Lottery.exe |
| 96 | SendMsg | SendMsg.exe |
| 97 | SpecialCalc | SpecialCalc.exe |
| 108 | olleH | hello.exe |
| 109 | tryregistry | tryregistry.exe (`RegOpenKeyExW`) |
| 110 | 陳廷宇_Baby_Assembly | BabyAssembly.exe (registry; decoy `CGCTF{is_this_the_flag}`) |
| 247 | Windows_2 (THY-Reverse) | VERSION.dll (DLL hijack theme) |

---

## D. Blind pwn — 有 service 沒 binary (live service, no binary)

| ID | Challenge | Port | Banner |
|----|-----------|------|--------|
| 244 | pwn_2 | 10009 | "Please enter your name:" (crashes on long input → likely BOF) |
| — | (unidentified) | 10005 | "What your name? / What do you want to say :)?" |

---

## E. 一般困難的 Web (hard, not confirmed broken — revisit)

| ID | Challenge | Port | Where it stands |
|----|-----------|------|-----------------|
| 111 | Admin | 20031 | `login.php` (`user`/`pass`) always "wrong"; no SQLi/default-cred; no source disclosure |
| 271 | babytrick | 20048 | HITCON Baby^H PHP-deserialization (`?data=` → `unserialize` → `__destruct` → `login`); needs the multibyte/`utf8_general_ci` trick to log in as `orange` **and** its password — double `mysql_escape_string` |
| 272 | papapa-ubuntu | 20049 | 302 → `https://…/index.php` on every path; "find the secret (pentesting)"; dirb + XFF/XFP header bypasses found nothing |
| 277 | you-cant-see-me | 20044 | `/user/N` lists 10 cats, no hidden ids, not SSTI (unlike its twin 280) |

---

## Summary

- **A. Missing source / DB-only:** 123, 273
- **B. picoCTF/CSAW custom flag:** 215, 203
- **C. Need Windows/wine:** 89, 90, 92, 96, 97, 108, 109, 110, 247
- **D. Blind pwn:** 244, 10005
- **E. Hard web (revisit):** 111, 271, 272, 277

Highest-value follow-up: a **Windows/wine** environment unlocks all of section **C** (9).
The rest need the organiser (missing challenge source, DB-only flag) or more work (E).
No fixable-defect challenges remain — everything left needs an environment, a missing
file/binary, or genuine solving effort.

---

*Recently resolved (removed from this list): 26 fa, 81 張元_Pwn-6 (build/ was on EOL
`ubuntu:16.04` + wrong problem.md description; rebased, all 3 stages → shell → flag),
114 KAIBRO BUY, 119 Web-2 (mislabelled; now a working SQLi challenge →
`ACTF{YURXMTYS4C1MiSwjPBZc}`), 128/262/270 XSS, 153 web-2 Easy_Robots (→
`BreakALLCTF{7QtKB2N5TlqAAEzCrzNO}`), 158 registration + 159 start (added `build/`:
Dockerfile + socat + flag; both solved end-to-end), 227/230/233 Calc_RSA, 265
information_leakage, 251 Shop (`flag()` was an empty stub; recompiled `shop.c` with a
real `puts()`, replaced `dist/shop` — inflate balance with a negative `amount`, then
buy item 3 → flag), 278 find-method, 279 my-new-router, 張元_Pwn-6~9, THY
path_traversal, **THY-Crypto CryptoLab-2024 ×12** (1/2-ASCII, 3-Hex, 4-Chinese,
5-Base64, 6-Base64_Hex, 9-Substitution, 1/2-AES, 3/4-AES_ECB, 9-AES_CBC — puzzle text
was stranded in `build/task.yml`; moved into `challenge.yml` `description`, dropped the
dead `nc` `connection_info`, attached `cipher.txt`; all 12 flags re-verified by decoding)
— fixed via `challenge.yml` flag, `build/flag`, or Dockerfile/build changes.*

*Not actually broken (misdiagnosed in earlier surveys, no change needed): 23 b85 —
it's standard Python `base64.b85encode` with a junk char from `!@#$%^&*` inserted after
every 3rd char (`random.seed(2024)`); strip every 4th char, then `b85decode` →
`breakall{u_such_encoding_master}` (verified). 184/207 Special Agent User — pcap UA is
`Chrome/36.0.1985.125`; the description says give 3 subversion levels and drop trailing
`.0`s, so the answer is exactly `Chrome 36.0.1985`, which is what the yml holds (verified).*
