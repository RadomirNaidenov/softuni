class EmailValidator:

    def __init__(self, min_length: int, mails: list[str], domains: list[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, email: str):
        username, email_rest = email.split("@")
        mail, domain = email_rest.split(".")

        return self.__is_name_valid(username) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)



