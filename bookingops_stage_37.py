# === Stage 37: Add recommendations for the next useful action ===
# Project: BookingOps
def recommend_next_actions(booking_ops):
    """Generate actionable recommendations based on current booking state."""
    recommendations = []
    
    # Check for underutilized resources that could take more bookings
    for resource in booking_ops.get_resources():
        utilization = calculate_utilization(resource)
        if utilization < 0.3 and len(resource.bookings) > 0:
            recommendations.append({
                'action': 'consider_promoting_booking',
                'resource_id': resource.resource_id,
                'reason': f'Resource {resource.resource_name} is underutilized ({utilization:.1%})'
            })
    
    # Check for resources with no bookings that could benefit from new reservations
    idle_resources = [r for r in booking_ops.get_resources() if len(r.bookings) == 0]
    if idle_resources:
        recommendations.append({
            'action': 'create_new_booking',
            'suggested_resource_ids': [r.resource_id for r in idle_resources],
            'reason': f'{len(idle_resources)} resource(s) have no current bookings'
        })
    
    # Check for customers who could book more resources
    active_customers = booking_ops.get_active_customers()
    if active_customers:
        recommendations.append({
            'action': 'expand_customer_bookings',
            'customer_ids': [c.customer_id for c in active_customers],
            'reason': f'{len(active_customers)} customers have existing bookings'
        })
    
    # Check for upcoming conflicts to prepare mitigation
    conflicts = booking_ops.get_conflicts()
    if conflicts:
        recommendations.append({
            'action': 'resolve_scheduling_conflict',
            'conflict_details': conflicts,
            'reason': f'{len(conflicts)} scheduling conflict(s) detected'
        })
    
    return recommendations

if __name__ == '__main__':
    # Example usage with sample data
    sample_resources = [
        {'resource_id': 'room_1', 'resource_name': 'Conference Room A', 'capacity': 10, 'bookings': [{'booking_id': 'b1'}]},
        {'resource_id': 'room_2', 'resource_name': 'Meeting Room B', 'capacity': 5, 'bookings': []},
        {'resource_id': 'room_3', 'resource_name': 'Training Hall', 'capacity': 50, 'bookings': [{'booking_id': 'b1'}, {'booking_id': 'b2'}]}
    ]
    
    sample_customers = [
        {'customer_id': 'c1', 'name': 'Alice Corp'},
        {'customer_id': 'c2', 'name': 'Bob Inc'},
        {'customer_id': 'c3', 'name': 'Charlie LLC'}
    ]
    
    booking_ops = {
        'resources': sample_resources,
        'customers': sample_customers,
        'conflicts': []
    }
    
    recs = recommend_next_actions(booking_ops)
    for i, rec in enumerate(recs, 1):
        print(f"Recommendation {i}: {rec['action']} - {rec['reason']}")
