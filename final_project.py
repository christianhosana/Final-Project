# Input library
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email import encoders

# "Interface program"
while True: 
    class color:
        BOLD = '\033[1m'
        END = '\033[0m'

    print(color.BOLD + "Selamat datang dalam program pengirim e-mail otomatis" + color.END)
    print("------------------------------------------------------")
    print("---Menu---\n")
    print("1. Daftar email Penerima\n2. Tambah email Penerima\n3. Kirim email\n4. Keluar\n")
    menu = input("Masukan input menu: \n")

# Pilihan menu program
    if menu == '1':
        print("Daftar email penerima")
        print("----------------------\n")
        with open ('receiverlist.txt', 'r') as filex: 
            daftar_penerima = filex.read()
            print(daftar_penerima)

    elif menu == '2':
        email = input(str("Tambah email penerima: "))
        with open ('receiverlist.txt', 'a') as filex: 
            filex.write(email)
            filex.write('\n')
        print()        
        print('Email berhasil ditambahkan')
    
    elif menu == '3':
        print("Silahkan login terlebih dahulu")
        gmail_user = input(str("Masukkan akun email: "))
        gmail_app_password = getpass.getpass()

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = input(str("Subject email : "))
        body = input(str("Isi email: "))

# Menyertakan attachment dalam email
        while True: 
            lampiran = input("Apakah anda ingin menyertakan lampiran? (yes/no) ")
            if lampiran == 'yes':

                filename = input("Masukkan nama file beserta formatnya: ")
                path = "paimon.gif"
                attachment = open(path, "rb") 
                
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(part)

                with open('receiverlist.txt','r') as filex:
                    penerima = filex.readlines()

                for i in range(len(penerima)):
                    receiver = penerima[i]                    
                    msg['To'] = receiver
                    msg.attach(MIMEText(body, 'plain'))
        
                    try:          
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_app_password)
                        text = msg.as_string()
                        server.sendmail(gmail_user, receiver, text)
                        server.quit()
                        print("e-mail terkirim!")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)
    
                break

            elif lampiran == 'no':
                with open ('receiverlist.txt','r') as filex:
                    penerima = filex.readlines()

                for i in range(len(penerima)):
                    receiver = f"{penerima[i]}"
                    msg['To'] = receiver
                    msg.attach(MIMEText(body, 'plain'))
            
                    try:          
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.ehlo()
                        server.login(gmail_user, gmail_app_password)
                        text = msg.as_string()
                        server.sendmail(gmail_user, receiver, text)
                        server.quit()
                        print("e-mail terkirim!")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)

                break

            else :
                print("Pilihan tidak tersedia")
            

    elif menu == '4': 
        print("---------------------------------")
        print("Terima kasih")
        print("---------------------------------")
        break

    else : 
        print("Mohon maaf, menu yang dituju tidak tersedia.")