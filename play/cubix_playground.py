class Cubix:
    def __init__(self, size=3):
        self.n = size  # typically 3
        self.mid = self.n // 2
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
        self.x, self.y = self.mid, self.mid
        self.input_provider = None # Added this line for injecting input

    def get_current_cell(self):
        front = self.position_map['F']
        return self.faces[front][self.x][self.y]

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
            raise ValueError(f"Unknown axis: {axis}")

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

        else: # Counter-clockwise
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

    def increment_cell(self, num=1): # Added default num=1 for convenience
        front = self.position_map['F']
        self.faces[front][self.x][self.y] += num

    def decrement_cell(self, num=1): # Added default num=1 for convenience
        front = self.position_map['F']
        self.faces[front][self.x][self.y] -= num

    def output_cell(self, output):
        front = self.position_map['F']
        output.append(str(self.faces[front][self.x][self.y]))

    def input_cell(self):
        front = self.position_map['F']
        val = None
        if self.input_provider: # Use the injected input_provider
            val = self.input_provider()
        else:
            val = input()  # Fallback to Python's input if not provided

        try:
            self.faces[front][self.x][self.y] = int(val)
        except Exception:
            self.faces[front][self.x][self.y] = 0

    def dump_front_face(self, output):
        front = self.position_map['F']
        output.append(str(self.faces[front]))

    def dump_cube_state(self, output):
        F, R, B, L, U, D = (self.faces[self.position_map['F']],
                            self.faces[self.position_map['R']],
                            self.faces[self.position_map['B']],
                            self.faces[self.position_map['L']],
                            self.faces[self.position_map['U']],
                            self.faces[self.position_map['D']])

        def row_str(row):
            return " ".join(str(x) for x in row)

        def padded(rows, letter):
            return ["            [" + letter + "] " + row_str(row) for row in rows]

        # This formatting assumes n=3, adjust for other sizes if needed
        output.append("\n".join([
            *padded(U, "U"),
            "",
            "[L] " + row_str(L[0]) + "   [F] " + row_str(F[0]) + "   [R] " + row_str(R[0]) + "   [B] " + row_str(B[0]),
            "[L] " + row_str(L[1]) + "   [F] " + row_str(F[1]) + "   [R] " + row_str(R[1]) + "   [B] " + row_str(B[1]),
            "[L] " + row_str(L[2]) + "   [F] " + row_str(F[2]) + "   [R] " + row_str(R[2]) + "   [B] " + row_str(B[2]),
            "",
            *padded(D, "D")
        ]))

    def move_left(self):
        if self.x > 0:
            self.x -= 1

    def move_right(self):
        if self.x < self.n - 1:
            self.x += 1

    def move_up(self):
        if self.y > 0:
            self.y -= 1

    def move_down(self):
        if self.y < self.n - 1:
            self.y += 1


def tokenize(code_str):
    tokens = []
    i = 0
    last_function_def_index = None
    pending_loop_token = None

    while i < len(code_str):
        c = code_str[i]
        if c in (" ", "\n"):
            i += 1
            continue
        
        elif c == '"':
            i += 1
            func_name = ""
            while i < len(code_str) and code_str[i] != '"':
                func_name += code_str[i]
                i += 1
            if i >= len(code_str) or code_str[i] != '"':
                raise RuntimeError("Unclosed function name.")
            i += 1
            tokens.append({'type': 'function_def', 'name': func_name})
            last_function_def_index = len(tokens) - 1

        elif c == '{':
            i += 1
            body = ""
            brace_depth = 1
            while i < len(code_str):
                if code_str[i] == '{':
                    brace_depth += 1
                elif code_str[i] == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        break
                body += code_str[i]
                i += 1
            if brace_depth != 0:
                raise RuntimeError("Unclosed function body '{'")
            i += 1  # skip final }

            if last_function_def_index is None:
                raise RuntimeError("Function body found without function name.")
            tokens[last_function_def_index]['body'] = tokenize(body)
            last_function_def_index = None

        elif c == '[':
            i += 1
            count = ""
            while i < len(code_str) and code_str[i] != ']':
                count += code_str[i]
                i += 1
            if i >= len(code_str) or code_str[i] != ']':
                raise RuntimeError("Unclosed loop count '['")
            i += 1
            try:
                count_int = int(count)
            except ValueError:
                raise RuntimeError(f"Invalid loop count '{count}'")
            pending_loop_token = {'type': 'loop', 'count': count_int}

        elif c == '(':
            if pending_loop_token is None:
                raise RuntimeError("Loop body defined without preceding loop count.")
            i += 1
            loop_body = ""
            paren_depth = 1
            while i < len(code_str):
                if code_str[i] == '(':
                    paren_depth += 1
                elif code_str[i] == ')':
                    paren_depth -= 1
                    if paren_depth == 0:
                        break
                loop_body += code_str[i]
                i += 1
            if paren_depth != 0:
                raise RuntimeError("Unclosed loop body '('")
            i += 1
            pending_loop_token['body'] = tokenize(loop_body)
            tokens.append(pending_loop_token)
            pending_loop_token = None

        elif c == '$':
            i += 1
            call_name = ""
            while i < len(code_str) and code_str[i] != '$':
                call_name += code_str[i]
                i += 1
            if i >= len(code_str) or code_str[i] != '$':
                raise RuntimeError("Unclosed function call.")
            i += 1
            tokens.append({'type': 'function_call', 'name': call_name})

        elif i + 1 < len(code_str) and code_str[i + 1] == "'":
            tokens.append(code_str[i] + "'")
            i += 2

        else:
            tokens.append(c)
            i += 1

    return tokens


def parse_and_run(tokens, cubix, output, input_func, functions_scope): # MODIFIED: Added 'functions_scope' parameter
    cubix.input_provider = input_func # Pass the input_func to the Cubix instance
    # REMOVED: functions = {}  <- This line caused the scope issue
    pc = 0
    code_len = len(tokens) # Changed 'code' to 'tokens' as input is now tokenized list

    while pc < code_len:
        cmd = tokens[pc] # Changed 'code' to 'tokens'

        if isinstance(cmd, dict) and cmd.get('type') == 'function_def':
            if 'body' not in cmd or not cmd['body']:
                raise RuntimeError(f"Function '{cmd['name']}' definition missing body.")
            functions_scope[cmd['name']] = cmd['body'] # MODIFIED: Use functions_scope
        elif isinstance(cmd, dict) and cmd.get('type') == 'function_call':
            function_name = cmd['name']
            if function_name not in functions_scope: # MODIFIED: Use functions_scope
                raise RuntimeError(f"Function '{function_name}' not defined.")
            # Recursive call, passing the same functions_scope
            parse_and_run(functions_scope[function_name], cubix, output, input_func, functions_scope) # MODIFIED: Pass functions_scope
        elif cmd in ["X'", "Y'", "Z'"]:
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
            cubix.output_cell(output)
        elif cmd == ",":
            cubix.input_cell()
        elif cmd == "d":
            cubix.dump_cube_state(output)
        elif cmd == '<':
            cubix.move_left()
        elif cmd == '>':
            cubix.move_right()
        elif cmd == '^':
            cubix.move_up()
        elif cmd == 'v':
            cubix.move_down()
        elif cmd == 'p':
            output.append(f"Cursor: ({cubix.x}, {cubix.y})")
        elif cmd == 'i':
            cubix.dump_front_face(output)
        elif isinstance(cmd, dict) and cmd.get('type') == 'loop':
            if 'count' not in cmd or 'body' not in cmd:
                raise RuntimeError(f"Malformed loop command: {cmd}")
            for _ in range(cmd['count']):
                # Recursive call for loop body, passing the same functions_scope
                parse_and_run(cmd['body'], cubix, output, input_func, functions_scope) # MODIFIED: Pass functions_scope
        else:
            raise RuntimeError(f"Unknown command: {cmd}")

        pc += 1


def run_code(code_str, inputs=None):
    if inputs is None:
        inputs = []
    cubix = Cubix(size=3)
    output = []
    input_index = 0

    # Define the input function to be passed to Cubix
    def input_func():
        nonlocal input_index
        if input_index < len(inputs):
            val = inputs[input_index]
            input_index += 1
            return val
        else:
            return "0"  # default if no more inputs

    # MODIFIED: Initialize the global functions dictionary here
    global_functions_dict = {}

    # MODIFIED: Tokenize the code_str once
    tokens = tokenize(code_str)

    # MODIFIED: Call parse_and_run with the tokenized code and the global_functions_dict
    parse_and_run(tokens, cubix, output, input_func, global_functions_dict)
    return "\n".join(output)
