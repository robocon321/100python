import smtplib

sender = "robocon321n@gmail.com"
password = "rjkxcoqivkizxgti"
receiver = "18130164@st.hcmuaf.edu.vn"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user = sender, password = password)
    connection.sendmail(
        from_addr = sender,
        to_addrs = receiver,
        msg = "Subject: Hello\n\nThis is the body of my email."
    )

    