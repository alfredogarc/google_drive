import sys
from funciones import obtener_nombre_con_extension, procesar

def main(sArchivoAEnviar, sIdCarpeta, sEmails):
    if sArchivoAEnviar == '':
        return(400)
    elif sIdCarpeta == '':
        return(400)
    elif sEmails == "":
        return(400)
    else:
        print("Archivo: " + sArchivoAEnviar + ".   idCarpeta: " + sIdCarpeta + ".   Emails: " + sEmails)
        procesar(sArchivoAEnviar, sIdCarpeta, sEmails)
        

if __name__ == '__main__':
    if len(sys.argv) < 1:
        sArchivoAEnviar = ""
        sIdCarpeta = ""
    else:
        sArchivoAEnviar = sys.argv[1]
        sIdCarpeta = sys.argv[2]
        sEmails = sys.argv[3]

main(sArchivoAEnviar, sIdCarpeta, sEmails)

