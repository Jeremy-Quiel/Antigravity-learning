# Code Formatting Rules

## 1. Purpose
Define uniform code formatting standards across all source code files in the project to ensure readability, maintainability, and consistency.

## 2. Scope
Applies to all source code files generated or maintained by autonomous agents and developers in this repository.

## 3. Core Rules
- **Indentation:** All generated code must strictly use **2 spaces** of indentation per level. No tabs, and no other indentation sizes (e.g., 4 spaces are not permitted).

## 4. Examples

### Python (2 spaces)
```python
def calculate_sum(a: int, b: int) -> int:
  """Calculate the sum of two integers."""
  result = a + b
  return result
```