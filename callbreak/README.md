# API

This document details the API interactions between the game server
and the player.

The response will always be in the format
```json
{
    "result": "success/failure",
    "data" : {"relevant data on success",
                "reason on failure"}
}
```

## Request Endpoints

Name                     | Description
-------------------------|--------------------------------------
`break`  | Only valid at relevant points in the game. Request `data = {'<suit><rank>'}`. This would be equivalent to playing the card. |
`call`   | Only valid at relevant points in the game. Request `data = {'<int-call-value>'}`
`get`     | Get card played in a round by a player at a move. Request `data = {'round' : '1-5', 'player' = '1-4', break = '0-13'}`. Response is in the form `data = {'<suit><rank>'}` which is say the player played that card. To get the hand that a player was dealt at the beginning of the round use `break=0`; only applicable if the requester is also the player being queried
`new`     | Restart a game. In doing so, your last game will no longer exist. `http://127.0.0.1:5000/new`. No `data` returned.
`status` | Return last played `data = {'round' : '1-5', 'player' = '1-4', break = '0-13'}`. The format is the same as is used for sending data to the `get` endpoint. `
`score` | Valid at any point in the game. `data` is ignored for requests. Returns `data = {[ _ , _ , _ , _ ], [....], [....], [....], [....]}`. The scores are ordered by rounds and players. The dealer in the first round is the first player in all reporting. The score is reported imagining a counterclockwise arrangement from the first player.
