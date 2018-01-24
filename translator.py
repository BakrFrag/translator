import googletrans;
from tkinter import *;
##LANGUAGES = {
##    'af': 'afrikaans',
##    'sq': 'albanian',
##    'am': 'amharic',
##    'ar': 'arabic',
##    'hy': 'armenian',
##    'az': 'azerbaijani',
##    'eu': 'basque',
##    'be': 'belarusian',
##    'bn': 'bengali',
##    'bs': 'bosnian',
##    'bg': 'bulgarian',
##    'ca': 'catalan',
##    'ceb': 'cebuano',
##    'ny': 'chichewa',
##    'zh-cn': 'chinese (simplified)',
##    'zh-tw': 'chinese (traditional)',
##    'co': 'corsican',
##    'hr': 'croatian',
##    'cs': 'czech',
##    'da': 'danish',
##    'nl': 'dutch',
##    'en': 'english',
##    'eo': 'esperanto',
##    'et': 'estonian',
##    'tl': 'filipino',
##    'fi': 'finnish',
##    'fr': 'french',
##    'fy': 'frisian',
##    'gl': 'galician',
##    'ka': 'georgian',
##    'de': 'german',
##    'el': 'greek',
##    'gu': 'gujarati',
##    'ht': 'haitian creole',
##    'ha': 'hausa',
##    'haw': 'hawaiian',
##    'iw': 'hebrew',
##    'hi': 'hindi',
##    'hmn': 'hmong',
##    'hu': 'hungarian',
##    'is': 'icelandic',
##    'ig': 'igbo',
##    'id': 'indonesian',
##    'ga': 'irish',
##    'it': 'italian',
##    'ja': 'japanese',
##    'jw': 'javanese',
##    'kn': 'kannada',
##    'kk': 'kazakh',
##    'km': 'khmer',
##    'ko': 'korean',
##    'ku': 'kurdish (kurmanji)',
##    'ky': 'kyrgyz',
##    'lo': 'lao',
##    'la': 'latin',
##    'lv': 'latvian',
##    'lt': 'lithuanian',
##    'lb': 'luxembourgish',
##    'mk': 'macedonian',
##    'mg': 'malagasy',
##    'ms': 'malay',
##    'ml': 'malayalam',
##    'mt': 'maltese',
##    'mi': 'maori',
##    'mr': 'marathi',
##    'mn': 'mongolian',
##    'my': 'myanmar (burmese)',
##    'ne': 'nepali',
##    'no': 'norwegian',
##    'ps': 'pashto',
##    'fa': 'persian',
##    'pl': 'polish',
##    'pt': 'portuguese',
##    'pa': 'punjabi',
##    'ro': 'romanian',
##    'ru': 'russian',
##    'sm': 'samoan',
##    'gd': 'scots gaelic',
##    'sr': 'serbian',
##    'st': 'sesotho',
##    'sn': 'shona',
##    'sd': 'sindhi',
##    'si': 'sinhala',
##    'sk': 'slovak',
##    'sl': 'slovenian',
##    'so': 'somali',
##    'es': 'spanish',
##    'su': 'sundanese',
##    'sw': 'swahili',
##    'sv': 'swedish',
##    'tg': 'tajik',
##    'ta': 'tamil',
##    'te': 'telugu',
##    'th': 'thai',
##    'tr': 'turkish',
##    'uk': 'ukrainian',
##    'ur': 'urdu',
##    'uz': 'uzbek',
##    'vi': 'vietnamese',
##    'cy': 'welsh',
##    'xh': 'xhosa',
##    'yi': 'yiddish',
##    'yo': 'yoruba',
##    'zu': 'zulu',
##    'fil': 'Filipino',
##    'he': 'Hebrew'
##};
root=Tk();
translator=googletrans.Translator();
root.geometry("450x450");
root.title("Translator");
root.resizable(0,0);
global str11,str22,str33;
str1=StringVar();
str2=StringVar();
str3=StringVar();
frame=Frame(root);
frame.pack();
label1=Label(frame,text="Enter Word/Sentence",font=("Helvetica", 18));
label1.pack();
entry1=Entry(frame,width=50,textvariable=str1);
entry1.pack();
label2=Label(frame,text="Source Languaage Code",font=("Helvetica", 18));
label2.pack();
entry2=Entry(frame,width=50,textvariable=str2);
entry2.pack();
label3=Label(frame,text="Destination Language Code",font=("Helvetica", 18));
label3.pack();
entry3=Entry(frame,width=50,textvariable=str3);
entry3.pack();

def translated():
    global str11,str22,str33;
    str11=str1.get();
    str22=str2.get();
    str33=str3.get();
    if str22=="":
           str22="en";
    elif str33=="":
           str33="ar";
    result=translator.translate(str11,src=str22,dest=str33);
    message=result.text
    text.delete("1.0",END)
    text.insert(END,message);
button=Button(frame,text="Translate Result",font=("Helvetica",20),padx=10,pady=10,command=translated)
button.pack()
text=Text(frame,font=("arial",14),width=50,height=10);
text.pack();
root.mainloop();
