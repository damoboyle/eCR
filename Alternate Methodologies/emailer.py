import win32com.client as win32

def send(address, subject, message, file)
    #Open Outlook and compose an email
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)

    mail.To = address
    mail.Subject = subject

    #Pulls up default signature of sender from Outlook
    mail.GetInspector
    
    #HTML text to inform receiver that this email is automated
    intro = "<i style='color:gray'>This is an automated message.</i><br><br>"

    #Used to merge intro and user message into HTML body properly while including default signature
    index = mail.HTMLbody.find('>', mail.HTMLbody.find('<body'))
    mail.HTMLbody = mail.HTMLbody[:index + 1] + intro + message + mail.HTMLbody[index + 1:]
    
    #Attaches eCR PDF
    mail.Attachments.Add("I:/eCR/00 Converted to PDF/" + file)
    mail.Display(True)  #Displays for Testing
    #mail.Send()

#Code modifidied from:
#https://medium.com/mlearning-ai/use-python-to-send-outlook-emails-d673ce9e33e4
#How to include default signature from Outlook
#https://stackoverflow.com/questions/32209091/add-signature-to-outlook-email-with-python-using-win32com