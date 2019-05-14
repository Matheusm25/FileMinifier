def removeInlineComments(file_str):
    file_arr = file_str.split("\n")
    file_return = str()

    for i in range(len(file_arr)):
        try:
            if ("//" in file_arr[i]):
                position = file_arr[i].find("//")
                if (position != 0):
                    file_arr[i] = file_arr[i][0:position]
                else:
                    file_arr[i] = ""
        except IndexError:
            break
    for i in file_arr:
        if (i != ""):
            file_return += i + "\n"
    return file_return 


def removeBlockComments(file_str):
    notComment = ""
    for i in range(1, len(file_str)):
        if (file_str[i - 1] + file_str[i] == "/*"):
            for j in range(i, len(file_str)):
                if (file_str[j - 1] + file_str[j] == "*/"):
                    notComment = file_str[0:i - 1]
                    notComment += file_str[j+1:]
                    file_str = notComment
                    break
            break
    if ("/*" in file_str):
        file_str = removeBlockComments(file_str)
    return file_str


def hasSemicolon(file_line):
    if ("var " in file_line or "let " in file_line or "const " in file_line):
        if (";" in file_line):
            return True
        else:
            return False
    return True


def isObject(file_line):
    if ("var " in file_line or "let " in file_line or "const " in file_line):
        if ("{" in file_line):
            return True
    return False


def placeSemicolonObject(file_line, semicolon_count):
    semicolon_count += file_line.count("{")
    semicolon_count -= file_line.count("}")
    if (semicolon_count == 0):
        file_line += ";"
    return [file_line, semicolon_count]


def placeSemicolon(file_str):
    semicolon_count = 0
    file_arr = file_str.split("\n")
    file_return = str()

    for i in range(len(file_arr)):
        if (not hasSemicolon(file_arr[i]) and not isObject(file_arr[i])):
            file_arr[i] += ";"
        elif (isObject(file_arr[i]) or semicolon_count != 0):
            aux_arr = placeSemicolonObject(file_arr[i], semicolon_count) 
            file_arr[i] = aux_arr[0]
            semicolon_count = aux_arr[1] 
    for i in file_arr:
        file_return += i + " "
    return file_return

def compress(file):
    #Open the file
    try:
        input_file = open(file, 'r')
    except:
        print("The file can't be found or can't be open")
        exit(0)
    input_name = str(file).split(".")[0]
    input_extension = str(file).split(".")[1]
    
    #Stores in a String
    input_str = input_file.read()

    output_str = removeInlineComments(input_str)
    output_str = removeBlockComments(output_str)
    output_str = placeSemicolon(output_str)
    
    output_file = open(input_name + ".min." + input_extension, "w")
    output_file.write(output_str)