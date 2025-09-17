import phonenumbers
from phonenumbers import geocoder,carrier

def main():    
    print("*********** Telefon Lokasyon ve Servis Sağlayıcı Bilgisi ***********")
    phone_input=input("Telefon numarasını ülke kodu ile birlikte girin(örn:+9055555555): ").strip()

    try:
        number=phonenumbers.parse(phone_input,None)

        if not phonenumbers.is_valid_number(number):
            print("⚠️ Geçersiz bir telefon numarası girdiniz!")
            return
        
        location=geocoder.description_for_number(number,"tr")
        operator=carrier.name_for_number(number,"tr")

        international=phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        national=phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.NATIONAL)
        e164=phonenumbers.format_number(number,phonenumbers.PhoneNumberFormat.E164)

        print("\n--- Bilgiler ---")
        print(f"Numara (Uluslararası): {international}")
        print(f"Numara (Ulusal): {national}")
        print(f"Numara (E.164): {e164}")
        print(f"Lokasyon: {location}")
        print(f"Servis Sağlayıcı: {operator}")

    except phonenumbers.NumberParseException:
        print("⚠️ Telefon numarası çözümlenemedi. Lütfen doğru formatta girin (örn: +905555555555)")

if __name__=="__main__":
    main()