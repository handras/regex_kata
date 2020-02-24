alphabet = ('a', 'b', 'c', 'd')


class Empty:
    pass


empty = Empty()


class regex:
    states = []
    transitions = []
    final = None

    def compile(self, p):
        prevstate = 0
        for i in range(len(p)):
            try:
                n_char = p[i + 1]
                if n_char == '*':
                    continue
            except IndexError:
                pass
            char = p[i]

            if char == '*':
                multiplied_char = p[i - 1]
                if multiplied_char == '.':
                    for a in alphabet:
                        self.transitions.append((prevstate, a, prevstate + 1))
                        self.transitions.append((prevstate, empty, prevstate + 1))
                        self.transitions.append((prevstate, a, prevstate))
                else:
                    self.transitions.append((prevstate, multiplied_char, prevstate + 1))
                    self.transitions.append((prevstate, empty, prevstate + 1))
                    self.transitions.append((prevstate, multiplied_char, prevstate))
                prevstate = prevstate + 1
                pass
            elif char in alphabet:
                self.transitions.append((prevstate, char, prevstate + 1))
                prevstate = prevstate + 1
                pass
            elif char == '.':
                for a in alphabet:
                    self.transitions.append((prevstate, a, prevstate + 1))
                prevstate = prevstate + 1
                pass
        self.final = prevstate
        pass

    def _match(self, state, string):
        if string == '':
            if state == self.final:
                return True
            else:
                return False

        for t in self.transitions:
            if t[0] == state and t[1] == string[0]:
                m = self._match(t[2], string[1:])
                if m:
                    return True
            if t[0] == state and t[1] is empty:
                m = self._match(t[2], string)
                if m:
                    return True
        return False

    def match(self, s, p):
        self.states = []
        self.transitions = []
        self.final = None
        self.compile(p)
        return self._match(0, s)
