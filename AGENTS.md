# Project Rules Configuration

This document centralizes and integrates all policies, behavioral guidelines, and development standards governing autonomous agents and workflows within this repository.

## Active Rule Modules

The following modularized rules are imported and enforced:

@import .agents/rules/git.md
@import .agents/rules/idioma.md
@import .agents/rules/formatoCodigo.md

## Workflofs Modules

The following modularizes workflows are imported and enforced:

@import .agents/workflows/debug.md

## Agent Output Policy

**Output Format:** Execute the task. Display executed commands (if any) and relevant errors in standard output. Upon completion, provide a very short summary (maximum 1 paragraph) explaining what was changed or done. Do not display full file contents or complete code unless strictly necessary for the summary.
