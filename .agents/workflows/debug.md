# Debug Workflow

## Purpose
Standardized process for diagnosing and fixing bugs in this Python codebase in a reproducible and traceable way.

## Trigger
Use this workflow when: tests fail, unexpected runtime errors, incorrect output, or bug reports.

## Workflow

### 1. Triage and Context
- Identify the symptom: error message, stack trace, expected vs actual behavior.
- Locate affected module(s): `calculadora.py`, `arbol_binario_busqueda.py`, or other.
- Check recent changes: `git log --oneline -10` and `git diff main...HEAD`.
- Classify severity: blocker / major / minor and reproducibility: always / intermittent.

### 2. Reproduce
- Create minimal reproduction before touching source code.
- Prefer a standalone script `reproduce_issue.py` or a failing test case:
  ```bash
  python3 reproduce_issue.py
  # or
  python3 -m pytest tests/test_regression.py -v
  # or direct module execution
  python3 calculadora.py
  python3 arbol_binario_busqueda.py
  ```
- Confirm the error is deterministic. Capture full output: traceback, inputs, Python version (`python3 --version`).
- If not reproducible, log environment details and close as `cannot-reproduce` with evidence.

### 3. Isolate Root Cause
- Narrow scope with binary search / divide and conquer: comment out, add prints/logging, or use `pdb`/`breakpoint()`.
- Inspect logs and stack trace top-down: entry point -> failing function -> failing line.
- Validate assumptions:
  ```bash
  python3 -c "import ast; ast.parse(open('calculadora.py').read()); print('syntax ok')"
  python3 -m py_compile calculadora.py arbol_binario_busqueda.py
  ```
- Check common causes: invalid input handling, type errors, off-by-one, missing edge cases (e.g., `divide(..., 0)`, `factorial(-1)`), BST invariants.
- Document root cause in one sentence: "Root cause is X in `file:line` because Y".

### 4. Fix
- Apply minimal, focused fix — do not refactor unrelated code.
- Respect project rules: `AGENTS.md` and `.agents/rules/formatoCodigo.md` (if exists).
- Add defensive checks and clear error messages where applicable.
- If fix requires API change, update callers and `README.md`/`USER.md`.

### 5. Verify
- Rerun reproduction script — must pass.
- Run relevant existing checks:
  ```bash
  python3 -m pytest -v
  # or manual smoke tests if no test suite
  python3 -m py_compile calculadora.py arbol_binario_busqueda.py
  python3 arbol_binario_busqueda.py
  ```
- Add/update regression test covering the bug and edge cases.
- Test edge cases explicitly: empty input, zero, negative, large values, duplicate BST inserts.

### 6. Cleanup and Commit
- Remove temporary reproduction files or move them to `tests/` if kept as regression.
- Follow `.agents/rules/git.md`: atomic commit with Conventional Commits:
  ```bash
  git status
  git add <files>
  git commit -m "fix: description of bug and root cause"
  git push origin <current_branch>
  ```
- Reference issue ID in commit body if applicable.

## Output Required
Upon completion, report:
- Root cause (`file:line` + reason)
- Fix applied
- Verification command and result (pass/fail)

## Anti-patterns
- Fixing without reproducing first.
- Large unrelated refactors in a bugfix commit.
- Suppressing exceptions with `except: pass` instead of handling the cause.
