import asyncio
from collections import defaultdict
from itertools import islice, chain

from client import prepare_request


async def unfollow(uid: str):
    await prepare_request('unfollow', {'id': uid})
    print(f'unfollowed {uid}')


async def retrieve(i, afters):
    return {
        'data': await prepare_request(i, {'after': afters.get(i)}),
        'name': i
    }


def chunks(iterable, size):
    iterator = iter(iterable)
    for first in iterator:
        yield chain([first], islice(iterator, size - 1))


async def main():
    print('Starting...')
    result = defaultdict(list)
    denied = []
    afters = defaultdict()
    items = ['followers', 'following']
    while len(denied) < 2:
        list_result = await asyncio.gather(*[
            retrieve(i, afters)
            for i in items if i not in denied
        ])
        for d in list_result:
            i = d['name']
            data = d['data']['data']['viewer'][i]
            if not data['pageInfo']['hasNextPage'] or not len(data['nodes']):
                denied.append(i)
            result[i].extend(map(lambda x: x['id'], data['nodes']))
            afters[i] = data['pageInfo']['endCursor']
    for i in chunks(filter(lambda x: x not in result['followers'], result['following']), 5):
        await asyncio.gather(*[
            unfollow(d)
            for d in i
        ])


if __name__ == '__main__':
    asyncio.run(main())
