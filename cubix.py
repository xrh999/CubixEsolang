import sys


class Cubix:
    def __init__(self, size=3):
        self.n = size  # typically 3
        self.mid = self.n//2
        self.faces = {
            'F': [[0] * self.n for _ in range(self.n)],
            'B': [[0] * self.n for _ in range(self.n)],
            'U': [[0] * self.n for _ in range(self.n)],
            'D': [[0] * self.n for _ in range(self.n)],
            'L': [[0] * self.n for _ in range(self.n)],
            'R': [[0] * self.n for _ in range(self.n)],
        }
        self.position_map = {
            'F': 'F',
            'B': 'B',
            'U': 'U',
            'D': 'D',
            'L': 'L',
            'R': 'R',
        }
        self.x, self.y = self.n//2, self.n//2

    def rotate_cube_faces(self, axis, clockwise):
        p = self.position_map
        if axis == 'X':
            if clockwise:
                p['F'], p['D'], p['B'], p['U'] = p['D'], p['B'], p['U'], p['F']
            else:
                p['F'], p['U'], p['B'], p['D'] = p['U'], p['B'], p['D'], p['F']
        elif axis == 'Y':
            if clockwise:
                p['L'], p['B'], p['R'], p['F'] = p['B'], p['R'], p['F'], p['L']
            else:
                p['L'], p['F'], p['R'], p['B'] = p['F'], p['R'], p['B'], p['L']
        elif axis == 'Z':
            if clockwise:
                p['U'], p['R'], p['D'], p['L'] = p['L'], p['U'], p['R'], p['D']
            else:
                p['U'], p['L'], p['D'], p['R'] = p['R'], p['U'], p['L'], p['D']
        else:
            print(f"Unknown axis: {axis}")
            sys.exit(1)

    def rotate_face(self, face, clockwise):
        F, R, B, L, U, D = self.faces["F"], self.faces["R"], self.faces["B"], self.faces["L"], self.faces["U"], self.faces["D"]
        n = self.n

        if clockwise:
            self.faces[face] = [list(row) for row in zip(*self.faces[face][::-1])]
            if face == "U":
                tmp = F[0][:]
                F[0] = L[0][:]
                L[0] = B[0][:]
                B[0] = R[0][:]
                R[0] = tmp
            elif face == "D":
                tmp = F[n-1][:]
                F[n-1] = R[n-1][:]
                R[n-1] = B[n-1][:]
                B[n-1] = L[n-1][:]
                L[n-1] = tmp
            elif face == "L":
                tmp = [U[i][0] for i in range(n)]
                for i in range(n):
                    U[i][0] = B[n-1-i][n-1]
                    B[n-1-i][n-1] = D[i][0]
                    D[i][0] = F[i][0]
                    F[i][0] = tmp[i]
            elif face == "R":
                tmp = [U[i][n-1] for i in range(n)]
                for i in range(n):
                    U[i][n-1] = F[i][n-1]
                    F[i][n-1] = D[i][n-1]
                    D[i][n-1] = B[n-1-i][0]
                    B[n-1-i][0] = tmp[i]
            elif face == "F":
                tmp = U[n-1][:]
                for i in range(n):
                    U[n-1][i] = L[n-1-i][n-1]
                    L[n-1-i][n-1] = D[0][n-1-i]
                    D[0][n-1-i] = R[i][0]
                    R[i][0] = tmp[i]
            elif face == "B":
                tmp = U[0][:]
                for i in range(n):
                    U[0][i] = R[i][n-1]
                    R[i][n-1] = D[n-1][n-1-i]
                    D[n-1][n-1-i] = L[n-1-i][0]
                    L[n-1-i][0] = tmp[i]

        else:
            self.faces[face] = [list(row) for row in zip(*self.faces[face])][::-1]
            if face == "U":
                tmp = F[0][:]
                F[0] = R[0][:]
                R[0] = B[0][:]
                B[0] = L[0][:]
                L[0] = tmp
            elif face == "D":
                tmp = F[n-1][:]
                F[n-1] = L[n-1][:]
                L[n-1] = B[n-1][:]
                B[n-1] = R[n-1][:]
                R[n-1] = tmp
            elif face == "L":
                tmp = [U[i][0] for i in range(n)]
                for i in range(n):
                    U[i][0] = F[i][0]
                    F[i][0] = D[i][0]
                    D[i][0] = B[n-1-i][n-1]
                    B[n-1-i][n-1] = tmp[i]
            elif face == "R":
                tmp = [U[i][n-1] for i in range(n)]
                for i in range(n):
                    U[i][n-1] = B[n-1-i][0]
                    B[n-1-i][0] = D[i][n-1]
                    D[i][n-1] = F[i][n-1]
                    F[i][n-1] = tmp[i]
            elif face == "F":
                tmp = U[n-1][:]
                for i in range(n):
                    U[n-1][i] = R[i][0]
                    R[i][0] = D[0][n-1-i]
                    D[0][n-1-i] = L[n-1-i][n-1]
                    L[n-1-i][n-1] = tmp[i]
            elif face == "B":
                tmp = U[0][:]
                for i in range(n):
                    U[0][i] = L[n-1-i][0]
                    L[n-1-i][0] = D[n-1][n-1-i]
                    D[n-1][n-1-i] = R[i][n-1]
                    R[i][n-1] = tmp[i]

    def increment_cell(self):
        front = self.position_map['F']
        self.faces[front][self.x][self.y] += 1

    def decrement_cell(self):
        front = self.position_map['F']
        self.faces[front][self.x][self.y] -= 1

    def output_cell(self):
        front = self.position_map['F']
        print(self.faces[front][self.x][self.y])

    def input_cell(self):
        front = self.position_map['F']
        self.faces[front][self.x][self.y] = int(input())

    def dump_front_face(self):
        front = self.faces(self.position_map['F'])
        print(self.faces[front])

    def dump_cube_state(self):
        F, R, B, L, U, D = self.faces["F"], self.faces["R"], self.faces["B"], self.faces["L"], self.faces["U"], self.faces["D"]
        def row_str(row): return " ".join(str(x) for x in row)

        def padded(rows, letter):
            return ["            [" + letter + "] " + row_str(row) for row in rows]

        print("\n".join([
            *padded(U, "U"),
            "",
            "[L] " + row_str(L[0]) + "   [F] " + row_str(F[0]) + "   [R] " + row_str(R[0]) + "   [B] " + row_str(B[0]),
            "[L] " + row_str(L[1]) + "   [F] " + row_str(F[1]) + "   [R] " + row_str(R[1]) + "   [B] " + row_str(B[1]),
            "[L] " + row_str(L[2]) + "   [F] " + row_str(F[2]) + "   [R] " + row_str(R[2]) + "   [B] " + row_str(B[2]),
            "",
            *padded(D, "D")
        ]))

    def move_left(self):
        if self.x >= 0:
            self.x -= 1

    def move_right(self):
        if self.x < self.n:
            self.x += 1

    def move_up(self):
        if self.y >= 0:
            self.y -= 1

    def move_down(self):
        if self.y < self.n:
            self.y += 1


def tokenize(code_str):
    loops = []
    tokens = []
    i = 0
    while i < len(code_str):
        if code_str[i] == " " or code_str[i] == ")" or code_str[i] == "\n":
            i += 1
            continue
        elif code_str[i] == "[":
            i += 1  # skip '['
            loop_number = ""
            while i < len(code_str) and code_str[i] != "]":
                loop_number += code_str[i]
                i += 1
            i += 1  # skip ']'
            loops.append({'type': 'loop', 'count': int(loop_number)})
            continue
        elif code_str[i] == "(":
            i += 1  # skip '('
            loop_code = ""
            while i < len(code_str) and code_str[i] != ")":
                loop_code += code_str[i]
                i += 1
            i += 1  # skip ')'
            loops[-1]['body'] = tokenize(loop_code)
            tokens.append(loops[-1])
            continue
        elif i + 1 < len(code_str) and code_str[i+1] == "'":
            tokens.append(code_str[i] + "'")
            i += 2
        else:
            tokens.append(code_str[i])
            i += 1
    return tokens


def parse_and_run(code, cubix):
    code = tokenize(code)  # valid commands
    pc = 0  # program counter
    code_len = len(code)

    while pc < code_len:
        cmd = code[pc]
        if cmd in ["X'", "Y'", "Z'"]:
            cubix.rotate_cube_faces(cmd[0], clockwise=False)
        elif cmd in ["X", "Y", "Z"]:
            cubix.rotate_cube_faces(cmd, clockwise=True)
        elif cmd in ["F'", "B'", "U'", "D'", "L'", "R'"]:
            cubix.rotate_face(cmd[0], clockwise=False)
        elif cmd in ["F", "B", "U", "D", "L", "R"]:
            cubix.rotate_face(cmd, clockwise=True)
        elif cmd == "+":
            cubix.increment_cell()
        elif cmd == "-":
            cubix.decrement_cell()
        elif cmd == ".":
            cubix.output_cell()
        elif cmd == ",":
            cubix.input_cell()
        elif cmd == "p":
            cubix.dump_front_face()
        elif cmd == "d":
            cubix.dump_cube_state()
        elif cmd == '<':
            cubix.move_left()
        elif cmd == '>':
            cubix.move_right()
        elif cmd == '^':
            cubix.move_up()
        elif cmd == 'v':
            cubix.move_down()
        elif cmd == 'p':
            print(f"Cursor: ({cubix.x}, {cubix.y})")
        elif isinstance(cmd, dict) and cmd.get('type') == 'loop':
            for _ in range(cmd['count']):
                parse_and_run(cmd['body'], cubix)
        else:
            print(f"Unknown command: {cmd}")
            sys.exit(1)
        pc += 1


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 cubix.py program.cbx")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        code = f.read()
    cubix = Cubix(size=3)
    parse_and_run(code, cubix)
    print()  # newline at the end


if __name__ == "__main__":
    main()
