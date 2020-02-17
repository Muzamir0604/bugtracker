from bug.models import Bug
from users.models import CustomUser
import rules
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

@rules.predicate
def is_reporter(CustomUser, Bug):
    # user = get_user_model()
    return Bug.reported_by == CustomUser

is_analyst = rules.is_group_member('Analysts')
is_supervisor = rules.is_group_member('Supervisors')
is_developer = rules.is_group_member('Developers')

#rules
rules.add_rule('can_read_bug', is_reporter & is_analyst | is_supervisor)
rules.add_rule('can_change_bug', is_reporter & is_analyst | is_supervisor)
rules.add_rule('can_delete_bug', is_reporter | is_supervisor )
rules.add_rule('can_add_bug', is_analyst)

# permissions
rules.add_perm('bug.read_bug', is_reporter & is_analyst | is_supervisor)
rules.add_perm('bug.change_bug', is_reporter & is_analyst | is_supervisor)
rules.add_perm('bug.delete_bug', is_reporter | is_supervisor)
rules.add_perm('bug.add_bug', is_analyst)



# User =  get_user_model()
# muthubug = Bug.objects.get(pk=38)
# print("Rules:Reported_by: %r"%(muthubug.reported_by))
# farzana =  User.objects.get(username="farzana")
# print("farzana can change bug: %r "%(rules.test_rule('can_change_bug', farzana, muthubug)))
# # muzamir =  User.objects.get(username="muzamir")
# print("farzaana can change bug: %r"%(rules.test_rule('can_delete_bug', farzana, muthubug)))
# print("bug change : %r "% (farzana.has_perm('bug.change_bug', muthubug)))
# print("bug delete : %r "% (farzana.has_perm('bug.delete_bug', muthubug)))
