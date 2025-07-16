class Cubix {
    constructor(size = 3) {
      this.n = size;
      this.mid = Math.floor(this.n / 2);
      this.faces = {
        F: this.makeFace(),
        B: this.makeFace(),
        U: this.makeFace(),
        D: this.makeFace(),
        L: this.makeFace(),
        R: this.makeFace(),
      };
      this.positionMap = {
        F: "F",
        B: "B",
        U: "U",
        D: "D",
        L: "L",
        R: "R",
      };
      this.x = this.mid;
      this.y = this.mid;
    }
  
    makeFace() {
      return Array(this.n)
        .fill(null)
        .map(() => Array(this.n).fill(0));
    }
  
    rotateCubeFaces(axis, clockwise) {
      const p = this.positionMap;
      if (axis === "X") {
        if (clockwise) {
          [p.F, p.D, p.B, p.U] = [p.D, p.B, p.U, p.F];
        } else {
          [p.F, p.U, p.B, p.D] = [p.U, p.B, p.D, p.F];
        }
      } else if (axis === "Y") {
        if (clockwise) {
          [p.L, p.B, p.R, p.F] = [p.B, p.R, p.F, p.L];
        } else {
          [p.L, p.F, p.R, p.B] = [p.F, p.R, p.B, p.L];
        }
      } else if (axis === "Z") {
        if (clockwise) {
          [p.U, p.R, p.D, p.L] = [p.L, p.U, p.R, p.D];
        } else {
          [p.U, p.L, p.D, p.R] = [p.R, p.U, p.L, p.D];
        }
      } else {
        throw new Error(`Unknown axis: ${axis}`);
      }
    }
  
    rotateFace(face, clockwise) {
      const F = this.faces.F,
        R = this.faces.R,
        B = this.faces.B,
        L = this.faces.L,
        U = this.faces.U,
        D = this.faces.D;
      const n = this.n;
  
      // Rotate the face matrix itself
      if (clockwise) {
        this.faces[face] = this.faces[face]
          .map((_, i) => this.faces[face].map((row) => row[i]))
          .map((row) => row.reverse());
      } else {
        this.faces[face] = this.faces[face]
          .map((_, i) => this.faces[face].map((row) => row[i]))
          .reverse();
      }
  
      // Rotate adjacent edges depending on face and direction
      if (clockwise) {
        if (face === "U") {
          let tmp = F[0].slice();
          F[0] = L[0].slice();
          L[0] = B[0].slice();
          B[0] = R[0].slice();
          R[0] = tmp;
        } else if (face === "D") {
          let tmp = F[n - 1].slice();
          F[n - 1] = R[n - 1].slice();
          R[n - 1] = B[n - 1].slice();
          B[n - 1] = L[n - 1].slice();
          L[n - 1] = tmp;
        } else if (face === "L") {
          let tmp = U.map((row) => row[0]);
          for (let i = 0; i < n; i++) {
            U[i][0] = B[n - 1 - i][n - 1];
            B[n - 1 - i][n - 1] = D[i][0];
            D[i][0] = F[i][0];
            F[i][0] = tmp[i];
          }
        } else if (face === "R") {
          let tmp = U.map((row) => row[n - 1]);
          for (let i = 0; i < n; i++) {
            U[i][n - 1] = F[i][n - 1];
            F[i][n - 1] = D[i][n - 1];
            D[i][n - 1] = B[n - 1 - i][0];
            B[n - 1 - i][0] = tmp[i];
          }
        } else if (face === "F") {
          let tmp = U[n - 1].slice();
          for (let i = 0; i < n; i++) {
            U[n - 1][i] = L[n - 1 - i][n - 1];
            L[n - 1 - i][n - 1] = D[0][n - 1 - i];
            D[0][n - 1 - i] = R[i][0];
            R[i][0] = tmp[i];
          }
        } else if (face === "B") {
          let tmp = U[0].slice();
          for (let i = 0; i < n; i++) {
            U[0][i] = R[i][n - 1];
            R[i][n - 1] = D[n - 1][n - 1 - i];
            D[n - 1][n - 1 - i] = L[n - 1 - i][0];
            L[n - 1 - i][0] = tmp[i];
          }
        }
      } else {
        if (face === "U") {
          let tmp = F[0].slice();
          F[0] = R[0].slice();
          R[0] = B[0].slice();
          B[0] = L[0].slice();
          L[0] = tmp;
        } else if (face === "D") {
          let tmp = F[n - 1].slice();
          F[n - 1] = L[n - 1].slice();
          L[n - 1] = B[n - 1].slice();
          B[n - 1] = R[n - 1].slice();
          R[n - 1] = tmp;
        } else if (face === "L") {
          let tmp = U.map((row) => row[0]);
          for (let i = 0; i < n; i++) {
            U[i][0] = F[i][0];
            F[i][0] = D[i][0];
            D[i][0] = B[n - 1 - i][n - 1];
            B[n - 1 - i][n - 1] = tmp[i];
          }
        } else if (face === "R") {
          let tmp = U.map((row) => row[n - 1]);
          for (let i = 0; i < n; i++) {
            U[i][n - 1] = B[n - 1 - i][0];
            B[n - 1 - i][0] = D[i][n - 1];
            D[i][n - 1] = F[i][n - 1];
            F[i][n - 1] = tmp[i];
          }
        } else if (face === "F") {
          let tmp = U[n - 1].slice();
          for (let i = 0; i < n; i++) {
            U[n - 1][i] = R[i][0];
            R[i][0] = D[0][n - 1 - i];
            D[0][n - 1 - i] = L[n - 1 - i][n - 1];
            L[n - 1 - i][n - 1] = tmp[i];
          }
        } else if (face === "B") {
          let tmp = U[0].slice();
          for (let i = 0; i < n; i++) {
            U[0][i] = L[n - 1 - i][0];
            L[n - 1 - i][0] = D[n - 1][n - 1 - i];
            D[n - 1][n - 1 - i] = R[i][n - 1];
            R[i][n - 1] = tmp[i];
          }
        }
      }
    }
  
    incrementCell() {
      const front = this.positionMap.F;
      this.faces[front][this.x][this.y]++;
    }
  
    decrementCell() {
      const front = this.positionMap.F;
      this.faces[front][this.x][this.y]--;
    }
  
    outputCell() {
      const front = this.positionMap.F;
      // For playground, let's output as a character
      return String.fromCharCode(this.faces[front][this.x][this.y]);
    }
  
    inputCell(charCode) {
      const front = this.positionMap.F;
      this.faces[front][this.x][this.y] = charCode;
    }
  
    moveLeft() {
      if (this.y > 0) this.y--;
    }
  
    moveRight() {
      if (this.y < this.n - 1) this.y++;
    }
  
    moveUp() {
      if (this.x > 0) this.x--;
    }
  
    moveDown() {
      if (this.x < this.n - 1) this.x++;
    }
  
    dumpFrontFace() {
      const front = this.faces[this.positionMap.F];
      return front.map((row) => row.join(" ")).join("\n");
    }
  
    dumpCubeState() {
      const { F, R, B, L, U, D } = this.faces;
      const rowStr = (row) => row.join(" ");
      const pad = (rows, letter) =>
        rows.map((row) => `            [${letter}] ${rowStr(row)}`);
  
      return [
        ...pad(U, "U"),
        "",
        `[L] ${rowStr(L[0])}   [F] ${rowStr(F[0])}   [R] ${rowStr(R[0])}   [B] ${rowStr(B[0])}`,
        `[L] ${rowStr(L[1])}   [F] ${rowStr(F[1])}   [R] ${rowStr(R[1])}   [B] ${rowStr(B[1])}`,
        `[L] ${rowStr(L[2])}   [F] ${rowStr(F[2])}   [R] ${rowStr(R[2])}   [B] ${rowStr(B[2])}`,
        "",
        ...pad(D, "D"),
      ].join("\n");
    }
  }
  
  // Tokenizer — same logic as Python version
  function tokenize(codeStr) {
    const loops = [];
    const tokens = [];
    let i = 0;
    while (i < codeStr.length) {
      if (codeStr[i] === " " || codeStr[i] === ")" || codeStr[i] === "\n") {
        i++;
        continue;
      } else if (codeStr[i] === "[") {
        i++;
        let loopNumber = "";
        while (i < codeStr.length && codeStr[i] !== "]") {
          loopNumber += codeStr[i];
          i++;
        }
        i++; // skip ']'
        loops.push({ type: "loop", count: parseInt(loopNumber, 10) });
        continue;
      } else if (codeStr[i] === "(") {
        i++;
        let loopCode = "";
        while (i < codeStr.length && codeStr[i] !== ")") {
          loopCode += codeStr[i];
          i++;
        }
        i++; // skip ')'
        loops[loops.length - 1].body = tokenize(loopCode);
        tokens.push(loops[loops.length - 1]);
        continue;
      } else if (i + 1 < codeStr.length && codeStr[i + 1] === "'") {
        tokens.push(codeStr[i] + "'");
        i += 2;
      } else {
        tokens.push(codeStr[i]);
        i++;
      }
    }
    return tokens;
  }
  
  // Main interpreter
  function parseAndRun(code, cubix, inputFn, outputFn) {
    const tokens = tokenize(code);
    let pc = 0;
  
    while (pc < tokens.length) {
      const cmd = tokens[pc];
  
      if (cmd === "X'" || cmd === "Y'" || cmd === "Z'") {
        cubix.rotateCubeFaces(cmd[0], false);
      } else if (cmd === "X" || cmd === "Y" || cmd === "Z") {
        cubix.rotateCubeFaces(cmd, true);
      } else if (["F'", "B'", "U'", "D'", "L'", "R'"].includes(cmd)) {
        cubix.rotateFace(cmd[0], false);
      } else if (["F", "B", "U", "D", "L", "R"].includes(cmd)) {
        cubix.rotateFace(cmd, true);
      } else if (cmd === "+") {
        cubix.incrementCell();
      } else if (cmd === "-") {
        cubix.decrementCell();
      } else if (cmd === ".") {
        const val = cubix.outputCell();
        outputFn(String.fromCharCode(val));
      } else if (cmd === ",") {
        const inputChar = inputFn();
        cubix.inputCell(inputChar.charCodeAt(0));
      } else if (cmd === "p") {
        cubix.dumpFrontFace();
      } else if (cmd === "d") {
        cubix.dumpCubeState();
      } else if (cmd === "<") {
        cubix.moveLeft();
      } else if (cmd === ">") {
        cubix.moveRight();
      } else if (cmd === "^") {
        cubix.moveUp();
      } else if (cmd === "v") {
        cubix.moveDown();
      } else if (typeof cmd === "object" && cmd.type === "loop") {
        for (let i = 0; i < cmd.count; i++) {
          parseAndRun(cmd.body, cubix, inputFn, outputFn);
        }
      } else {
        throw new Error(`Unknown command: ${cmd}`);
      }
  
      pc++;
    }
  }