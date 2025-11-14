
### Writing Regular Expression Patterns

Make  your strings raw

```python
r"my pattern"
```

Characters that be escaped
```python

\.   \^   \$   \*   \+   \?   \{   \}   \[   \]   \\   \|   \(   \)

```


### Character Classes

Match one character from a set.

|Pattern|Matches|
|---|---|
|`[abc]`|a, b, or c|
|`[A-Z]`|capital letters|
|`[0-9]`|digits|
|`[a-zA-Z]`|any letter|
|`[^0-9]`|NOT a digit|

Predefined classes:

| Pattern | Meaning                          |
| ------- | -------------------------------- |
| `\d`    | digit                            |
| `\D`    | non-digit                        |
| `\w`    | word char (letters, digits, `_`) |
| `\W`    | not word char                    |
| `\s`    | whitespace                       |
| `\S`    | not whitespace                   |

