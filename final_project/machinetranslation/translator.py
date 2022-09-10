"""
Module docstring
"""
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-08-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """
    Translate English text to French
    """
    french_text = "text must be provided"
    # check for null input
    if english_text is None:
        return french_text

    try:
        # make a call to transation service
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr').get_result()
        # extract translated text
        french_text = translation.get("translations")[0].get("translation")
    except ApiException as ex:
        french_text = f"Method failed with status code {str(ex.code)} : {ex.message}"
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English
    """
    english_text = "text must be provided"
    # check for null input
    if french_text is None:
        return english_text
    try:
        # make a call to translation service
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en').get_result()
        # extract translated text
        english_text = translation.get("translations")[0].get("translation")
    except ApiException as ex:
        english_text = f"Method failed with status code {str(ex.code)} : {ex.message}"
    return english_text
