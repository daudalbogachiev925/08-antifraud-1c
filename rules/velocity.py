from datetime import datetime, timedelta

def check(tx, history):
    hour_ago = datetime.now() - timedelta(hours=1)
    recent = [t for t in history if t['ts'] > hour_ago
              and t['client_id'] == tx['client_id']]
    return {'triggered': len(recent) > 10, 'reason': 'velocity'}
