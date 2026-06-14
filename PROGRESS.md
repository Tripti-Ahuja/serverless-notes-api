# Progress Log

## Day 1
- Set up repo structure via Python script
- Next: Write basic Note class with create/read functions

## Day 1 — Completed ✅
- Created repo structure via Python script (pathlib, dict-driven setup)
- Initialized Git, pushed to GitHub
- Next: Build Note class with create/read methods

## Day 2 — Completed ✅
- Built Note and NotesStore classes
- Implemented create, get_all, get_by_id
- Learned: __init__, self, type hints, list comprehensions
- Next: Add update and delete (the U and D in CRUD)

## Day 3 — Completed ✅
- Added update() and delete() methods
- Full CRUD now working in memory
- Learned: default parameters, `is not None`, graceful error handling
- Next: Add input validation and write proper tests

## Day 4 — Completed ✅
- Added ValidationError custom exception class
- Validated input in create() — empty/whitespace titles and content now rejected
- Removed accidental `turtle` auto-import (dead code cleanup)
- Added count() method to NotesStore using built-in len()
- Added __str__ method to Note for readable print output
