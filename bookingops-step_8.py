# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: BookingOps
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
import re

@dataclass
class FilterConfig:
    status: Optional[str] = None
    category: Optional[str] = None
    owner: Optional[str] = None
    tag: Optional[List[str]] = field(default_factory=list)

def apply_filters(reservations: List[Dict], config: FilterConfig) -> List[Dict]:
    filtered = reservations
    
    if config.status is not None:
        pattern = re.compile(re.escape(config.status), re.IGNORECASE)
        filtered = [r for r in filtered if pattern.search(r.get("status", ""))]
    
    if config.category is not None:
        pattern = re.compile(re.escape(config.category), re.IGNORECASE)
        filtered = [r for r in filtered if pattern.search(r.get("category", ""))]
        
    if config.owner is not None:
        pattern = re.compile(re.escape(config.owner), re.IGNORECASE)
        filtered = [r for r in filtered if pattern.search(r.get("owner", ""))]
    
    if config.tag:
        tag_set = set(t.lower() for t in config.tag)
        def has_tag(res):
            res_tags = (res.get("tags") or "").lower().split(", ")
            return any(tag in res_tags for tag in tag_set)
        filtered = [r for r in filtered if has_tag(r)]
        
    return filtered
