# trocar as funções, usar o metodo find para pegar a posição exata
# do que eu estou procurando
# Caso a variavel seja definida em mais de uma linha
# vai dar erro


def removeInlineComments(file_str):
    notComment = ""
    for i in range(1, len(file_str)):
        if (file_str[i - 1] + file_str[i] == "//"):
            for j in range(i, len(file_str)):
                if (file_str[j] == "\n"):
                    notComment = file_str[0:i - 1]
                    notComment += file_str[j+1:]
                    file_str = notComment
                    break   
            break
    if ("//" in file_str):
        file_str = removeInlineComments(file_str)
    return file_str


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


def removeEndOfLine(file_str):
    return file_str.replace("\n", " ")


def hasSemicolon(file_line):
    if ("var " in file_line or "let " in file_line or "const " in file_line):
        if (";" in file_line):
            return True
        else:
            return False
    return True


def placeSemicolon(file_str):
    file_arr = file_str.split("\n")
    file_return = str()

    for i in range(len(file_arr)):
        if (not hasSemicolon(file_arr[i])):
            file_arr[i] += ";"
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
    # desnecessaria já que a função de colocar ponto e virgula
    # já tira as quebras de linha
    # output_str = removeEndOfLine(output_str)
    
    output_file = open(input_name + ".min." + input_extension, "w")
    output_file.write(output_str)