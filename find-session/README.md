# find-session

Pin a specific Claude Code conversation by UUID and resume it with a one-word shell command.

## What it solves

`claude --continue` picks the *most recent* conversation in the current directory — unreliable when:

- You have multiple long-running parallel conversations in the same project
- You started Claude Code from `~` (so all your sessions live in the home-dir bucket)
- The "most recent" jumps around as you switch tasks

`claude --resume <uuid>` is exact, but you have to find the right UUID, and there can be more than one Claude instance claiming the same one.

This skill walks Claude through the right grep-the-jsonl workflow, then pins the verified UUID as a `~/.zshrc` shell function so you can type e.g. `headsup` from any new terminal and land in the exact same conversation.

## When to use

- "I can't find my conversation" / "claude --continue picks the wrong one"
- "I want a one-word command to resume my long-running [project] session"
- Multiple `.jsonl` files exist under `~/.claude/projects/<encoded-cwd>/`

## How to invoke

```
我找不到我的对话, 帮我找出来
```

or explicitly:

```
/find-session
```

The skill will:

1. List `~/.claude/projects/*/` and find the most recently active bucket
2. List all `.jsonl` files in that bucket (each = one conversation)
3. Ask you for a unique-content hint (a filename, URL, function name only this conversation would contain)
4. `grep -c` that string across every `.jsonl` to identify the right one
5. Confirm UUID, ask for a short alias name (e.g. `aichain`, `headsup`, `work`)
6. Append a function to `~/.zshrc`:

   ```bash
   <name>() {
     cd "$HOME" && claude --resume "<uuid>"
   }
   ```

7. Tell you to `source ~/.zshrc` (or open a new terminal) — done.

## Why grep-not-size

The biggest `.jsonl` is **not** necessarily yours. Multiple Claude Code processes can attach to the same conversation file simultaneously and any of them might be confused about which UUID it lives under. Only matching against unique content you remember writing or generating is reliable.

## Why `cd "$HOME"`

Sessions are indexed by their **starting** cwd, not by where the work happened. A session started from `~` lives under `~/.claude/projects/-Users-yourname/`, even if the conversation cd'd into a project subdirectory. The alias must `cd "$HOME"` so `claude --resume <uuid>` looks in the right project bucket.

## License

MIT — see repo root.
