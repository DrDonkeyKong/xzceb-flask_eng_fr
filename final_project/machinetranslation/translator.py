
""" This is a module docstring
"""
import json
import os
from ibm_watson import LanguageTranslatorV3, ApiException
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
language_translator.set_disable_ssl_verification(True)

def englishToFrench(english_text: str) -> str:
    """ Translates english to french text
    """
    if english_text in ["", None]:
        return ""
    try:
        translation = language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()
        print(translation)
        if translation and translation["translations"] and len(translation["translations"]) > 0:
            french_text = json.dumps(translation["translations"][0]["translation"], indent=2, ensure_ascii=False)
        return french_text.strip('"')
    except ApiException as ex:
        print(f"Method failed with status code {ex.code}: {ex.message}")


def frenchToEnglish(french_text: str) -> str:
    """ Translates french to english text
    """
    if french_text in ["", None]:
        return ""
    try:
        translation = language_translator.translate(
            text=french_text,
            model_id='fr-en'
        ).get_result()
        if translation and translation["translations"] and len(translation["translations"]) > 0:
            english_text = json.dumps(translation["translations"][0]["translation"], indent=2, ensure_ascii=False)
        return english_text.strip('"')
    except ApiException as ex:
        print(f"Method failed with status code {ex.code}: {ex.message}")
