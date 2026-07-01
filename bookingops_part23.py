# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: BookingOps
def manage_tags(resource, tags):
    if isinstance(tags, str):
        tag_set = {tags}
    else:
        tag_set = set(tags)
    for t in tag_set:
        resource.tags.add(t)
    return resource

def remove_tag(resource, tag):
    if tag in resource.tags:
        resource.tags.discard(tag)
    return resource

def get_tag_summary(resources, target_tags=None):
    summary = {}
    all_resources = resources if isinstance(resources, list) else [resources]
    for r in all_resources:
        current_tags = set(r.tags)
        if target_tags is None:
            summary[r.id] = sorted(current_tags)
        else:
            matched = sorted(current_tags & set(target_tags))
            summary[r.id] = matched if matched else []
    return summary

def filter_by_tag(resources, tag):
    return [r for r in resources if tag in r.tags]
