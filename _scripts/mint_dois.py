#!/usr/bin/env python3
"""
Self-mint Rogue Scholar DOIs for Studio posts (Quarto pre-render hook).

For each post directory under posts/ that contains a single post file and has
no DOI yet, assign a stable DOI under the Rogue Scholar prefix 10.59350 and
store it in that directory's _metadata.yml. Rogue Scholar then registers the
DOI you supplied (instead of generating its own) when it ingests the feed.

Guarantees:
  * Idempotent — an existing `doi:` is never changed.
  * Opt-out — a directory whose _metadata.yml has `mint_doi: false` is skipped
    (used for posts already published with a Rogue-Scholar-generated DOI).
  * Safe — never raises; always exits 0 so it cannot break `quarto render`.
  * No hard dependencies — uses only the stdlib. If `commonmeta-py` happens to
    be installed it is used for an exact-format suffix; otherwise a compatible
    Crockford-base32 suffix is generated locally.

Wired via `project: pre-render:` in _quarto.yml, so it runs on every render.
"""
import os
import sys
import glob
import secrets

PREFIX = "10.59350"
POSTS_DIR = "posts"
OUTPUT_DIR = "docs"   # Quarto output-dir; a post already rendered here is "published"
POST_EXTS = (".qmd", ".md", ".ipynb")
# Crockford base32 (no i, l, o, u) — matches Rogue Scholar's DOI suffix style.
CROCKFORD = "0123456789abcdefghjkmnpqrstvwxyz"


def gen_suffix():
    """Return a DOI suffix like '9ydw5-3vt28'."""
    try:
        from commonmeta import encode_doi  # type: ignore
        doi = encode_doi(PREFIX)
        if doi and "/" in doi:
            return doi.split("/", 1)[1]
    except Exception:
        pass
    g = lambda n: "".join(secrets.choice(CROCKFORD) for _ in range(n))
    return f"{g(5)}-{g(5)}"


def read_meta_flags(meta_path):
    """Return (has_doi, opted_out) by scanning an existing _metadata.yml."""
    has_doi, opted_out = False, False
    if not os.path.exists(meta_path):
        return has_doi, opted_out
    try:
        with open(meta_path, encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s.startswith("#"):
                    continue
                if s.startswith("doi:") and s.split(":", 1)[1].strip():
                    has_doi = True
                if s.replace(" ", "").lower() == "mint_doi:false":
                    opted_out = True
    except Exception:
        # Unreadable -> treat as "do not touch".
        return True, True
    return has_doi, opted_out


def post_files(d):
    return [n for n in os.listdir(d)
            if n != "_metadata.yml" and n.lower().endswith(POST_EXTS)]


def already_published(d):
    """True if this post already has rendered HTML in the output dir.

    Self-minting is only for posts not yet published; already-live posts get a
    DOI from Rogue Scholar, and retro-assigning one here would clash.
    """
    out = os.path.join(OUTPUT_DIR, POSTS_DIR, os.path.basename(d))
    return bool(glob.glob(os.path.join(out, "*.html")))


def main():
    if not os.path.isdir(POSTS_DIR):
        return
    minted = 0
    for d in sorted(glob.glob(os.path.join(POSTS_DIR, "*"))):
        if not os.path.isdir(d):
            continue
        files = post_files(d)
        if not files:
            continue
        meta = os.path.join(d, "_metadata.yml")
        has_doi, opted_out = read_meta_flags(meta)
        if has_doi or opted_out:
            continue
        if already_published(d):
            continue
        if len(files) > 1:
            sys.stderr.write(f"[mint_dois] skip (multiple post files): {d}\n")
            continue
        doi = f"{PREFIX}/{gen_suffix()}"
        try:
            pad = "\n" if (os.path.exists(meta) and os.path.getsize(meta) > 0) else ""
            with open(meta, "a", encoding="utf-8") as f:
                f.write(pad)
                f.write("# Auto-minted Rogue Scholar DOI — permanent once registered; do not change.\n")
                f.write(f'doi: "{doi}"\n')
            minted += 1
            sys.stderr.write(f"[mint_dois] assigned {doi} -> {d}\n")
        except Exception as e:
            sys.stderr.write(f"[mint_dois] could not write {meta}: {e}\n")
    if minted:
        sys.stderr.write(f"[mint_dois] minted {minted} new DOI(s)\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # never break the build
        sys.stderr.write(f"[mint_dois] non-fatal error: {e}\n")
    sys.exit(0)
