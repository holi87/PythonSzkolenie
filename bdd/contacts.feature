Scenario Outline: Add new contact
  Given a contacts list
  Given a contact with <first_name> and <last_name>
  When I add the contact to list
  Then the new contact list is equal to new list with added contact

  Examples:
  | first_name | last_name |
  | imie1 | nazwisko1 |
  | imie2 | nazwisko2 |


Scenario: Delete a contact
  Given a non-empty contacts list
  Given a random contact
  When I delete a random contact from list
  Then the new contacts list is equal to olg contacts list without deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contacts list
  Given a random contact
  When I modify <first_name> and <last_name> of contact from list
  Then the new contact is modified with <first_name> and <last_name>

  Examples:
  | first_name | last_name |
  | nowe_imie1 | nowe_nazwisko1 |
  | nowe_imie2 | nowe_nazwisko2 |