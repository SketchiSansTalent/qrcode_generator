import qrcode

def generer_qr_code(texte, nom_fichier):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texte)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(nom_fichier)
    print(f"QR Code enregistré sous {nom_fichier}")

texte = input("Entrez le texte ou le lien à encoder : ")
nom_fichier = input("Entrez le nom du fichier de sortie (ex: qr_code.png) : ")
generer_qr_code(texte, nom_fichier)