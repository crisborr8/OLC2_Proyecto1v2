colorscheme = "/spectral11/"
txt_hoja = txt_nodo = ""
i = 0

def initGraph():
    global txt_hoja, txt_nodo, i
    txt_hoja = txt_nodo = ""
    i = 0

def setHoja(hoja):
    global txt_hoja, i, colorscheme
    i += 1
    id_hoja = 'ND_' + str(i)
    hoja = "<<table CELLSPACING=\"0\" BORDER=\"0\"><tr><td  BORDER=\"1\" bgcolor=\""+colorscheme+"3\">" + str(hoja) + "</td></tr></table>>"
    txt_hoja += id_hoja + " [label=" + hoja + "];\n"
    return id_hoja

def setNodo(nodo, hijos):
    global txt_nodo, txt_hoja, i, colorscheme
    i += 1
    k = 0
    id_nodo = 'ND_' + str(i)
    nodo = "<<table  CELLSPACING=\"0\" BORDER=\"0\"><tr><td BORDER=\"1\" colspan=\"" + str(len(hijos)) + "\"  bgcolor=\""+colorscheme+"4\">" + str(nodo) + "</td></tr><tr>"
    for id_hijo in hijos:
        f = "f" + str(k)
        txt_nodo += id_nodo + ":" + f + "->" + id_hijo + ";\n"
        nodo += "<td BORDER=\"1\" port=\"" + f + "\"  bgcolor=\"" + colorscheme + str(k + 5) + "\"></td>"
        k += 1
    nodo += "</tr></table>>"
    txt_hoja += id_nodo + " [label=" + nodo + "];\n"
    return id_nodo

def viewGraph():
    file_name = "ply/report/input.dot"
    f = open(file_name, 'w+')
    graph = "digraph {\nnode [shape=plaintext]\n" + txt_hoja + "\n" + txt_nodo + "}"
    f.write(graph)
    f.close()
    print("guardado...")