try:
    import mechanize
    nv = mechanize.Browser()
    nv.open("http://www.pudim.com.br")
except:
    print('\033[;31mO site pudim não esta acessivel no momento!')
else:
    print('\033[;32mConseguir acessar o site pudim com sucesso!')