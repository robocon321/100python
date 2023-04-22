try:
    file = open("a_file.txt")
    dictionary = {
        "key": "value"
    }
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("File not found error")
except KeyError as keyError:
    print(f"The key {keyError} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    raise TypeError("File was closed.")