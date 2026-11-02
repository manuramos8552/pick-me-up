# events.py - Interaction events and the logger that stores them
import time


class InteractionEvent:
    _next_id = 1

    def __init__(self, sku, slot_id, picked_up_at, duration_sec):
        self.event_id = InteractionEvent._next_id
        InteractionEvent._next_id += 1
        self.sku = sku
        self.slot_id = slot_id
        self.picked_up_at = picked_up_at
        self.duration_sec = duration_sec

    def to_dict(self):
        return {
            "id": self.event_id,
            "sku": self.sku,
            "slot": self.slot_id,
            "picked_up_at": self.picked_up_at,
            "duration_sec": self.duration_sec,
        }


class EventLogger:
    """Keeps recent events in memory (the Pico has limited RAM)."""

    def __init__(self, max_events=500):
        self._events = []
        self._max_events = max_events

    def log(self, event):
        self._events.append(event)
        if len(self._events) > self._max_events:
            self._events.pop(0)

    def count_by_sku(self):
        counts = {}
        for e in self._events:
            counts[e.sku] = counts.get(e.sku, 0) + 1
        return counts

    def clear(self):
        self._events = []
