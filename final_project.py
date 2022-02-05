# Input library
import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# "Interface program"
while True: 
    class color:
        BOLD = '\033[1m'
        END = '\033[0m'

    print(color.BOLD + "Welcome to the automatic e-mail sender program!" + color.END)
    print(color.BOLD + "------------------------------------------------------" + color.END)
    print(color.BOLD + "---MENU---\n" + color.END)
    print("1. Recipient email list\n2. Add recipient email\n3. Send email\n4. Exit\n")
    menu = input("Pilih menu: \n")

# Pilihan menu program
    if menu == '1':
        print("Recipient email list: ")
        print("----------------------\n")
        with open ('receiverlist.txt', 'r') as filex: 
            daftar_penerima = filex.read()
            print(daftar_penerima)

    elif menu == '2':
        email = input(str("Add recipient email: "))
        with open ('receiverlist.txt', 'a') as filex: 
            filex.write(email)
            filex.write('\n')
        print()        
        print('Email added succesfully!')
    
    elif menu == '3':
        print("Please login first")
        gmail_user = input(str("Insert your email address: "))
        gmail_app_password = getpass.getpass()

        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['Subject'] = input(str("Email subject : "))
        body = input(str("Email content: "))

# Menyertakan attachment dalam email
        while True: 
            lampiran = input("Do you want to include some attachments? (yes/no) ")
            if lampiran == 'yes':

                filename = input("Enter the file name and the format: ")
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
                        print("Email sent!")
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
                        print("Email sent!")
                    except Exception as exception:
                        print("Error: %s!\n\n" % exception)

                break

            else :
                print("The option is not available")
            

    elif menu == '4': 
        print("---------------------------------")
        print("Thank you and have a nice day!")
        print("---------------------------------")
        break

    else : 
        print("The option is not available")
