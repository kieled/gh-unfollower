<h2 align="center">Unfollower unmutual subscribers [GitHub]</h2>
<h4 align="center"><strong>using GraphQL API</strong></h4>

<p align="center"><strong>If you have a lot of github followings and / or followers this script can helps you. It will unfollow from all your
followings that not follows to you</strong></p>

### :pill: __Usage__

1. Clone repo

```
git clone https://github.com/kieled/gh-unfollower.git
```

2. Rename `.env.example` to `.env` and fill github token
3. Run script `with-poetry.sh` or `without-poetry.sh` depending on whether you have installed `poetry`


### :recycle: Dependencies

- __Python__ [^3.11]
- __python-graphql-client__ [^0.4.3] - For making GraphQL requests to Github API
- __pydantic[dotenv]__ [^1.10.9] - For validating and type hinting
- __aiofiles__ [^23.1.0] - For reading GraphQL schemas from files
- __types-aiofiles__ [^23.1.0.4] - For type hinting aiofiles
