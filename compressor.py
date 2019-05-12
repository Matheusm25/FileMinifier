# checar as declarações de varivaies
# tenho que terminar ela com ponto e virgula
# checar se está sendo declarada mais de uma variavel na mesam linha
# como vai estar tudo na mesma linha eu posso checar a palavra var
# e depois checar o valor depois do '=' e após ele colocar ;
# checar while(espaço) e checar se já tem ponto e virgula
# checar se a palavra var está realmente iniciando uma variavel
# e não faz parte de uma palavra normal 

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
    return file_str.replace("\n", " ");

def placeSemicolon(file_str):
    file_str_sc = ""
    for i in range(2, len(file_str)):
        aux = file_str[i - 2] + file_str[i - 1] + file_str[i]
        if (aux == "var" or aux == "let"):
            


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
    output_str = removeEndOfLine(output_str)

    output_file = open(input_name + ".min." + input_extension, "w")
    output_file.write(output_str)