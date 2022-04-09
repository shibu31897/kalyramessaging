import json
import os
import requests
from urllib.parse import urlencode
import pandas as pd
import re
import traceback
# coding="UTF-8"
import sys

sid = '1201159496520171573'
to = number
apiKey = yourApiKey
senderID = senderID  # SITARE

url = f'https://api.in.kaleyra.io/v1/{sid}/messages'
successCount = 0
failedCount = 0


def sendMessage(mobNo, fname, uid):
    template_id_Hindi = "1207164388298382368"
    messageBodyHindi = f"""प्रिय अभ्यर्थी {fname}, होप छात्रवृत्ति परीक्षा 2022 में आपका पंजीकरण सफलतापूर्ण हो गया है l  किसी सूचना के लिए 7406193300 पर कॉल करें l 
-सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/PhoneJson/{uid}.json', 'w') as f:
            json.dump(r.json(), f)

    # status = jsonF["status"]
    # data = jsonF['data']
    # kid = data['id']
    # dataStatus = data['status']
    # print(f"status 1 : {status} || id : {id} || status2 : {dataStatus}")

def inviteMessageIndore(mobNo):
    template_id_Hindi = "1207164700307672595"
    messageBodyHindi = """नमस्कार,सितारे फाउंडेशन संस्था की तरफ से आप सभी शिक्षकों से अनुरोध करना चाहती हु कि आप सभी अपने  स्कूलों के बच्चों को दिनांक 13 मार्च 2022 को 8:00 बजे होने वाली हो होप एवं ग्रोथ (कक्षा 5 से 9) परीक्षा देने के लिए प्रेरित करें ,
     उनका मार्गदर्शन करें और उन्हें परीक्षा देने के लिए प्रोत्साहित करें सभी बच्चों को उनको एक परीक्षा केंद्र पर अपना आधार कार्ड और एडमिट कार्ड लाना को कहें जिन विद्यार्थियों के पास एडमिट कार्ड नहीं है उनका एडमिट कार्ड केंद्र पर बना दिया जाएगा ।इस प्रवेश परीक्षा में सम्मिलित  होने पर आपको 100 रुपये मिलेंगे | -सितारे फाउंडेशन ( होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/IndoreJson/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)

def inviteMessageJaipur(mobNo):
    template_id_Hindi = "1207164779326084902"
    messageBodyHindi = """प्रिय छात्र-छात्राएं, अपने प्रवेश पत्र के अनुसार छात्रवृत्ति परीक्षा और समय का पालन करें| यदि आपके मित्र और साथी जो कक्षा 8,9  मे हैं तथा जिन्होंने सितारे फाउंडेशन की परीक्षा के लिए आवेदन नहीं किया या 
    जिनके पास एडमिट कार्ड नहीं है वह रविवार 27 मार्च को सुबह 8:00 बजे किड्स क्लब सीनियर सेकेंडरी स्कूल, न्यू सांगानेर रोड, धन्वंतरी अस्पताल के सामने, मानसरोवर, जयपुर(https://bit.ly/36bIWmQ) मे परीक्षा के लिए आ सकते हैं | कृपया अपना आधार या कोई भी आई डी अवश्य लाये | सभी परीक्षार्थियों को परीक्षा केंद्र पर 100/- रुपये भत्ता दिया जायेगा | सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट) """
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/JaipurJson/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)

def inviteMessageJaipurHope2(mobNo):
    template_id_Hindi = "1207164779311976379"
    messageBodyHindi = """प्रिय छात्र-छात्राएं, अपने प्रवेश पत्र के अनुसार छात्रवृत्ति परीक्षा और समय का पालन करें। आपके मित्र और साथी जो कक्षा 5,6,7 मे हैं तथा जिन्होंने सितारे फाउंडेशन की परीक्षा के लिए आवेदन नहीं किया या जिनके पास एडमिट कार्ड नहीं है वह रविवार 27 मार्च को सुबह 8:00 बजे अग्रवाल पी.जी.कॉलेज ,सांगानेरी गेट जयपुर(https://bit.ly/3Jl37wZ) मे परीक्षा के लिए आ सकते हैं | 
कृपया अपना आधार या कोई भी आई डी अवश्य लाये | सभी परीक्षार्थियों को परीक्षा केंद्र पर 100/- रुपये भत्ता दिया जायेगा | सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/JaipurJson/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)
def inviteMessageJodhpurHope(mobNo):
    template_id_Hindi = "1207164854483146376"
    messageBodyHindi = """प्रिय छात्र-छात्राएं, अपने प्रवेश पत्र के अनुसार छात्रवृत्ति परीक्षा और समय का पालन करें। आपके मित्र और साथी जो कक्षा 5,6,7 मे हैं तथा जिन्होंने सितारे फाउंडेशन की परीक्षा के लिए आवेदन नहीं किया या जिनके पास एडमिट कार्ड नहीं है वह रविवार 3 अप्रैल 2022 को दोपहर 12:00 PM सेंट्रल अकाडेमी,चोपासनी हाउसिंग बोर्ड(https://bit.ly/3ILYTgD) या सेंट्रल अकाडेमी, ट्रांसफार्मर चौराहा, बीजेडएस कॉलोनी(https://bit.ly/3uFwqEx) जोधपुर- राजस्थान मे परीक्षा के लिए आ सकते हैं | कृपया अपना आधार या कोई भी आई डी अवश्य लाये | सभी परीक्षार्थियों को परीक्षा केंद्र पर 100/- रुपये भत्ता दिया जायेगा | सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/Jodhpur/Hope/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)
def inviteMessageJodhpurGrowth(mobNo):
    template_id_Hindi = "1207164854488176126"
    messageBodyHindi = """प्रिय छात्र-छात्राएं, अपने प्रवेश पत्र के अनुसार छात्रवृत्ति परीक्षा और समय का पालन करें| यदि आपके मित्र और साथी जो कक्षा 8,9  मे हैं तथा जिन्होंने सितारे फाउंडेशन की परीक्षा के लिए आवेदन नहीं किया या जिनके पास एडमिट कार्ड नहीं है वह रविवार 3 अप्रैल 2022 दोपहर को 12:00 PM बजे सेंट्रल अकाडेमी, जोधपुर कैंट रेलवे स्टेशन के सामने नागौर रोड बाइ पास के पास, बनार रोड, जोधपुर- 342027 राजस्थान(https://bit.ly/3uBeCu1) मे परीक्षा के लिए आ सकते हैं | कृपया अपना आधार या कोई भी आई डी अवश्य लाये | सभी परीक्षार्थियों को परीक्षा केंद्र पर 100/- रुपये भत्ता दिया जायेगा | सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/Jodhpur/Growth/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)

def regularGrowtheUpdate(mobNo, exmaDate,exmaTime, uid,examCenter ="IES Public School,रातीबड़ रोड" ,allowance = "150"):
    template_id_Hindi = "1207164580260609231"
    messageBodyHindi = f"""प्रिय छात्र/छात्रा,
सितारे फाउंडेशन की छात्रवृत्ति परीक्षा दिनांक {exmaDate}, को {exmaTime} बजे {examCenter} में हो रही है जिसमें कक्षा 5, 6, व 7 के छात्र/छात्रा भाग ले सकते हैं इस परीक्षा में उत्तीर्ण होने पर सितारे फाउंडेशन आपकी शिक्षा का संपूर्ण खर्च वहन करेगा तथा आपको परीक्षा स्थल पर आने के लिए ₹{allowance} यात्रा भत्ता मिलेगा, यह सूचना आप अधिक से अधिक विद्यार्थियों तक पहुंचाएं. अधिक जानकारी के लिए संपर्क करें +91-7406193300 -सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/RegularUpdate/{uid}.json', 'w') as f:
            json.dump(r.json(), f)

def regularHopeUpdate(mobNo, exmaDate, exmaTime, uid, examCenter="IES Public School,रातीबड़ रोड", allowance="150"):
        template_id_Hindi = "1207164580260609231"
        messageBodyHindi = f"""प्रिय छात्र/छात्रा,
    सितारे फाउंडेशन की छात्रवृत्ति परीक्षा दिनांक {exmaDate}, को {exmaTime} बजे {examCenter} में हो रही है जिसमें कक्षा 5, 6, व 7 के छात्र/छात्रा भाग ले सकते हैं इस परीक्षा में उत्तीर्ण होने पर सितारे फाउंडेशन आपकी शिक्षा का संपूर्ण खर्च वहन करेगा तथा आपको परीक्षा स्थल पर आने के लिए ₹{allowance} यात्रा भत्ता मिलेगा, यह सूचना आप अधिक से अधिक विद्यार्थियों तक पहुंचाएं. अधिक जानकारी के लिए संपर्क करें +91-7406193300 -सितारे फाउंडेशन (होप एंड ड्रीम्स ट्रस्ट)"""
        url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
        param = {
            'method': 'sms',
            'message': messageBodyHindi,
            'template_id': str(template_id_Hindi),
            'to': mobNo,
            'sender': 'SITARE',
            'unicode': '1'
        }
        urlparam = urlencode(param)
        urlF = url3 + "&" + urlparam
        # print(urlF)
        r = requests.post(urlF)
        print(r.status_code)
        if r.status_code == 200:
            print(f"Successfully send to {mobNo}")
            with open(f'/Users/harshit/PycharmProjects/kalyramessaging/RegularUpdate/{uid}.json', 'w') as f:
                json.dump(r.json(), f)



def sendCenterMessage(mobNo, seid, examDate, shift, examTime, uid,examCenter,allowance="100"):
    template_id_Hindi = "1207164779250970739"
    messageBodyHindi = f"""प्रिय विद्यार्थी ,
आपका सितारे पंजीकरण नंबर {seid} है और आपकी परीक्षा {examDate} को {examCenter} में शिफ्ट {shift} में होगी। आपको केंद्र पर {examTime} पहुंचना होगा। इस प्रवेश परीक्षा में सम्मिलित  होने पर आपको 100 रुपये मिलेंगे | -सितारे फाउंडेशन ( होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/Jodhpur/UpdateCenterJson/{uid}.json', 'w') as f:
            json.dump(r.json(), f)


    # status = jsonF["status"]
    # data = jsonF['data']
    # kid = data['id']
    # dataStatus = data['status']
    # print(f"status 1 : {status} || id : {id} || status2 : {dataStatus}")

def sendAdmitCardInvite(mobNo):
    template_id_Hindi = "1207164779270644304"
    messageBodyHindi = f"""प्रिय छात्र-छात्रा,
अगर आप सरकारी स्कूल में अध्ययनरत है तो आप सितारे फाउंडेशन स्कॉलरशिप एग्जाम का अपना प्रवेश पत्र अपने सरकारी स्कूल से शनिवार, 2 अप्रैल 2022 तक प्राप्त कर लीजिए परीक्षा रविवार 3 अप्रैल 2022 को होगी, परीक्षा की पूरी जानकारी प्रवेश पत्र पर उपलब्ध है. अधिक जानकारी के लिए 7406193300 पर संपर्क करे | -सितारे फाउंडेशन ( होप एंड ड्रीम्स ट्रस्ट)"""
    url3 = f"https://api-alerts.kaleyra.com/v4/?api_key={apiKey}"
    param = {
        'method': 'sms',
        'message': messageBodyHindi,
        'template_id': str(template_id_Hindi),
        'to': mobNo,
        'sender': 'SITARE',
        'unicode': '1'
    }
    urlparam = urlencode(param)
    urlF = url3 + "&" + urlparam
    # print(urlF)
    r = requests.post(urlF)
    print(r.status_code)
    if r.status_code == 200:
        print(f"Successfully send to {mobNo}")
        with open(f'/Users/harshit/PycharmProjects/kalyramessaging/AdmitCardInvite/{mobNo}.json', 'w') as f:
            json.dump(r.json(), f)


def messagePrompt():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for fname, phoneNum, uid in zip(myPhoneCSV['Name'], myPhoneCSV['Mobile1'], myPhoneCSV['ID Number']):
            if find(str(uid)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                print(f"{str(fname).split()[0]} and phone number : {str(phoneNum)} ")
                sendMessage(str(phoneNum).replace(" ", ""), str(fname).split()[0], uid)
    except Exception as e:
        print(f"Something wrong with {uid} phone number : {phoneNum}  : {traceback.print_exc()} ")

def messagePromptForJodhpur():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for phoneNum in myPhoneCSV['Mobile1']:
            if find(str(phoneNum)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                inviteMessageJodhpurGrowth(str(phoneNum))
                #sendAdmitCardInvite(phoneNum)
    except Exception as e:
        print(f"Something wrong with {phoneNum} phone number : {phoneNum}  : {traceback.print_exc()} ")
def messageAdmitPrompt():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for  phoneNum, uid in zip(myPhoneCSV['Mobile1'], myPhoneCSV['ID Number']):
            if find(str(uid)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                sendAdmitCardInvite(phoneNum,uid)
    except Exception as e:
        print(f"Something wrong with {uid} phone number : {phoneNum}  : {traceback.print_exc()} ")


def messagePromptCenterUpdate():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for uid, phoneNum, seid, examDate, shift,examCenter, examTime in zip(myPhoneCSV['UID'], myPhoneCSV['Mobile1'],
                                                                  myPhoneCSV['SEID'], myPhoneCSV['Exam Date'],
                                                                  myPhoneCSV['Shift'],myPhoneCSV["Center"] ,myPhoneCSV['ExamTime']):
            if find(str(uid)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                sendCenterMessage(phoneNum, seid, examDate, shift, examTime, uid,examCenter,"100")
                print(f"send successfully  to phone number :with {seid} - {str(phoneNum)} ")
    except Exception as e:
        print(f"Something wrong with {uid} phone number : {phoneNum} : {traceback.print_exc()} ")

def regularUpdateHopePrompt():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for uid, phoneNum, seid, examDate, examTime in zip(myPhoneCSV['UID'], myPhoneCSV['Mobile1'],
                                                                  myPhoneCSV['SEID'], myPhoneCSV['Exam Date'] , myPhoneCSV['ExamTime']):
            if find(str(uid)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                regularHopeUpdate(phoneNum,examDate,examTime,uid)
                print(f"send successfully  to phone number :with {seid} - {str(phoneNum)} ")
    except Exception as e:
        print(f"Something wrong with {uid} phone number : {phoneNum} : {traceback.print_exc()} ")

# messagePrompt()
# sendMessage("9555903247","Harshit","123456789101")
def regularUpdateGrowthPrompt():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for uid, phoneNum, seid, examDate, examTime in zip(myPhoneCSV['UID'], myPhoneCSV['Mobile1'],
                                                                  myPhoneCSV['SEID'], myPhoneCSV['Exam Date'] , myPhoneCSV['ExamTime']):
            if find(str(uid)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                regularHopeUpdate(phoneNum,examDate,examTime,uid)
                print(f"send successfully  to phone number :with {seid} - {str(phoneNum)} ")
    except Exception as e:
        print(f"Something wrong with {uid} phone number : {phoneNum} : {traceback.print_exc()} ")

def sendInvitePrompt():
    csvLoc = str(input("Enter the location of CSV\n"))
    myPhoneCSV = pd.read_csv(csvLoc)
    try:
        for phoneNum in myPhoneCSV['Mobile1']:
            if find(str(phoneNum)) and isValid(str(phoneNum)):  # and str(phoneNum) != "Unknown"
                inviteMessageJaipurHope2(str(phoneNum))
                print(f"send successfully  to phone number {phoneNum}")
    except Exception as e:
        print(f"Something wrong wit phone number : {phoneNum} : {traceback.print_exc()} ")


def find(name, path="/Users/harshit/PycharmProjects/kalyramessaging/Jodhpur/Growth/"):
    for root, dirs, files in os.walk(path):
        if name + ".json" in files:
            return False  # return false if found
        else:
            return True


# Python program to check if
# given mobile number is valid


def enterNumber(s):
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


# Driver Code
def isValid(s):
    global successCount
    global failedCount
    if (enterNumber(s)):
        successCount += 1
        return True
    else:
        failedCount += 1
        return False


# messagePrompt()
#sendCenterMessage("9555903247","110022","5 मार्च 2022","1","सुबह 9:00 AM","123321123123")
#messagePromptCenterUpdate()
#regularUpdatePrompt()
#sendInvitePrompt() #to be run at 24 March
# inviteMessageJaipurHope2("9555903247")
#inviteMessageJaipur("9555903247")
#sendAdmitCardInvite("9555903247")
messagePromptForJodhpur()
#messagePromptForJaipur()
#inviteMessageIndore("9555903247")\
#inviteMessageJodhpurHope("9555903247")
print(f'Success : {successCount} || Failed: {failedCount}')
