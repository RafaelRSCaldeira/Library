import re

txt = "Devolução de livro - ISBN: // Título: "

x = re.search("^.*ISBN:.*", txt)
print(x)