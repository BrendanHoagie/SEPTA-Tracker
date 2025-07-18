import requests

_BASIC_URL = "https://www3.septa.org/api/"

_REQUEST_URLS = {
    "regional_rail_arrivals": "Arrivals/index.php",
    "list_all_trains": "TrainView/index.php",
    "next_to_arrive": "NextToArrive/index.php",
    "trolley_location_by_route": "TransitView/index.php",
    "all_trolley_location": "TransitViewAll/index.php",
    "trolley_detours": "BusDetours/index.php",
    "alerts_no_message": "Alerts/index.php",
    "alerts_with_message": "Alerts/get_alert_data.php",
    "elevator_outages": "Elevator/index.php",
    "regional_rail_schedules": "RRSchedules/index.php",
    "trolley_schedules": "BusSchedules/index.php",
    "trolley_schedules_as_sms": "sms/index.php",
    "list_all_trolley_stops": "Stops/index.php",
    "locations": "locations/get_locations.php",
}
