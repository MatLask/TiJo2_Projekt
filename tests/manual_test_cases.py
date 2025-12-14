manual_test_cases = [
    {"Given": "User opens main page", "When": "Page loads", "Then": "List of events is displayed"},
    {"Given": "User clicks 'Add Event'", "When": "Fills valid form and submits", "Then": "New event appears on main page"},
    {"Given": "User clicks 'Add Event'", "When": "Leaves title empty", "Then": "Error message appears"},
    {"Given": "User clicks 'Add Event'", "When": "Leaves date empty", "Then": "Error message appears"},
    {"Given": "User clicks 'Edit' on an event", "When": "Changes title and saves", "Then": "Changes are saved and displayed"},
    {"Given": "User clicks 'Edit'", "When": "Leaves required field empty", "Then": "Error message appears"},
    {"Given": "User clicks 'Delete'", "When": "Confirms deletion", "Then": "Event disappears from main page"},
    {"Given": "User clicks 'Done' on an event", "When": "Marks as done", "Then": "Event card shows strikethrough and gray"},
    {"Given": "User clicks 'Done' again", "When": "Marks as undone", "Then": "Event card returns to normal style"},
    {"Given": "User opens app on mobile", "When": "Page adjusts layout", "Then": "Cards stack vertically and buttons are visible"}
]
