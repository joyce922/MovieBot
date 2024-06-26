"""Domain knowledge for the simulation.

The domain specifies the slots used for elicitation of preferences and for
inquiries.

In the example below, there are 6 slots in total, with 2 slots for elicitation
and 3 slots for inquiries.
```yaml
name: "MovieDomain"
slot_names:
  title: ["no_elicitation"]
  genre:
  keywords:

inquire_slots:
  - plot
  - year
  - actors
```
"""

from typing import List

from dialoguekit.core.domain import Domain


class SimulationDomain(Domain):
    def __init__(self, config_file: str) -> None:
        """Initializes the simulation domain."""
        super().__init__(config_file)

        if not {"inquire_slots"}.issubset(self._config):
            raise KeyError(
                "The domain configuration should contain the field "
                "'inquire_slots'."
            )

    def get_slot_names(self) -> List[str]:
        """Returns the list of slot names.

        Returns:
            List of slot names.
        """
        return list(self._config.get("slot_names").keys())

    def get_slot_names_elicitation(self) -> List[str]:
        """Returns the list of slot names for elicitation.

        Returns:
            List of slot names.
        """
        elicitation_slots = []
        slots = self._config.get("slot_names")
        for slot, params in slots.items():
            if params and "no_elicitation" in params:
                continue
            elicitation_slots.append(slot)
        return elicitation_slots

    def get_slot_names_inquiry(self) -> List[str]:
        """Returns list of slots name for inquiries."""
        return self._config.get("inquire_slots")
