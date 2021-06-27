
import smtplib

MY_EMAIL = "yukwokng@yahoo.com"
PASSWORD = "lkgpczgtbyunkabs"

with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)   # --- auth
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="billynyk@qq.com",
                        msg=f"Subject: TESTING"
                            f"\n\n"
                            f"TESTING body")
