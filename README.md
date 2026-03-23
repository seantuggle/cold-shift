# COLD SHIFT

**A text adventure / interactive fiction game of creeping dread set during an overnight museum security shift.**

## Overview

*Cold Shift* is a Python narrative game focused on atmosphere, exploration, object interaction, and parser-driven command input. You play as **Nick Callahan**, a new overnight security guard working through a blizzard while something in the museum slowly becomes harder to explain.

The game combines:

- classic parser-based interaction (`LOOK`, `EXAMINE`, `TAKE`, `READ`, `CALL`, `WAIT`, etc.)
- room-based exploration
- item and container interactions
- light narrative state and recurring event systems
- a distinct voice inspired by classic interactive fiction with modern readability

## Current Structure

From the code currently in the repo, the project is organized around a few core systems:

- `main.py` — game loop, command dispatch, event timing, and narrative responses
- `parser.py` — input parsing and verb normalization
- `player.py` — inventory and player state
- `room.py` — base room model, room descriptions, exits, items, and ambient text
- `items.py` — base item classes and item interaction behavior
- additional modules under `rooms/` and `engine/` are expected by `main.py`

## Features

- **Parser-based input** with verb synonyms and directional commands
- **Room traversal** with long/short descriptions, exits, and ambient messages
- **Interactive objects** including takeable, consumable, and container-style items
- **Narrative event handling** such as radio interruptions, timed dread escalation, and contextual responses
- **Strong character voice** throughout descriptions and command feedback

## Running the Game

Make sure the repository includes all required modules referenced by `main.py`, especially:

- `engine/game_state.py`
- `rooms/security_office.py`
- `rooms/main_lobby.py`

Then run:

```bash
python main.py
```

## Example Commands

```text
look
examine logbook
take radio
call karen
read post-it
reverse note
wait
inventory
go north
```

## Project Status

This project is currently **work in progress**. The core tone, parser structure, and interaction model are already strong, but the repo benefits from continued polish in:

- parser consistency
- command routing cleanup
- inventory/state consistency
- additional room content
- testing and packaging

## Why This Project Is Cool

This project stands out because it is not just a command parser — it already has a clear narrative identity. The writing voice is consistent, the setting is memorable, and the structure is strong enough to grow into a polished interactive fiction game.
