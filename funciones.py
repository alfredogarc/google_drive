import os 
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def obtener_nombre_con_extension(ruta, nDevolver):
    if nDevolver == 1:
        return os.path.basename(ruta)
    else:
        if nDevolver == 2:
            return os.path.splitext(os.path.basename(ruta))[0]
        else:
            return os.path.splitext(ruta)[1]

#sIdCarpeta = '1YCSL_QwR1vIi5ec9Y90lUaaXpLfK4VuT'

def procesar(sArchivoAEnviar, sIdCarpeta, sEmails):
    # Autenticación con Google Drive
    sArchivoCredencial = "mycreds_" + sIdCarpeta + ".txt"
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(sArchivoCredencial)  # Carga las credenciales desde un archivo
    if gauth.credentials is None:
        # Realiza la autenticación si no se encuentran credenciales válidas
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresca el token de acceso si ha expirado
        gauth.Refresh()
    else:
        # Inicializa las credenciales
        gauth.Authorize()
    gauth.SaveCredentialsFile(sArchivoCredencial)  # Guarda las credenciales en un archivo para 
    gauth.LocalWebserverAuth()

    # Inicializa el objeto GoogleDrive con la autenticación
    drive = GoogleDrive(gauth)

    # Ruta local del archivo que deseas subir
    file_path = sArchivoAEnviar
    sNombreCompleto = obtener_nombre_con_extension(file_path, 1)
    sNombre = obtener_nombre_con_extension(file_path, 2)
    sExt = obtener_nombre_con_extension(file_path, 3)                                   

    # Busca si el archivo ya existe en la carpeta específica
    file_list = drive.ListFile({'q': "'" + sIdCarpeta + "' in parents and trashed=false"}).GetList()
    for file in file_list:
        if file['title'] == sNombre:
            # Elimina el archivo existente antes de subir el nuevo
            file.Delete()

    # Crea un objeto de archivo en Google Drive
    file = drive.CreateFile({'title': sNombreCompleto, 'parents': [{'id': sIdCarpeta}]})
    file.SetContentFile(file_path)  # Establece el contenido del archivo
    file.Upload(param={'convert': True})  # Sube el archivo a Google Drive

    emails = sEmails
    emails = emails.replace(';', ',')  # Reemplaza los puntos y coma por comas
    emails = emails.replace(' ', '')    # Elimina los espacios en blanco
    email_list = emails.split(',')      # Divide la cadena en una lista usando la coma como
    
    #email_list = ['cesarmtroncoso@gmail.com', 'yerikasilva@gmail.com']
    for email in email_list:
        file.InsertPermission({
            'type': 'user',
            'value': email,
            'role': 'writer'
        })
