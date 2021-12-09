# class Solution:
#     def __init__(self):
#         self.pattern_dot = re.compile(r"\+(.+)@")
#         self.pattern_plus = re.compile(r"\+(.+)@")
    
#     def numUniqueEmails(self, emails: List[str]) -> int:
#         ret = []
#         for email in emails:
#             ret.append(self.normalize(email))
#         return len(set(ret))
        
#     def normalize(self, email):
#         email = self.pattern_dot.sub(r"@", email)
#         email = self.pattern_plus.sub(r"@", email)
#         return email

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ret = []
        for email in emails:
            ret.append(self.normalize(email))
        return len(set(ret))
        
    def normalize(self, email):
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".", "")
        return local + "@" + domain
