from sys import maxsize
__author__ = "Grzegorz Holak"


# I decided to make first name and last name without default value, as rest can be blank
# only these 2 I decided to must have in each contact, so I changed order of parameters in method to make
# it easier. After all we could test more possibilities, fill some parts and left rest etc.
# init new contact

class Contact:
    def __init__(self, first_name, last_name, email=None, mobile_phone=None, middle_name=None, nick=None, title=None
                 , company=None
                 , address=None, home_phone=None, work_phone=None, fax=None, email2=None, email3=None, homepage=None
                 , birthday_year=None, ann_year=None, address2=None, home_phone2=None, notes=None, birthday_day=0
                 , birthday_month=0, ann_month=0, ann_day=0, contact_id=None, all_phones_from_home_page=None
                 , all_emails_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.mobile_phone = mobile_phone
        self.middle_name = middle_name
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthday_year = birthday_year
        self.ann_year = ann_year
        self.address2 = address2
        self.home_phone2 = home_phone2
        self.notes = notes
        # these are for options but in script need add 2 to this, dunno why, but it is working OK.
        self.birthday_day = birthday_day + 2
        self.birthday_month = birthday_month + 1
        self.ann_month = ann_month + 1
        self.ann_day = ann_day + 2
        self.contact_id = contact_id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s %s: %s: %s" % (self.contact_id, self.first_name, self.last_name, self.mobile_phone, self.email)

    def __eq__(self, other):
        return (self.contact_id is None or other.contact_id is None or self.contact_id == other.contact_id)\
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.contact_id:
            return int(self.contact_id)
        else:
            return maxsize
