import json
import functools

def to_json(func):
    @functools.wraps(func)
    def new_style(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return new_style

@to_json
def get_data():
    return {
        'data': 42
    }

if __name__ == "__main__":
    print(get_data())