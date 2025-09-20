nombre_archivo = input("Ingrese el nombre del archivo: ")

extension = nombre_archivo.lower().split(".")[-1]

tipos_mime = {
    "gif": "image/gif",
    "jpg": "image/jpeg", 
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

if extension in tipos_mime:
    print(tipos_mime[extension])
else:
    print("application/octet-stream")