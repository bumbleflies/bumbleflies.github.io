---
name: field-notes-proofread
description: "Use before publishing or updating a Field Notes blog series post (src/content/blog/*.md) to proofread it for AI-generated rhetoric ('AI slop'), tone/voice consistency, and house style. Apply the same edits to both the DE and EN language files."
---

# Field Notes Proof-Read

A line-by-line editorial pass for the "Field Notes" blog series (the KI-Agenten-Betriebssystem / AI-agent-operating-system posts and their siblings). Distilled from an actual editing pass on `ki-agenten-betriebssystem.md` / `ai-agent-operating-system.md`.

## Process

1. Read the **published** post top to bottom (not just the diff) and classify every sentence:
   - **KEEP** — leave it.
   - **TIGHTEN** — right idea, sharpen the wording.
   - **REWRITE** — the idea's fine, the phrasing isn't.
   - **CUT** — generic filler or AI-slop, adds nothing.
   - **WATCH** — technically or rhetorically questionable; flag rather than silently fix (see Escalate below).
2. Apply edits to the language file you're proofreading.
3. **Mirror every edit to the other language file.** DE and EN posts are paired by `order` (see `src/content/blog/AGENTS.md`); a fix in one that isn't ported to the other creates drift a reader or the next editor won't expect.
4. Do a **final fresh read** of the whole post after all edits — not just the touched lines. Coordinated multi-step edits routinely produce new problems the line-level view can't see (see Cross-cutting checks below).
5. Run `npm run build` (or `astro check`) before calling it done — a frontmatter quote fix can silently break YAML parsing (see Gotcha below).

## Red flags — cut or rewrite on sight

- **Throat-clearing openers**: "The most important sentence first, because it explains everything else." State the sentence; don't announce it.
- **Empty value-signaling**: "They are the real value, and the thread running through this series." Says nothing concrete — cut.
- **Generic thought-leadership closers**: "None of this is a blueprint to copy." Consulting-speak — cut, let the next (concrete, self-doubting) sentence stand alone.
- **Generic marketing CTAs**: "Sounds like a topic that moves you too?" Reads like a different, worse author took over — cut.
- **Stacked metaphors**: this series already runs on "foundations / pillars / nervous system / cockpit." Don't add another metaphor system on top ("connective tissue," "a network with load-bearing seams," "two perpendicular foundations"). One metaphor family per post; describe mechanism in plain language everywhere else.
- **Unfalsifiable absolutes**: "It improvises, and improvises a little differently every time" invites an easy technical objection. Prefer a specific, defensible claim ("it doesn't automatically know your deployment pipeline; it has to infer it from context").
- **Vague growth metaphors**: "From this one idea grew a multi-layered operating system." Say what actually happened in concrete terms instead.

## Always preserve

- Concrete numbers and specifics (workflow counts, plugin counts, dated incidents) — these are the strongest anti-slop signal in the piece.
- Real quotes and slightly imperfect human phrasing (a customer's actual words, a self-deprecating aside) — don't polish the humanity out of them.
- Short, punchy declarative sentences that land the thesis.
- Self-aware or vulnerable admissions ("there are decisions in here I'm still not sure about").

## House style (see also `beta/CLAUDE.md`)

- **No em dashes.** Use a period, comma, colon, semicolon, or parentheses instead.
- **German quotes**: „ for the opening mark, a plain straight `"` for the closing mark, matching this series' existing body-text convention (not the typographically "correct" „…" pair).
- **German CTAs use `du`**, not `Sie`.

## Gotcha: frontmatter quotes break YAML

`description` (and other frontmatter strings) are YAML double-quoted scalars. If a rewritten description embeds a literal ASCII `"` as a closing quote mark (matching the body-text convention above), it **collides with the YAML delimiter** and breaks content sync with an opaque error ("bad indentation of a mapping entry"). Either:
- escape it as `\"`, or
- keep the frontmatter convention of plain `'single quotes'` for embedded quotes (avoids the whole class of bug).

Always run `npm run build` after touching frontmatter to catch this — `astro check`'s content-sync step will fail loudly if it's broken, silently succeed if it isn't.

## Cross-cutting checks (do these on the final read, not per-line)

- **Pronoun/credit consistency.** If a rewrite adds team credit ("we built this, my colleagues and I"), it must not immediately collide with an adjacent sentence re-claiming solo authorship of the *same* act ("I built this system..."). One acknowledgment near the top is enough; the rest of the post can stay first-person-singular *if* it's framed as personal account/decisions, not a repeated build claim.
- **Duplicate content across adjacent paragraphs.** Edits made independently (e.g., moving a phrase into paragraph A, then separately rewording paragraph B) can leave two paragraphs asserting the same fact back to back. Merge them; don't let both survive.
- **Repeated words in adjacent sentences.** E.g. "...design principles appear. These principles run through..." reads clumsy — combine into one sentence.
- **Deliberate callbacks are good, keep them.** E.g. this series intentionally echoes "traces back to a concrete/dated incident" in both the intro and the principles section — that repetition is a feature, not a bug. Don't flatten intentional echoes while hunting for accidental ones.

## Escalate instead of guessing

Some review items are bigger than a wording fix and should go back to the user as a question, not get applied unilaterally:
- **Structural reordering** (e.g., moving a concrete example earlier than the architecture explanation).
- **Shared template copy** (CTA text, AI-disclosure note) that lives outside the content file, in `src/pages/blog/[slug].astro`, and therefore affects every post in the series, not just the one being proofread.
