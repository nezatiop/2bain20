def buildContacts(name, phone):
    contact = set()
    for i in range(len(name)):
        contact[name] = phone
    return {"contacts": contact}