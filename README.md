# Part 3 — Starter (Executable Spec)

No descriptive exercise text. The spec is the **golden transcript** in
`part3/tests/snapshot_interaction.txt`.

Students should implement an extension of the current search. The user can enter multiple words to search. Those words are separated by white space (space, tabs, ...) - ToDo 1. 
Instead of searching the sonnets for one word, all words given by the user must be present in the sonnet. ToDo 2 is to merge search results for a sonnet, e.g., the search result for "summer" with the search result for "day".

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
- ToDo 1: At line 7: Copy your solution from part 2 into `find_spans`
- ToDo 2: At line 122: Split the string on white space
- ToDo 3: At line 74: Implement function `combine_results` to merge two search results
