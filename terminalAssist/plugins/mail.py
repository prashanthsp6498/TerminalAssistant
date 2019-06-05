import getpass
import smtplib
import ssl
import colorama


def send_mail():
    port = 465
    try:
        email = input("Email: ")
        password = getpass.getpass()
        reciever_mailid = input("Reciever mail: ")
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(email, password)
                subject = input("Subject: ")
                message = input("Message: ")
                message = """\
                        Subject: """+subject+"""\n"""+message
                print("Message sending to", reciever_mailid)
                server.sendmail(email, reciever_mailid, message)
        except Exception as e:
            print(colorama.Fore.RED, "Hey type correct password\n Or \n"+e,
                  colorama.Fore.WHITE)
    except Exception:
        print("\nSomething went wrong ")
