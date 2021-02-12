# Plan 9 Plumbing for Sublime Text

This package implements Plan 9 plumbing for Sublime Text.

## Design

This package is designed to work with the `plumber(4)` provided by [plan9port](https://9fans.github.io/plan9port/).

How to interface with the `plumber(4)`?

1. Just run `plumb(1)`
2. Determine namespace and write via `9p(1)`)
3. Expect `/mount/plumb/send` to exist and just `write(2)` to it

The first solution is the simplest to implement and already does the right thing,
although it requires external processes and doesn't use any special capabilitues.
The second solution gives more flexibility,
but it is not clear yet if it is worth the extra work.
Also,
it still requires an external process.
The third solution is quite simple from an implementation standpoint,
but it requires a properly setup environment.
This is especially problematic since the support for per program namespaces and user mounts on Linux is horrible.

For now,
solution 1 is selected,
although I would strongly prefer solution 3.

## TODO

- Update rules after editing
