## Start
```commandline
docker-compose up -d --build
```

### Check

POST http://localhost:8000/questions - add questions

Example body
```commandline
{
    "questions_num": 5
}
```
Example output
```commandline
{
    "id": 1,
    "question": "13,147-foot Boundary Peak,Area 51 (which we can't confirm or deny)",
    "answer": "Nevada",
    "created": "2022-07-27T01:50:35.537000"
}
```


GET http://localhost:8000/questions - see all questions

Example output
```commandline
[
    {
        "id": 1,
        "question": "13,147-foot Boundary Peak,Area 51 (which we can't confirm or deny)",
        "answer": "Nevada",
        "created": "2022-07-27T01:50:35.537000"
    },
    {
        "id": 2,
        "question": "A shoulder-held rocket launcher",
        "answer": "Bazooka",
        "created": "2022-07-27T00:57:04.810000"
    }
]
```