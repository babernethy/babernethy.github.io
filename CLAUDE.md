# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

The source for **bruceabernethy.com** — a Jekyll blog using the
[minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) theme (skin:
`dirt`), deployed to GitHub Pages. Roughly 234 posts spanning 2007–present; the
older ones were migrated from WordPress (many still carry a `dsq_thread_id`
front-matter key from that era).

## Local development

Ruby is pinned by `.ruby-version` (3.4.10) and activated automatically by
`chruby` on `cd` into the repo. If `ruby -v` reports the system 2.6.10, the
chruby hook in `~/.zshrc` did not load — open a new shell.

```bash
bundle install              # first time, or after a Gemfile change
bundle exec jekyll serve --drafts   # http://localhost:4000, includes _drafts
bundle exec jekyll build            # one-shot build into _site/
```

`Gemfile.lock` **is committed** — deliberately. It keeps local builds and CI on
identical gem versions and makes dependency bumps reviewable. Do not add it back
to `.gitignore`.

## Publishing

Push to `main`. `.github/workflows/jekyll.yml` builds with `JEKYLL_ENV=production`
and deploys to Pages. There is no staging environment, so build locally before
pushing. Deploy takes roughly two minutes.

## Writing a post

```bash
bin/new-post "My Post Title"            # -> _posts/YYYY-MM-DD-my-post-title.md
bin/new-post --draft "Half An Idea"     # -> _drafts/half-an-idea.md
```

Both scaffold from `_templates/post.md`. Posts are `_posts/YYYY-MM-DD-slug.md`;
the URL comes from `permalink: /:categories/:title/`, so a post with
`category: "ai"` lands at `/ai/slug/`.

Front matter to fill in on every new post:

| key | notes |
| --- | --- |
| `title` | Quoted. |
| `excerpt` | 1–2 sentences; shown on archive pages and teaser cards. |
| `description` | Meta description. Usually identical to `excerpt`. |
| `category` | **Singular.** One value. See vocabulary below. |
| `tags` | Array. Lowercase. |
| `comments` | `true` |
| `toc` | `true` for anything with `##` sections. |
| `header.teaser` | Path under `/assets/images/`. Drives the archive card image. |
| `header.tagline` | Usually identical to `excerpt`. |

Established vocabulary — reuse these rather than inventing new ones:

- **categories** (11): `ai`, `blog`, `development`, `jobs`, `links`, `nature`,
  `personal`, `physics`, `science`, `tech`, `ui`
- **tags** (35): `ai`, `art`, `birds`, `blog`, `books`, `design`, `development`,
  `ebikes`, `education`, `eink`, `family`, `flutter`, `fun`, `games`, `general`,
  `hardware`, `health`, `home`, `inspiration`, `jobs`, `leadership`,
  `microsoft`, `mobile`, `nature`, `physics`, `popular`, `presentations`,
  `robotics`, `science`, `security`, `silverlight`, `space`, `tech`, `thinking`,
  `ui`

`popular` is a curation marker, not a topic — it flags evergreen posts for
`_pages/popular.md`. `general` is a legacy catch-all carried by the link
roundups; prefer a real topic tag on new posts.

Two overlaps are deliberate, not drift: `physics` (2 posts) predates `science`
and was left in place so its URLs would not move, and the 2024+ link roundups
carry auto-generated tags from their own section headings, so they run wider
than the 1–3 tags a normal post gets.

Images go in `assets/images/` and are referenced from the repo root
(`/assets/images/foo.png`), not relatively.

## Known inconsistencies in existing content

The front-matter backfill pass is done: every post now carries a singular
`category` and 1–3 lowercase `tags` from the vocabulary above. `keywords:`,
bare `tag:`, plural `categories:`, and the `AI`/`dev`/`WPF`/`XAML` casing drift
are all gone.

Because `permalink` is `/:categories/:title/`, giving a post a category moves
its URL. The 202 posts that moved carry a `redirect_from:` with their old path,
served by `jekyll-redirect-from`. **Never remove or change a `redirect_from:`
entry** — it is the only thing keeping 19 years of inbound links alive. If you
change a post's `category`, add the old path to its `redirect_from:` list
rather than replacing it.

## Theme overrides

The theme is a gem, but several files shadow it. Check here before assuming
behavior comes from upstream:

- `_layouts/` — `posts.html` (year-grouped archive that excludes the `links`
  category), `tagpage.html`, `category2.html`, `home.html`, `post_old.html`
- `_includes/` — `archive2-single.html`, `breadcrumbs.html`
- `assets/css/main.scss` — skin import and color variables

## Gotchas

- **`actions/upload-pages-artifact` v4+ silently excludes dotfiles** from the
  deploy artifact. A real `.well-known/` directory would need a hand-built
  artifact. (Bluesky verification currently works via a DNS `TXT` record on
  `_atproto.bruceabernethy.com`, not a served file.)
- `assets/css/main.scss` uses Sass `@import` and the global `mix()` function,
  both removed in Dart Sass 3.0. The warnings are suppressed via `sass.quiet_deps`
  (gem-internal) plus `sass.silence_deprecations: [import, global-builtin]`
  (our own stylesheet) in `_config.yml`, so builds are clean. This is deferral,
  not a fix: the theme's Sass is `@import`-based throughout, so a real migration
  means waiting for minimal-mistakes to ship modules, or vendoring and rewriting
  its ~40 partials. Revisit before Dart Sass 3.0, which will break the build.
- `/categories/links/` is declared by both `_pages/links.md` and
  `_categories/links.html`. Jekyll silently picks one with no warning.
- `_config.yml` declares four collections (`recipes`, `pets`, `portfolio`,
  `category`) that are empty and unused.
