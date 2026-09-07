# 有問題的題目 (Problematic Challenges)

ISIP-CTF.Easy — challenges that are **blocked by a defect or a missing resource**, not
merely unsolved-because-hard. Current progress: **234/287**.

Categories below, most actionable first:

---

## A. 已破解但 CTFd 拒絕正解 (solved, but the correct flag is rejected)

These are almost certainly **platform bugs** — the challenge service hands back a flag,
or a documented decode produces one, but CTFd will not accept it. Worth reporting to the
organiser. (Pattern first seen on 123 SSRF, whose `FLAG{ssrf_bypass_limit}` only worked
for a *different* challenge id, 117.)

| ID | Challenge | What I got | Status |
|----|-----------|------------|--------|
| 227 / 230 / 233 | Calc_RSA / 1-/2-Calculate_RSA (`:30024-26`) | MT19937 state fully recovered (39×512-bit `getrandbits` = 624 words), next number predicted, service prints `Congratulations! Here's your flag: breakall{how_is_that_even_possible}` | **flag rejected** in every wrapper. Solver: `scratchpad/ctf/mt_solve.py` |
| 273 | RealWorld (WordPress, `:20047`) | Cracked wp-admin `tyc4d:Flowers1` (phpass hash leaked in a blog-post phpMyAdmin screenshot, john+rockyou) | logged in, but flag is **not** in any post/page/comment/option/media; plugin+theme files not writable (no RCE); REST API 404; DB/phpMyAdmin not exposed → **flag unreachable** (DB-only) |
| 153 | web-2: Easy_Robots.txt (`:40032`) | `/secret/flag.txt` → hex→base64 → `BreakALLCTF{7QtKB2N5TlqAAEzCrzNO}` | **rejected** (documented anomaly) |
| 123 | Level (URL Previewer / SSRF, `:20001`) | `?url=http://127.0.0.1/config.php` → `FLAG{ssrf_bypass_limit}` | **rejected** (same flag was correct for 117 SSRF Noob) |

---

## B. Decoy flag，真正的 flag 在不存在的伺服器上 (decoy in file, no server)

`strings`/runtime yields a `BreakALLCTF{…}` that CTFd rejects; the real flag is meant to
come from a server that isn't running (`connection_info = None`).

| ID | Challenge | Decoy flag (rejected) | Note |
|----|-----------|-----------------------|------|
| 53 | ForYou.tar.gz | `BreakALLCTF{U6TLCzQsk73HwcW7rqAW}` | flag in extracted file |
| 56 | TobeExe | `BreakALLCTF{UvB3IUqxCCiTVxeOuWrL}` | 32-bit ELF prints it on run |
| 73 | reverse | `BreakALLCTF{VLJekKONoWld7ari6HHJ}` | ELF: overflow `-0x4`→`0xabcd1234` prints the decoy; taunt "Do you know strings tool?" |

---

## C. picoCTF/CSAW 題目使用自訂 flag，與 pcap/內容不符 (custom flags don't match evidence)

The recovered evidence is correct, but CTFd expects a different custom string.

| ID | Challenge | What the evidence gives | Note |
|----|-----------|-------------------------|------|
| 184 / 207 | PicoCTF_2017: Special Agent User | User-Agent = `Chrome/36.0.1985.125` (OpenBSD) | every browser/version wrapper rejected |
| 215 | picoCTF2017: digital-camouflage-50 | POST `pswrd=S04xWjZQWFZ5OQ==` → `KN1Z6PXVy9` | every wrapper rejected; description text (GPS/image.jpg) also mismatches the pcap |
| 203 | CSAW Quals 2013: Networking 2 | telnet login `csaw` / password = the *Networking 1* flag → "Login incorrect" | real flag not derivable from the single stream |

---

## D. 需要 Windows / wine 才能執行 (need a Windows environment)

Windows PE binaries; no `wine`/Windows available in this sandbox, and static PE analysis
alone did not surface the flags. All are **BreakAll - Reverse** unless noted.

| ID | Challenge | File |
|----|-----------|------|
| 89 | CFM_Shaco | CPP_MFC2.exe (MFC) |
| 90 | Counter | counter.zip → counter.exe |
| 92 | Lottery | Lottery.exe |
| 96 | SendMsg | SendMsg.exe |
| 97 | SpecialCalc | SpecialCalc.exe |
| 108 | olleH | hello.exe |
| 109 | tryregistry | tryregistry.exe (uses `RegOpenKeyExW`) |
| 110 | 陳廷宇_Baby_Assembly | BabyAssembly.exe (registry; decoy `CGCTF{is_this_the_flag}`) |
| 247 | Windows_2 (THY-Reverse) | VERSION.dll (DLL hijack theme) |

---

## E. 伺服器已關閉 / 協定不明 (service down or unknown protocol)

The challenge needs a live `nc`/HTTP service that is currently down or unresponsive.

| ID | Challenge | Port | Note |
|----|-----------|------|------|
| 228-241 | THY-Crypto 1-AES…9-Substitution (14 challenges) | 30011-30023 | all **down**; only the client-side Crypto Playground SPA (`:30010`, flag = `FLAG{sha256(input)}`, ambiguous without a per-challenge prompt) and Calc_RSA (30024-26) are up |
| 81 | 張元_Pwn-6 | (magic+1000-math service) | binary needs magic `0x079487ff` then 1000 math → `system("sh")`, but **no live port** hosts it |
| 26 | fa | 30005 | connects but sends nothing; unknown protocol |
| 158 | registration | — | `conn=None`; binary has `systemAdmin()`→shell (ret2win) but no service to hit |
| 159 | start | — | `conn=None`; same overflow as 157 pass, but no service |
| 251 | Shop (THY-Reverse) | — | `conn=None`; binary's `flag()` is empty |

---

## F. Blind pwn — 有伺服器但沒有 binary (live service, no binary)

Live services with no downloadable binary, so exploitation would be blind (unknown
offsets / win addresses). Not feasible without the ELF.

| ID | Challenge | Port | Banner |
|----|-----------|------|--------|
| 244 | pwn_2 | 10009 | "Please enter your name:" (crashes on long input → likely BOF) |
| — | (unidentified) | 10005 | "What your name? / What do you want to say :)?" |

---

## G. 加密變體 / 演算法未確定 (crypto variant undetermined)

| ID | Challenge | Note |
|----|-----------|------|
| 23 | b85 (`:30003`) | dumps a 53-char base85 string on the RFC1924 charset, but no standard variant (ascii85 / base85 / z85 / RFC1924, big/little-endian) decodes to a readable flag — needs the exact custom alphabet |

---

## H. 一般困難的 Web (still-open, not obviously broken)

Surveyed but not yet cracked; these are "hard", not confirmed-broken, and are the best
candidates to revisit.

| ID | Challenge | Port | Where it stands |
|----|-----------|------|-----------------|
| 111 | Admin | 20031 | `login.php` (`user`/`pass`) always returns "wrong"; no SQLi/default-cred worked; no source disclosure found |
| 114 | KAIBRO BUY | 20062 | username-only login (`user`, maxlength 8); all usernames return the login page |
| 119 | Web-2: Easy_Robots.txt | 20028 | `/` → `echo_post.php` "SQL Injection" form (`acc`/`aa`); responses are static (1176 B) regardless of payload |
| 271 | babytrick | 20048 | HITCON Baby^H PHP-deserialization (`?data=` → `unserialize` → `__destruct` calls `login`); needs the multibyte/`utf8_general_ci` trick to log in as `orange` **and** its password — hard, double `mysql_escape_string` |
| 272 | papapa-ubuntu | 20049 | 302 → `https://…/index.php` on every path; "find the secret behind this website (pentesting)"; dirb + XFF/XFP header bypasses found nothing |
| 277 | you-cant-see-me | 20044 | `/user/N` lists 10 cats, no hidden ids, not SSTI (unlike its twin 280) |
| 279 | my-new-router-level 1 | 20050 | RCE achieved (`ip` param, `os.popen(f"ping -c 4 {ip}")`, blacklist only blocks the word `flag`), **but no flag file on the container** — `/root` unreadable, `find` empty; flag delivered by a build step not present at runtime |

---

## Summary counts

- **A. Rejected-despite-solve (platform bug):** 5 ids (227, 230, 233, 153, 123) + RealWorld 273
- **B. Decoy/no-server:** 3 (53, 56, 73)
- **C. Custom-flag mismatch:** 4 (184, 207, 215, 203)
- **D. Need Windows/wine:** 9 (89, 90, 92, 96, 97, 108, 109, 110, 247)
- **E. Service down:** 14 THY-crypto (228-241) + 81, 26, 158, 159, 251
- **F. Blind pwn:** 2 (244, 10005)
- **G. Crypto variant:** 1 (23)
- **H. Hard web (revisit):** 7 (111, 114, 119, 271, 272, 277, 279)

The highest-value follow-ups: give the organiser section **A** (likely real flag-checker
bugs), and provide a **Windows/wine** environment to unlock section **D** (9 challenges).

---

## Removed

- **XSS bot (128 / 262 / 270)** — not blocked. All three plant the flag in the
  visitor's *own* cookie (`session_id()` = flag on 128; `setcookie('passwd', …)` on
  262/270) and the XSS only needs to read `document.cookie`; no admin bot was ever part
  of the design ("此 Demo 只會顯示來自您自己的便利貼"). Flags match `challenge.yml`
  (`BreakALLCTF{BQmpK7Ip0IOxclRg5jex}`, `flag{i_hate_calculus}` ×2). Solved.

---

## challenge.yml flag 修正 (deployed ≠ yml; yml was wrong)

Repo-wide diff of `challenge.yml` flags vs the flag actually baked into `build/`
(flag file / Dockerfile `ENV FLAG` / source). Corrected to match deployment:

| Challenge | old yml | new yml (= deployed) |
|-----------|---------|----------------------|
| 張元_Pwn-6 (`:10002`) | `BreakAllCTF{Scr1pting_skill_is_important_for_a_hacker}` | `BreakAllCTF{A_g00d_h4cker_15_f4m1liar_w1th_b1n4ry_5ystem}` |
| 張元_Pwn-7 (`:10003`) | `…{A_g00d_h4cker_15_f4m1liar…}` | `BreakAllCTF{G00d_j0000000000b:)}` |
| 張元_Pwn-8 (`:10004`) | `…{G00d_j0000000000b:)}` | `BreakAllCTF{NX_pr0t4ct10n_d1sab1e_1s_h4cker_fr1endly}` |
| 張元_Pwn-9 (`:10005`) | `…{NX_pr0t4ct10n_d1sab1e…}` | `BreakAllCTF{Return_to_plt_is_p0werful:D}` |
| THY-Web CTF2024/path_traversal | `flag{path_traversal}` | `flag{read_my_server_qwq}` (twin `path_traversal-freememe` already had this) |
| THY-Web find-method (278, `:20042`) | `FLAG{N0w_u_k0nw_g3t_method}` | `FLAG{Now_u_k0nw_g3t_method_32rfwk}` (`Flag-From-Server` header on `GET /`) |
| THY-Web information_leakage (265, `:20059`) | `flag{information_leakage}` | `flag{git_commit_m_meow}` (first commit of `index.php` in the exposed `.git`) |

`information_leakage` also had a **build bug**: `src/git.zip` was copied into the
webroot as-is, so `/.git/` 404'd and only the raw zip was downloadable. Dockerfile
now `unzip`s it at build time and deletes the archive, so the `.git` dir is the leak.

The Pwn-6..9 yml flags were shifted by one position (each held the previous
challenge's flag); binary themes (`return` / NX-off / `plt`) confirm the deployed
side is correct.

Calc_RSA / 1-/2-Calculate_RSA (227/230/233) went the other way — there the yml was
right and `build/flag` was a placeholder; fixed by editing `build/flag`.

**Still open (yml ≠ deployed, direction undecided):**

- **web-2 Easy_Robots.txt** (153 `:40032`, 119 `:20028`) — both share yml
  `BreakALLCTF{alsidfj2fkJF0falkf9rf}`; instance 153 emits `BreakALLCTF{7QtKB2N5TlqAAEzCrzNO}`,
  instance 119 emits `ACTF{YURXMTYS4C1MiSwjPBZc}`. Neither produces the yml string →
  likely the yml is the true checker value and both files are decoy/stale.
- **CSAW Networking-2** (203) — pcap has `flag{d316759c281bf925d600be698a4973d5}`,
  yml `flag{f9b43c9e9c05be5e08ea163007af5144}`.
- **THY Crypto Playground** (1-ASCII etc.) — client JS flag is `FLAG{sha256(input)}`,
  yml is a static string the service never emits.
