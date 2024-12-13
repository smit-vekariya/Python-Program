class ScriptWriter:
    def __init__(self, file_name, cast):
        self.file_name = file_name
        self.cast = cast

    def write_script(self, text):
        with open(self.file_name, "a") as file:
            file.write(text+"\n")
    

if __name__ == "__main__":
    cast = {1:"person 1", 2:"person 2", 3:"[]", 4:"exit"}
    sw = ScriptWriter("Peacock.txt", cast)

    for key, value in cast.items():
        print(str(key) + ":" + value)

    while True:
        select_char = int(input("Select Option:"))
        if select_char == 4:
            break

        line = input("Enter line:")

        if select_char in [1, 2]:
            text = f"{cast[select_char]}: {line}"
            sw.write_script(text)
        elif select_char == 3:
            text = f"[ {line} ]"
            sw.write_script(text)