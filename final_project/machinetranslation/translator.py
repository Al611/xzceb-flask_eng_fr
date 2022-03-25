'''This is a translator French-English, English-French lab for the Corusera
    "Python Project for AI & Application Development" course using IBM Watson translator
    by A Ouellet '''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
    )
language_translator.set_service_url(url)

def englishtofrench(englishtext):
    '''Takes an English string and return a French translated string'''
    if (englishtext=='' or englishtext is None) :
        return "Nothing to translate / Rien à traduire"
    translatedtext=language_translator.translate(englishtext,model_id='en-fr').get_result()
    frenchtext=translatedtext['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    '''Takes a French string and return an English translated string'''
    if (frenchtext=='' or frenchtext is None) :
        return "Nothing to translate / Rien à traduire"
    translatedtext=language_translator.translate(frenchtext,model_id='fr-en').get_result()
    englishtext=translatedtext['translations'][0]['translation']
    return englishtext
