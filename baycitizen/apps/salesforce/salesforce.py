from armstrong.apps.crm import UserBackend, GroupBackend, ProfileBackend

#potential settings

DEFAULT_ACCOUNT_TYPE= 'PersonAccount'

class SalesforceUsersBackend(UserBackend):

    def created(user, **payload) 
        h = get_connection()

        account = h.generateObject('Account')
        if last_name == '[Not provided]' and email:
            account.Name = ' '.join((first_name, email,))
        else:
            account.Name = ' '.join((first_name, last_name,))
        account.Type = payload['account_type'] or DEFAULT_ACCOUNT_TYPE
        account_result = h.create(account) 
        
        contact = h.generateObject('Contact')
        contact.FirstName = user.first_name
        contact.LastName = user.last_name
        contact.Email = user.email
        contact.PKey_Email__c = user.email
        
        contact.AccountId = user.id
    
        contact.Referral_Code__c = referral_code
        contact.Bonus_Gift__c = bonus_gift
        contact_result = h.create(contact)    

    def updated(self, user, **payload):
        query_result = h.query("SELECT Id,AccountId FROM Contact WHERE Email = '%s'" % user.email
        contact=query_result.records[0]
        
        if hasattr(contact,'AccountId') and contact.AccountId:
            account = h.retrieve('Name', 'Account', contact.AccountId)  
            if last_name == '[Not provided]' and email:
                account.Name = ' '.join((first_name, email,))
            else:
                account.Name = ' '.join((first_name, last_name,))
            account.Type = DEFAULT_ACCOUNT_TYPE
            account_result = h.update(account) 
        
        
        contact.FirstName = user.first_name
        contact.LastName = user.last_name
        contact.Email = user.email
        contact.Referral_Code__c = referral_code
        contact.Bonus_Gift__c = bonus_gift
        contact_result = h.update(contact)


class SalesforceGroupBackend(GroupBackend):
    def created(group, **payload):
    
    def updated(group, **payload):
