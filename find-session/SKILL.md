---
name: find-session
description: Identify a specific Claude Code conversation by its UUID and optionally pin it as a shell function for one-word resume. Use when "claude --continue" picks the wrong session, or when the user wants to reliably resume a specific past conversation across reboots.
---

# find-session — pin a specific Claude conversation

`claude --continue` picks "most recent in cwd" — unreliable when multiple
sessions share a directory. `claude --resume <uuid>` is exact. This skill
finds the right UUID by grepping jsonl files, then writes a one-word shell
function so the user types e.g. `aichain` to resume that exact conversation.

## When to use

- User says "I can't find my session" / "claude --continue picks wrong one"
- User wants a one-word resume command for a specific long-running conversation
- Multiple `.jsonl` files in `~/.claude/projects/<encoded-cwd>/` exist

## Workflow

### 1. Find the encoded-cwd directory

Sessions are stored under `~/.claude/projects/<encoded-cwd>/`. The encoding
replaces `/` with `-`, so cwd `/Users/foo/Desktop/MyProj` becomes
`-Users-foo-Desktop-MyProj`. Often the cwd at session-start was the user's
HOME, even if work happened in a subdirectory.

If unsure which encoded-cwd to scan:

```bash
ls -dt ~/.claude/projects/*/ | head -5
```

The most recently modified directory is likely the right one.

### 2. List active session files

```bash
ls -lt ~/.claude/projects/<encoded-cwd>/*.jsonl 2>/dev/null | head -10
```

Multiple files = multiple sessions. **The biggest by size is NOT
necessarily the right one** — both the current assistant and other parallel
sessions can be wrong about that.

### 3. Get a unique-content hint from the user

Ask: "What's something only this conversation would contain? A specific
filename you created, a unique tool you ran, a project name, etc."

Good hints (highly unique):
- A hostname / URL the conversation generated (e.g. `waqvu5.png`)
- A file path that was created by this session (e.g. `kimi_research_results`)
- A specific function name written in this session (e.g. `compute_factor_scores`)
- A unique error message they remember

Bad hints (too common, will match multiple):
- Generic words like "Python", "test", "fix"
- Common library names

### 4. grep to find matching session

```bash
for f in ~/.claude/projects/<encoded-cwd>/*.jsonl; do
  echo "=== $(basename "$f") ==="
  grep -c "<unique-string>" "$f" 2>/dev/null
done
```

The session with non-zero hits (ideally many hits) is the answer. Confirm
with 2-3 different unique strings if the first match is ambiguous.

### 5. Offer to pin as shell function

Once UUID is identified, ask user for a short name (e.g. `aichain`,
`work`, `headsup`). Then append to `~/.zshrc`:

```bash
# <project description> — resume specific session
<short-name>() {
  cd "$HOME" && claude --resume "<uuid>"
}
```

`cd "$HOME"` matters: sessions are indexed by their starting cwd, so the
alias must cd to the same place where the session was originally created
(often HOME, even if the actual work touched subdirectories).

After write, tell user to either:
- Run `source ~/.zshrc` in current terminal, OR
- Open a new terminal

## Important notes

- Each `.jsonl` is the full transcript log of one session. Sizes can mislead;
  always rely on grep'd content matches, not file size.
- The UUID is stable forever — once pinned, the alias keeps working across
  reboots, OS upgrades, even years (assuming the .jsonl isn't deleted).
- If user has multiple long-running parallel sessions (e.g., two different
  projects, both started from HOME), each needs its own pin. Repeat the
  workflow once per session.
- Don't confuse session UUIDs across different conversations. If two Claude
  instances both claim the same UUID, at least one is wrong — only grep on
  actual unique content can verify.

## Quick check

After pinning, verify:

```bash
source ~/.zshrc && type <short-name>
```

Should show the function definition.
