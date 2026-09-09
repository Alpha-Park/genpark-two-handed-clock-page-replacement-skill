import sys
import json
from client import TwoHandedClock

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "access_pages":
        clock = TwoHandedClock(params.get("frames", 4))
        res = [clock.access_page(p) for p in params.get("pages", [])]
        return {"access_log": res}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
