from django.core.mail.backends.smtp import EmailBackend
import smtplib

class PatchedEmailBackend(EmailBackend):
    def open(self):
        try:
            self.connection = smtplib.SMTP(self.host, self.port, local_hostname=self.local_hostname, timeout=self.timeout)
            if self.use_tls:
                self.connection.starttls()  # ← patch: removed keyfile/certfile
            if self.username and self.password:
                self.connection.login(self.username, self.password)
            return True
        except:
            if not self.fail_silently:
                raise
            return False
