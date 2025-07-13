# 🧊 Cubix3D: A Cube-Based Esolang

Cubix3D is a Turing-complete language where you **program by rotating a cube**.  
Each face of the cube represents a different **operation**, and values are stored in a fixed 3×3 grid per face.

## 🧠 Design Philosophy

- The cube is **fixed in memory**
- You always operate on the center cell of the **Front face**: `F[1][1]`
- Rotating the cube moves values between faces, **applying functions along the way**
- Each face has its own **behavior** when it becomes the Front

---

## 🧩 Face Behaviors

| Face | Meaning when rotated to Face                      |
|------|---------------------------------------------------|
| `F`  | No-op (identity)                                  |
| `B`  | Changes output mode between letters and numbers   |
| `U`  | Loads a value (or acts as input buffer)           |
| `D`  | Sends value to output                             |
| `L`  | Applies increment                                 |
| `R`  | Applies decrement                                 |

Use `X`, `Y`, `Z` to rotate the **entire cube**, and `F`, `R`, `L`... to rotate individual **faces**.

You can also use `'` (apostrophe) to rotate **counterclockwise**:

| Command | Meaning               |
|---------|------------------------|
| `X`     | Rotate cube around X                 |
| `X'`    | Rotate X CCW                         |
| `R`     | Rotate Right face Clockwise          |
| `R'`    | Rotate Right face Counter-clockwise  |
---

## 🎮 Commands

| Symbol  | Action                                                  |
|---------|---------------------------------------------------------|
| `X`     | Rotate entire cube around X axis (clockwise)            |
| `X'`    | Rotate entire cube around X axis (counterclockwise)     |
| `Y`     | Rotate entire cube around Y axis (clockwise)            |
| `Y'`    | Rotate entire cube around Y axis (counterclockwise)     |
| `Z`     | Rotate entire cube around Z axis (clockwise)            |
| `Z'`    | Rotate entire cube around Z axis (counterclockwise)     |
| `F`     | Rotate Front face clockwise                             |
| `F'`    | Rotate Front face counterclockwise                      |
| `B`     | Rotate Back face clockwise                              |
| `B'`    | Rotate Back face counterclockwise                       |
| `U`     | Rotate Up face clockwise                                |
| `U'`    | Rotate Up face counterclockwise                         |
| `D`     | Rotate Down face clockwise                              |
| `D'`    | Rotate Down face counterclockwise                       |
| `L`     | Rotate Left face clockwise                              |
| `L'`    | Rotate Left face counterclockwise                       |
| `R`     | Rotate Right face clockwise                             |
| `R'`    | Rotate Right face counterclockwise                      |
| `+`     | Apply current face’s effect (e.g., L = +1)              |
| `-`     | Opposite of current face’s effect                       |
| `.`     | Output front center cell as ASCII                       |
| `,`     | Input a character into front center                     |
| `[` `]` | Loops: while front center ≠ 0                           |
| `d`     | Dump front face grid                                    |
| `i`     | Debug: show full cube state                             |


---

## 🌀 Sample Program: Increment and Output

This program:
1. Loads from `U`
2. Rotates to `L` to increment
3. Rotates to `D` to output

```text
U L + D .
```

---

## 🧠 Implementation Notes

- All data is stored as integers (0–255)
- Only `F[1][1]` is operated on
- You can extend face behaviors (`R` = XOR, `L` = bitshift, etc.)
- Program state is fully visible via debug mode

---

## 💡 Future Extensions

- Face functions can be **programmable**
- Stack-based memory (map B as a stack?)
- Multiple pointer modes
- Cube macros: define movement sequences

---

> Built for the Hack Club esolang challenge  
> By: Xiangrui ✨

