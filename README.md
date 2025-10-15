# Part 3 — Starter (Executable Spec)

No descriptive exercise text. The spec is the **golden transcript** in
`part3/tests/snapshot_interaction.txt`.

Students should implement an extension of the current search. The user can enter multiple words to search. Those words are separated by white space (space, tabs, ...). Instead of searching the sonnets for one word, all words given by the user must be present in the sonnet.

As in part 2, when printing the results the words are highlighted in the sonnets and only the matching sonnets are printed.

## Run the app

```bash
python -m part3.app
```

## Check against the transcript

```bash
python -m part3.tests.check_transcript
```

## Where to work

Edit `part3/app.py`:
- In `find_spans`: **Copy your solution from part 2**.
- Around line 113: **extend the search** so the app accepts multiple words and shows only sonnets that contain *all* of them (logical AND). Split the raw input into words, search per word, and combine results before handing them to `print_results`.
