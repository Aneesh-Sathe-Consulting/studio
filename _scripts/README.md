# _scripts

## mint_dois.py — self-minted Rogue Scholar DOIs

Runs automatically as a Quarto **pre-render** hook (see `pre-render` in
`../_quarto.yml`). Before each render it walks `posts/*/` and, for any post that
doesn't already have a DOI, writes a stable `10.59350/…` DOI into that post's
`_metadata.yml`. Rogue Scholar then registers the DOI you supplied rather than
minting its own.

**Behaviour**
- Idempotent: an existing `doi:` is never changed.
- Opt-out: a post whose `_metadata.yml` contains `mint_doi: false` is skipped
  (used for `8 Causality From Day One`, which was published before this pipeline
  and gets a Rogue-Scholar-generated DOI instead).
- Safe: the script never raises and always exits 0, so it cannot break a build.
- No required dependencies (stdlib only). If `commonmeta-py` is installed it is
  used for an exact-format suffix; otherwise a compatible one is generated.

**For post 1:** when its Rogue Scholar DOI shows up on your blog page, paste it
into `posts/8 Causality From Day One/_metadata.yml` and remove the `mint_doi`
line. That makes it permanent and self-managed like the others.

**Publishing note:** `publish.sh` runs a full `quarto render`, which also tries
to *execute* the older `.ipynb` posts (they have no `_freeze/` cache). To publish
a new Markdown post without touching the notebooks, render just that post and the
index, e.g.:

```bash
quarto render "posts/NN Title/Your Post.md"   # also re-renders index.qmd (listing + feed)
git add "posts/NN Title" docs && git commit -S -m "Publish: …" && git push
```
