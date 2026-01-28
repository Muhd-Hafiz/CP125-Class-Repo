def synchronize_databases(legacy_list, modern_set, blacklist):
    sanitized_legacy_ids = set()
    for record_id, email in legacy_list:
        if email not in blacklist:
            sanitized_legacy_ids.add(record_id)

    lost_set = sanitized_legacy_ids - modern_set
    ghost_set = modern_set - sanitized_legacy_ids

    return lost_set, ghost_set

    