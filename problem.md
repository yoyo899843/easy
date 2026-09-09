# 有問題的題目 (Problematic Challenges)

ISIP-CTF.Easy — challenges that are **blocked by a defect or a missing resource**, not
merely unsolved-because-hard. Current progress: **246/287**.

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
| 184 / 207 | PicoCTF_2017: Special Agent User | User-Agent = `Chrome/36.0.1985.125` (OpenBSD); every browser/version wrapper rejected |
| 215 | picoCTF2017: digital-camouflage-50 | POST `pswrd=S04xWjZQWFZ5OQ==` → `KN1Z6PXVy9`; description (GPS/image.jpg) also mismatches the pcap |
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

## D. challenge.yml 內容缺失 (self-contained puzzles wired to a dead service)

| ID | Challenge | Port | Note |
|----|-----------|------|------|
| 228-241 | THY-Crypto 1-AES…9-Substitution (14 challenges) | 30011-30023 | **not server challenges** — each is a self-contained "decode this data" puzzle. The data lives in `build/task.yml` but `challenge.yml` `description` is empty and points at a dead `nc` service. Verified: every flag = the decode result. Fix: move `task.yml` text into `challenge.yml` description, drop `connection_info`; attach `9-Substitution/dist/cipher.txt`. |

---

## E. Blind pwn — 有 service 沒 binary (live service, no binary)

| ID | Challenge | Port | Banner |
|----|-----------|------|--------|
| 244 | pwn_2 | 10009 | "Please enter your name:" (crashes on long input → likely BOF) |
| — | (unidentified) | 10005 | "What your name? / What do you want to say :)?" |

---

## F. 加密變體未確定 (crypto variant undetermined)

| ID | Challenge | Note |
|----|-----------|------|
| 23 | b85 (`:30003`) | 53-char base85 on the RFC1924 charset; no standard variant (ascii85 / base85 / z85 / RFC1924, either endianness) decodes to a readable flag — needs the exact custom alphabet |

---

## G. 一般困難的 Web (hard, not confirmed broken — revisit)

| ID | Challenge | Port | Where it stands |
|----|-----------|------|-----------------|
| 111 | Admin | 20031 | `login.php` (`user`/`pass`) always "wrong"; no SQLi/default-cred; no source disclosure |
| 271 | babytrick | 20048 | HITCON Baby^H PHP-deserialization (`?data=` → `unserialize` → `__destruct` → `login`); needs the multibyte/`utf8_general_ci` trick to log in as `orange` **and** its password — double `mysql_escape_string` |
| 272 | papapa-ubuntu | 20049 | 302 → `https://…/index.php` on every path; "find the secret (pentesting)"; dirb + XFF/XFP header bypasses found nothing |
| 277 | you-cant-see-me | 20044 | `/user/N` lists 10 cats, no hidden ids, not SSTI (unlike its twin 280) |

---

## Summary

- **A. Missing source / DB-only:** 123, 273
- **B. picoCTF/CSAW custom flag:** 184, 207, 215, 203
- **C. Need Windows/wine:** 89, 90, 92, 96, 97, 108, 109, 110, 247
- **D. challenge.yml content missing:** 228-241 (14, need `description` filled from `task.yml`)
- **E. Blind pwn:** 244, 10005
- **F. Crypto variant:** 23
- **G. Hard web (revisit):** 111, 271, 272, 277

Highest-value follow-up: a **Windows/wine** environment unlocks all of section **C** (9).
The rest need the organiser (missing challenge source, DB-only flag) or more work (G).

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
path_traversal — fixed via `challenge.yml` flag, `build/flag`, or Dockerfile/build changes.*
