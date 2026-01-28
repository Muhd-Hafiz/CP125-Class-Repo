def audit_zero_trust(baseline_set, current_log_list):
   current_log = set()
   for log in current_log_list:
         current_log.add(log)
   
   authorized = set()
   Alerts = set()
   for entry in current_log:
      if entry not in baseline_set:
         authorized.add(entry)
      else:
         Alerts.add(entry)

   inactive = set()
   for entry in baseline_set:
      if entry not in current_log:
         inactive.add(entry)

   return Alerts, authorized, inactive