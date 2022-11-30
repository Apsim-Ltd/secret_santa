import random 
import smtplib 
from email.message import EmailMessage
import os 
from dotenv import load_dotenv
load_dotenv()

sender = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")

def santaKid(team_name): 
    """
    generates a list of dictionary containing unique kid to a santa. 
    """
    copy_team = team_name.copy()
    result = []
    for santa in team_name: 
        kid = random.choice(copy_team)
        while santa == kid: 
            kid = random.choice(copy_team)
        result.append({santa: kid})
        copy_team.remove(kid)
    return result 


def emailContent(santa, kid): 
    message = f''''
        <!DOCTYPE html>
        <html>
            <body>
                <div style="background-color:#ff7f50;padding:10px 20px;">
                    <h2 style="font-family:'Mountains of Christmas', cursive;color#ffa07a; text-align:center;"> Echange des cadeaux chez Apsim</h2>
                </div>
                <div style="padding:20px 0px">
                    <div>
                        <img src="https://www.dukeshillham.co.uk/Portals/0/product/images/secret_satnta_2019.jpg" style="width:100%;">
                        <div style="text-align:center;">
                            <h3>{santa}</h3>
                            <p>Ho Ho Ho!! </p> 
                            <p> Histoire de faire perdurer l'esprit de noël dans nos bureaux, tu es invité à participer à l'échange des cadeaux.</p>
                            <p> L'elfe de noël t'a choisi pour être le secret Santa de <b>{kid}</b>! {kid} a été bon enfant et attend son cadeau avec patience.</p>
                            <img src= "https://clipground.com/images/christmas-box-clipart-13.jpg" style="height:300px;">
                        </div>
                    </div>
                </div>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@700&display=swap" rel="stylesheet">
            </body>
        </html>
        '''
    return message 

def automateEmail(recipient,message): 
    msg = EmailMessage()
    msg['Subject'] = 'Mission: Santa Secret 🎅'
    msg['From'] = sender 
    msg['To'] = recipient
    msg.set_content(message, subtype='html')

    try: 
        smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587) 
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)
        smtp.quit()
        print("Email sent successfully!")
    except Exception as e: 
        print(e)

def main(): 
    team_name = ['Adeline', 'Aurelie', 'Caroona', 'Christophe', 'Divya', 'Francesca', 'Joanito', 'Melanie', 'Roan', 'Sarojadevi']
    result = santaKid(team_name)
    for idx in result: 
        for santa, kid in idx.items(): 
            recipient = f"{santa.lower()}@opsearch.com"
            print(recipient)
            message = emailContent(santa, kid)
            automateEmail(recipient, message)

if __name__ == "__main__": 
    main()
