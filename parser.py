with open("dev.txt","r") as fi:
    fo=open("dev.js","w")
    fo.write("var base=[]; base['dev']=[")
    for line in fi:
        line = line[:-1]
        print(line)
        fo.write('"'+line+'",')
    fo.write("];")

