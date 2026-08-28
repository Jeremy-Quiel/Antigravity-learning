# Language and Communication Rules

## 1. Purpose
Establish English as the official language to ensure global consistency, standard code conventions, clear documentation, and maintainability across the repository.

## 2. Scope
Applies to all autonomous agent responses, technical documentation files (`.md`), source code identifiers, comments and docstrings, as well as Git commit messages.

## 3. Core Rules

| Scope | Required Language | Directive |
| :--- | :--- | :--- |
| **Agent Responses & Communication** | English | All explanations, reports, answers, and interactions must be written in English by default. |
| **Technical Documentation** | English | Manuals, `README.md` files, architectural notes, and project rule files must be written in English. |
| **Code Comments & Docstrings** | English | All inline comments, function/class docstrings, and type annotations must be documented in English. |
| **Git Commit Messages** | English | All Git commits must be written in English following the *Conventional Commits* specification (e.g., `feat:`, `fix:`, `docs:`, `chore:`). |
| **Code Nomenclatures & Identifiers** | English | Variable names, function names, classes, constants, and module names must use standard English terminology. |

## 4. Exceptions
* **Explicit User Requests:** When the user explicitly requests another language for a specific output, translation, or task.
* **Domain-Specific Constants / Data:** Literal text or external dataset values that inherently exist in other languages.

## 5. Examples

### Code Documentation
```python
def calculate_total(subtotal: float, tax_rate: float) -> float:
    """Calculate the total amount after applying the tax rate.

    :param subtotal: Base amount before taxes.
    :param tax_rate: Decimal representation of the tax percentage.
    :return: Final calculated total.
    """
    # Calculate tax and add to subtotal
    tax_amount = subtotal * tax_rate
    return subtotal + tax_amount
```

### Git Commit Messages
* `feat: add binary search tree implementation`
* `docs: update README with model specifications`
* `fix: correct numeric validation in interactive calculator`
