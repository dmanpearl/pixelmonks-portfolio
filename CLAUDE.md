# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A shared media and static assets directory for the Pixelmonks portfolio projects. It contains no source code — only PNG images (logos and screenshots).

## Referenced Projects

- **breaking-news** — Django ASGI broadcast system that dispatches messages to Discord and Slack (`/Users/dmanpearl/pixelmonks/breaking-news/`)
- **la-surfing-school** — Django marketing/booking site with Stripe payments (`/Users/dmanpearl/pixelmonks/la-surfing-school/`)
- **rating-ranch** — Django sports ratings application (`/Users/dmanpearl/pixelmonks/phoenix/alliancesports/rating-ranch/`)

## Structure

```
media/projects/{project-name}/   # logos and screenshots per project
static/images/logo.png           # main branding logo
```

## Constraints

Only `find` Bash commands are permitted in this directory (see `.claude/settings.local.json`). There is no build process, no package manager, and no test suite — this is a static assets directory only.
