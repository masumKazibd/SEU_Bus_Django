from django.shortcuts import render, Http404
 
ROUTES_DATA = [
    {
        "id": 1,
        "name": "Route - 1",
        "description": "Mirpur 10 to Campus via Shewrapara & Kazipara",
        "schedules": [
            {"bus_no": "Bus-01", "time": "07:30 AM", "direction": "Campus-bound"},
            {"bus_no": "Bus-01", "time": "05:15 PM", "direction": "Return"},
        ]
    },
    {
        "id": 2,
        "name": "Route - 2",
        "description": "Uttara House Building to Campus via Airport & Khilkhet",
        "schedules": [
            {"bus_no": "Bus-02", "time": "07:45 AM", "direction": "Campus-bound"},
            {"bus_no": "Bus-02", "time": "05:15 PM", "direction": "Return"},
        ]
    },
    {
        "id": 3,
        "name": "Route - 3",
        "description": "Dhanmondi 32 to Campus via Science Lab & Farmgate",
        "schedules": [
            {"bus_no": "Bus-03", "time": "08:00 AM", "direction": "Campus-bound"},
            {"bus_no": "Bus-03", "time": "05:30 PM", "direction": "Return"},
        ]
    },
    {
        "id": 4,
        "name": "Route - 4",
        "description": "Gulshan to Campus via R/A & Banani",
        "schedules": [
            {"bus_no": "Bus-04", "time": "08:15 AM", "direction": "Campus-bound"},
            {"bus_no": "Bus-04", "time": "05:45 PM", "direction": "Return"},
        ]
    },
    {
        "id": 5,
        "name": "Route - 5",
        "description": "Dhanmondi 32 to Campus via Science Lab & Farmgate",
        "schedules": [
            {"bus_no": "Bus-03", "time": "08:00 AM", "direction": "Campus-bound"},
            {"bus_no": "Bus-03", "time": "05:30 PM", "direction": "Return"},
        ]
    },
]

# all route list
def route_list(request):
    return render(request, 'schedule/route_list.html', {'routes': ROUTES_DATA})

# route detail view
def route_detail(request, route_id):
    route = next((r for r in ROUTES_DATA if r["id"] == route_id), None)
    if route is None:
        raise Http404("Route not found!")
    return render(request, 'schedule/route_detail.html', {'route': route})