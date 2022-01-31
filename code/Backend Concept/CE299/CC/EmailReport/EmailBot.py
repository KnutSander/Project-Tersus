import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




#Full email of recipient and the reportfilename (WITH file extension!)
#e.g. Report.pdf 
#SendEmail(STRING,STRING)
def SendEmail(EndAddress,ReportFile):
    
    smtp_server="taylor.mxrouting.net" #SMTP server address
    port = 465 #Port of the SMTP server
    you = EndAddress #Email of Recipient
    me = "info@projecttersus.tech" #EMail of sender
    password = "Q4X4Td8J" #Password to account (change this from plaintext?)
    reportfile = ReportFile #name of report pdf to be sent NEED TO HAVE FUNCTION FROM PDF GEN HERE
    
    body = """Dear """+EndAddress+"""
    Your weekly report is due, here is an attachment of your concluded performance,
    Please take time to read the information and adjust your behavior accordingly.
    
    Many thanks,
    Project Tersus
    """
    message = MIMEMultipart()
    message['From'] = me
    message['To'] = you
    message['Subject'] = "Handwashing Weekly Report"
    message.attach(MIMEText(body,'plain'))
    
    
    filename = "ArifReport.PDF"
    attachment = open(filename,"rb")
    
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=%s"%filename)    
    
    
    message.attach(part)
    
    context = ssl.create_default_context() #Create SSL context for connection
    with smtplib.SMTP_SSL(smtp_server,port,context = context) as server:
        server.login(me,password)
        text = message.as_string()
        server.sendmail(me,you,text)
        
        
    #EMail being sent doesnt have working pdf on recipients end
    
