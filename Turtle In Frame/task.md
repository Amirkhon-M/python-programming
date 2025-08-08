# 🐢 Framing the Word "Turtle"

## 📋 Task Description

You need to create a **frame** around the word `Turtle` using a **given character** as the filler. The **frame must be 10 characters wide**.

Use the **string duplication operation** (repeating strings using `*`) to build the frame.

---

## 📥 Input Format

You are given **a single character**, which will be used to **build the frame**.

---

## 📤 Output Format

You must output the word `Turtle`, surrounded by a **10-character-wide frame**, as shown in the example below.

---

## 📌 Example

### Input
```
*
```

### Output
```
**********
*        *
* Turtle *
*        *
**********
```

---

## 💡 Hint

Use string multiplication to build repeated characters:

```
char = '*'
print(char * 10)  # Output: **********
```

To align the word properly in the center row, note that:

- There are 10 characters in total per line.
- The line with "Turtle" has 1 space on each side and is enclosed with the border character.