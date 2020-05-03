from typing import Dict


def lower_strs(payload: Dict) -> Dict:
    return {
        key: value.lower() if isinstance(value, str) else value
        for key, value in payload.items()
    }
