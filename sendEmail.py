from flask import Flask, request, jsonify
import requests




def refresh_the_token(tokens):
    try:
        data = {
            "client_id": "4dccd1f5-dc76-4b7d-b00f-e61d6b818fe2",
            "scope": "User.Read Mail.Read Mail.Send",
            "refresh_token": tokens["refreshToken"],
            "grant_type": "refresh_token",
            "client_secret": "Fgb8Q~7SwZZ5gCZsddrvxNre0DY6ntFDvJjMUbqQ",
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }

        response = requests.post(
            "https://login.microsoftonline.com/common/oauth2/v2.0/token",
            data=data,
            headers=headers,
        )

        response_data = response.json()
        access_token = response_data.get("access_token")
        refresh_token = response_data.get("refresh_token")

        return {"accessToken": access_token, "refreshToken": refresh_token}
    except Exception as e:
        print("Error refreshing token:", e)
        raise e

def send_email(email_address, link, old_tokens):
    try:
        tokens = refresh_the_token(old_tokens)
        authorization_header = {"Authorization": f"Bearer {tokens['accessToken']}"}
        content_type_header = {"Content-Type": "application/json"}

        send_mail_data = {
            "message": {
                "subject": "Push Notification",
                "body": {
                    "contentType": "Text",
                    "content": f"News content is against the goverment at link: {link}",
                },
                "toRecipients": [
                    {
                        "emailAddress": {
                            "address": email_address,
                        },
                    },
                ],
            },
        }

        response = requests.post(
            "https://graph.microsoft.com/v1.0/me/sendMail",
            json=send_mail_data,
            headers={**authorization_header, **content_type_header},
        )

        # Check if the response status code indicates success (2xx)
        if response.status_code // 100 == 2:
            print("Mail sent successfully.")
        else:
            print("Error sending mail. Status Code:", response.status_code)

        # Optionally, you can print the response content for debugging
        print("Response Content:", response.text)
    except Exception as e:
        print("Error:", e)




tokens = {'accessToken': 'eyJ0eXAiOiJKV1QiLCJub25jZSI6IjhTRTNiVGZTMUNzbFkwa0VwSUNFeFFYMjJpTnltOFd2VXZHVWZTU1p4SW8iLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84NGMzMWNhMC1hYzNiLTRlYWUtYWQxMS01MTlkODAyMzNlNmYvIiwiaWF0IjoxNjk1NDE1MjA2LCJuYmYiOjE2OTU0MTUyMDYsImV4cCI6MTY5NTQyMDg5NiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFUUUF5LzhVQUFBQXFUOU5iZ0U2NFpJRXlzelZ1ZTFoaFRYSE45YzA3V1ZXYmJKTXBiT0doWGNTNkZyeG5FYTNlWDlLYnpuR085dmoiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6Im1zdXNkZXYiLCJhcHBpZCI6IjRkY2NkMWY1LWRjNzYtNGI3ZC1iMDBmLWU2MWQ2YjgxOGZlMiIsImFwcGlkYWNyIjoiMSIsImZhbWlseV9uYW1lIjoiQ2hhbmRyYXNla2FyYW4iLCJnaXZlbl9uYW1lIjoiTmlzaGFudGgiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxMjIuMTg3LjExNy4xNzkiLCJuYW1lIjoiTmlzaGFudGggQ2hhbmRyYXNla2FyYW4iLCJvaWQiOiI4ZjdmNWQzNS03ODkzLTQ0ZDgtYWVhYS1jMjA2N2VmYmVmZGQiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDI2OEI2MEU1RiIsInJoIjoiMC5BUVFBb0J6RGhEdXNyazZ0RVZHZGdDTS1id01BQUFBQUFBQUF3QUFBQUFBQUFBQUVBSjguIiwic2NwIjoiQ2FsZW5kYXJzLlJlYWQgQ2FsZW5kYXJzLlJlYWRXcml0ZSBNYWlsLlJlYWQgTWFpbC5SZWFkV3JpdGUgTWFpbC5TZW5kIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6Im9rblZVeDM2ejhqa21LWVoxSVdQWWE3TGZmZzRTd05zdWZUWWtNQTFQeXMiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiI4NGMzMWNhMC1hYzNiLTRlYWUtYWQxMS01MTlkODAyMzNlNmYiLCJ1bmlxdWVfbmFtZSI6Ik5pc2hhbnRoLkNoYW5kcmFzZWthcmFuQHN0dWRlbnRhbWJhc3NhZG9ycy5jb20iLCJ1cG4iOiJOaXNoYW50aC5DaGFuZHJhc2VrYXJhbkBzdHVkZW50YW1iYXNzYWRvcnMuY29tIiwidXRpIjoiYzBnOE52Ykc0a0dGcndvN1ZUNkVBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19zdCI6eyJzdWIiOiJIU3ZQQkxocUFVWklraTAtcVN3RjdhX0VYN0xoTGlsVVVxZDdSRUlyNTlzIn0sInhtc190Y2R0IjoxMzYyNTIyNDY4fQ.ndwpXx1mtBi-auOUBRd3k4T2XHtX_Pj1tykAVKMn1yT0bhjt7cr9lEZ4ncaPR8LyyZaL7Zt6OvsPwXFcne8P7LHufopZSR4RaFmzNW-iF8odcOa8wJRPdwekHqhgHBDtf6r4CDNqwVFsYhh_NizPFObKgOqsihrJL0HI3yF5qEUEi5NrwHPa1xHn4pSjOIXdUOtto9S-cUesB6Pz2N8ebPdSy7DOsj9FLUygfW62uGehZSK-ENmclAeXbykkd5m56F5idPZ95bJ5wp85X4V7fGven8FtSfDRXh8CB2ypsGR26ZQn0sEi7eD6e4a8w_3tFGItAfgpIHBn1b3Eam0zDA', 'refreshToken': '0.AQQAoBzDhDusrk6tEVGdgCM-b_XRzE123H1LsA_mHWuBj-IEAJ8.AgABAAEAAAAtyolDObpQQ5VtlI4uGjEPAgDs_wUA9P8kxwL6lKbOf9S3Tt2mo1BOoGFIXaPtSd_nxft2nRIuaaa5pPFU_Ri-M0idRrU29J69aPuCRaD79Q73c6FtDEL3-QL_0uBX6vTbgdbilKq_05IWO38QLaFNfWUK4KQWyx4wmpGS3c4ZdxraFPNv4MKyvxPX7V51w2mSLoThXBthOBmdbLJjDfhAMBAFsX52LjlSFbebLm1hQW2Uda1AHluE2y25ahzqsUk4x5o4Sy4WJC4uOCaLqMRJyw2qr2KQpLvKM-NSisKqb5Mx4kLX2QCRMf7axNAGDLu077LPR-n98fo2sNuYn6nKnvIoe02W5_abB_50jp9tvYQD77kWTV665426UvdhMvQg7YpkkoreDIO4aL3vA6wK0UjbjrQnqcJ56eXD6pOs5AH9xkL-K4czDVyz37lcSrQbKQ7lQY9xxRxZrxeAiFQUM5KyVjGoiH5rnMs_MNcdgTGB2tOSLPSzTQt_WB2RrdSAiIq-98BfqN4dYb7M3iwxdTbkqEXjOxQT2iKbvIBkEqQqZ7gy6aFjCfL3tkQ2hLYNLNn6JQ8Jca-akE2Rrql3p-OtH8k6KiT7N6hwHYDvO-clEyQtpVLacdnv3nq8NkzusQjcRkL5GBxqeftbPPrgk79BU3m-FAnXvKDTpNjhWWIQmUekFHNBsDcAOJOP1aOrD8CIKxfEMbllhgOeP087qM3Y7aSKWZXDmMXVqaKX6SV99O6g5K1qqIkK50WB-nUQpqIQwlSJpWkH6ayUf_aLWFwpDnJH'}

# send_email('nishanth.c2021@vitstudent.ac.in', "www.google.com", tokens)
