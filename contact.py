__author__ = "Grzegorz Holak"


# I decided to make first name, last name, mobile phone and email without default value, as rest can be blank
# only these 4 I decided to must have in each contact, so I changed order of parameters in method to make
# it easier. After all we could test more possibilities, fill some parts and left rest etc.
# init new contact

class Contact:
    def __init__(self, first_name, last_name, email, mobile_phone, middle_name="", nick="", title="", company=""
                 , address="", home_phone="", work_phone="", fax="", email2="", email3="", homepage=""
                 , birthday_year="", ann_year="", address2="", home_phone2="", notes="", birthday_day="0"
                 , birthday_month="0", ann_month="0", ann_day="0"):
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
        # these are for options but in script month 1 = January, 2 = Febuary etc. and for days 1 = first, 2= second
        # but this part of script not working correctly, probably need to change something
        self.birthday_day = birthday_day
        self.birthday_month = birthday_month
        self.ann_month = ann_month
        self.ann_day = ann_day
